"""Terminal UI for PyBLOCK AI Assistant."""

import sys
import time

import qrcode

from shared.display import clear
from pblogo import blogo

from .client import AstrolexisClient
from .context import gather_node_context


def ai_menu(path, lndconnectload=None):
    """Main AI assistant menu. Requires Astrolexis token in config."""
    from config import cfg

    token = cfg.settings.get("astrolexis_token", "")
    if not token:
        token = _setup_token(cfg)
        if not token:
            return

    client = AstrolexisClient(token)

    # Verify connection
    try:
        info = client.verify()
    except Exception as e:
        clear()
        blogo()
        print(f"\n  Error connecting to Astrolexis: {e}")
        print("  Check your token in Settings.\n")
        input("  Press Enter to continue...")
        return

    balance = info["balance_sats"]
    _chat_loop(client, path, lndconnectload, balance)


def _setup_token(cfg):
    """First-time token setup."""
    clear()
    blogo()
    print("""
  \033[1;37;40mAI Assistant Setup\033[0;37;40m

  Powered by \033[1;36;40mAstrolexis KCode\033[0;37;40m

  To use the AI Assistant, you need an Astrolexis token.
  Get yours at: \033[1;33;40mhttps://astrolexis.com/pyblock\033[0;37;40m

  Enter your token below, or press Enter to cancel.
""")
    token = input("  Token: ").strip()
    if not token:
        return None

    if not token.startswith("astrolexis_"):
        print("\n  Invalid token format. Must start with 'astrolexis_'")
        input("  Press Enter to continue...")
        return None

    # Save to config
    settings = cfg.settings
    settings["astrolexis_token"] = token
    cfg.save("pyblocksettings.conf", settings)
    print("\n  \033[1;32;40mToken saved.\033[0;37;40m")
    time.sleep(1)
    return token


def _chat_loop(client, path, lndconnectload, balance):
    """Main chat loop."""
    conversation = []

    while True:
        try:
            clear()
            blogo()
            print(f"""
  \033[1;37;40mAI Assistant\033[0;37;40m
  Powered by \033[1;36;40mAstrolexis KCode\033[0;37;40m
  Balance: \033[1;32;40m{balance:,}\033[0;37;40m sats

  Type your question, or:
    \033[1;33;40mT\033[0;37;40m  Top Up Balance
    \033[1;33;40mU\033[0;37;40m  Usage History
    \033[1;33;40mC\033[0;37;40m  Clear Conversation
    \033[1;33;40mQ\033[0;37;40m  Quit
""")

            # Show conversation history (last 3 exchanges)
            if conversation:
                print("  \033[0;37;40m--- Conversation ---\n")
                for msg in conversation[-6:]:
                    if msg["role"] == "user":
                        print(f"  \033[1;32;40m> {msg['content']}\033[0;37;40m")
                    else:
                        print(f"  {msg['content']}")
                    print()

            user_input = input("  \033[1;32;40m> \033[0;37;40m").strip()
            if not user_input:
                continue

            upper = user_input.upper()
            if upper == "Q":
                break
            if upper == "T":
                balance = _topup_flow(client)
                continue
            if upper == "U":
                _show_usage(client)
                continue
            if upper == "C":
                conversation = []
                continue

            # Build messages with conversation history
            conversation.append({"role": "user", "content": user_input})

            # Gather node context
            context = gather_node_context(path, lndconnectload)

            # Stream response
            print()
            full_response = ""
            try:
                for chunk in client.chat(
                    conversation, node_context=context
                ):
                    if chunk.get("type") == "content_block_delta":
                        text = chunk.get("delta", {}).get("text", "")
                        sys.stdout.write(text)
                        sys.stdout.flush()
                        full_response += text
                print("\n")

                # Add response to conversation
                conversation.append({
                    "role": "assistant", "content": full_response
                })

                # Update balance from billing info if available
                if hasattr(chunk, "get") and chunk.get("_billing"):
                    balance = chunk["_billing"]["balance_sats"]
                else:
                    try:
                        balance = client.get_balance()
                    except Exception:
                        pass

            except requests.exceptions.HTTPError as e:
                if e.response and e.response.status_code == 402:
                    data = e.response.json()
                    print(
                        f"\n  \033[1;31;40mInsufficient balance "
                        f"({data.get('balance_sats', 0)} sats).\033[0;37;40m"
                    )
                    print(
                        f"  Estimated cost: "
                        f"{data.get('estimated_cost', '?')} sats."
                    )
                    print("  Press T to top up.\n")
                    # Remove the unanswered user message
                    conversation.pop()
                else:
                    print(f"\n  \033[1;31;40mError: {e}\033[0;37;40m\n")
                    conversation.pop()

            input("  Press Enter to continue...")

        except KeyboardInterrupt:
            break


def _topup_flow(client):
    """Lightning top-up flow. Returns new balance."""
    clear()
    blogo()
    print("""
  \033[1;37;40mTop Up Balance\033[0;37;40m

  Enter amount in sats (100 - 100,000):
""")
    try:
        amount = int(input("  Amount: ").strip())
        if amount < 100 or amount > 100000:
            print("  Amount must be between 100 and 100,000 sats.")
            input("  Press Enter to continue...")
            return client.get_balance()
    except (ValueError, KeyboardInterrupt):
        return client.get_balance()

    try:
        result = client.topup(amount)
    except Exception as e:
        print(f"\n  Error creating invoice: {e}")
        input("  Press Enter to continue...")
        return client.get_balance()

    invoice = result["invoice"]
    payment_hash = result["payment_hash"]

    clear()
    blogo()
    print(f"\n  \033[1;37;40mLightning Invoice ({amount:,} sats)\033[0;37;40m\n")

    # QR code
    try:
        qr = qrcode.QRCode(box_size=1, border=1)
        qr.add_data(invoice.upper())
        print("\033[1;30;47m")
        qr.print_ascii()
        print("\033[0;37;40m")
    except Exception:
        pass

    print(f"  {invoice}\n")
    print("  Pay with any Lightning wallet. Waiting for payment...\n")

    # Poll for payment
    for i in range(200):  # ~10 min max
        time.sleep(3)
        try:
            if client.check_payment(payment_hash):
                new_balance = client.get_balance()
                print(
                    f"\n  \033[1;32;40mPayment received! "
                    f"New balance: {new_balance:,} sats\033[0;37;40m\n"
                )
                input("  Press Enter to continue...")
                return new_balance
        except Exception:
            pass
        sys.stdout.write(".")
        sys.stdout.flush()

    print("\n\n  Invoice expired. Try again.")
    input("  Press Enter to continue...")
    return client.get_balance()


def _show_usage(client):
    """Display usage statistics."""
    clear()
    blogo()
    try:
        stats = client.usage(30)
        print(f"""
  \033[1;37;40mUsage (last 30 days)\033[0;37;40m

    Queries:      {stats.get('total_queries', 0)}
    Sats spent:   {stats.get('total_sats', 0):,}
    Tokens in:    {stats.get('total_tokens_in', 0):,}
    Tokens out:   {stats.get('total_tokens_out', 0):,}
    Balance:      {stats.get('balance_sats', 0):,} sats
""")
    except Exception as e:
        print(f"\n  Error: {e}\n")

    input("  Press Enter to continue...")
