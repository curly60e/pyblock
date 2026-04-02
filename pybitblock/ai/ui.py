"""Terminal UI for PyBLOCK AI Assistant."""

import sys
import time

import qrcode
import requests
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.text import Text

from shared.display import clear
from pblogo import blogo

from .client import AstrolexisClient
from .context import gather_node_context

_console = Console()

# Colors
G = "\033[1;32;40m"   # green
C = "\033[1;36;40m"   # cyan
Y = "\033[1;33;40m"   # yellow
R = "\033[1;31;40m"   # red
W = "\033[1;37;40m"   # white bold
D = "\033[0;37;40m"   # dim/default
DIM = "\033[2m"


def ai_menu(path, lndconnectload=None):
    """Main AI assistant menu. Requires Astrolexis token in config."""
    from config import cfg

    token = cfg.settings.get("astrolexis_token", "")
    if not token:
        token = _setup_token(cfg)
        if not token:
            return

    client = AstrolexisClient(token)

    try:
        info = client.verify()
    except Exception as e:
        clear()
        blogo()
        print(f"\n  {R}Error connecting to Astrolexis:{D} {e}")
        print(f"  Check your token in Settings.\n")
        input("  Press Enter to return...")
        return

    _chat_loop(client, path, lndconnectload, info["balance_sats"])


def _setup_token(cfg):
    """First-time token setup."""
    clear()
    blogo()
    print(f"""
  {W}AI Assistant Setup{D}

  Powered by {C}Astrolexis KCode{D}

  To use the AI Assistant, you need an Astrolexis token.
  Get yours at: {Y}https://astrolexis.space/pyblock{D}

  Enter your token below, or press Enter to cancel.
""")
    token = input("  Token: ").strip()
    if not token:
        return None

    if not token.startswith("astrolexis_"):
        print(f"\n  {R}Invalid token format.{D} Must start with 'astrolexis_'")
        input("  Press Enter to return...")
        return None

    settings = cfg.settings
    settings["astrolexis_token"] = token
    cfg.save("pyblocksettings.conf", settings)
    print(f"\n  {G}Token saved.{D}")
    time.sleep(1)
    return token


def _render_response(text):
    """Render AI response using Rich Markdown for proper formatting."""
    _console.print()
    _console.print(Markdown(text), width=min(80, _console.width - 4))
    _console.print()


def _status_line(balance):
    """Compact status line."""
    return (
        f"  {C}AI Assistant{D} | "
        f"Balance: {G}{balance:,}{D} sats | "
        f"{DIM}T{D}=topup {DIM}U{D}=usage {DIM}C{D}=clear {DIM}Q{D}=quit"
    )


def _chat_loop(client, path, lndconnectload, balance):
    """Continuous chat loop — no screen clearing between messages."""
    conversation = []
    context = None

    clear()
    blogo()
    print(f"""
  {W}AI Assistant{D}
  Powered by {C}Astrolexis KCode{D}
  Balance: {G}{balance:,}{D} sats

  {DIM}Ask anything about your Bitcoin/Lightning node.
  Commands: T=topup  U=usage  C=clear  Q=quit{D}
""")

    # Gather context once at start, refresh on new blocks
    try:
        context = gather_node_context(path, lndconnectload)
    except Exception:
        context = {}

    while True:
        try:
            # Prompt
            user_input = input(f"  {G}>{D} ").strip()
            if not user_input:
                continue

            upper = user_input.upper()
            if upper == "Q":
                break
            if upper == "T":
                balance = _topup_flow(client)
                # Redraw header after topup
                clear()
                blogo()
                print(f"\n{_status_line(balance)}\n")
                continue
            if upper == "U":
                _show_usage(client)
                try:
                    balance = client.get_balance()
                except Exception:
                    pass
                print(f"\n{_status_line(balance)}\n")
                continue
            if upper == "C":
                conversation = []
                clear()
                blogo()
                print(f"\n  {DIM}Conversation cleared.{D}\n")
                print(f"{_status_line(balance)}\n")
                continue

            # Add to conversation
            conversation.append({"role": "user", "content": user_input})

            # Refresh context periodically
            try:
                context = gather_node_context(path, lndconnectload)
            except Exception:
                pass

            # Stream response
            print()
            full_response = ""
            try:
                for chunk in client.chat(
                    conversation, node_context=context
                ):
                    if chunk.get("type") == "content_block_delta":
                        text = chunk.get("delta", {}).get("text", "")
                        full_response += text

                _render_response(full_response)

                # Add to conversation history
                conversation.append({
                    "role": "assistant", "content": full_response
                })

                # Update balance
                try:
                    balance = client.get_balance()
                except Exception:
                    pass

                # Show cost inline
                print(f"\n  {DIM}Balance: {balance:,} sats{D}\n")

            except requests.exceptions.HTTPError as e:
                if e.response is not None and e.response.status_code == 402:
                    data = e.response.json()
                    bal = data.get('balance_sats', 0)
                    cost = data.get('estimated_cost', '?')
                    print(
                        f"  {R}Insufficient balance{D} "
                        f"({bal} sats, need ~{cost})."
                    )
                    print(f"  Press {Y}T{D} to top up.\n")
                    conversation.pop()
                else:
                    print(f"  {R}Error:{D} {e}\n")
                    conversation.pop()

            except Exception as e:
                print(f"  {R}Error:{D} {e}\n")
                if conversation and conversation[-1]["role"] == "user":
                    conversation.pop()

        except KeyboardInterrupt:
            print(f"\n\n  {DIM}Ctrl+C — back to main menu{D}\n")
            break
        except EOFError:
            break


def _topup_flow(client):
    """Lightning top-up flow. Returns new balance."""
    clear()
    blogo()
    print(f"""
  {W}Top Up Balance{D}

  Enter amount in sats (100 - 100,000):
""")
    try:
        amount = int(input("  Amount: ").strip())
        if amount < 100 or amount > 100000:
            print(f"  {R}Amount must be between 100 and 100,000 sats.{D}")
            input("  Press Enter to return...")
            return client.get_balance()
    except (ValueError, KeyboardInterrupt):
        return client.get_balance()

    try:
        result = client.topup(amount)
    except Exception as e:
        print(f"\n  {R}Error creating invoice:{D} {e}")
        input("  Press Enter to return...")
        return client.get_balance()

    invoice = result["invoice"]
    payment_hash = result["payment_hash"]

    clear()
    blogo()
    print(f"\n  {W}Lightning Invoice ({amount:,} sats){D}\n")

    # QR code
    try:
        qr = qrcode.QRCode(box_size=1, border=1)
        qr.add_data(invoice.upper())
        print("\033[1;30;47m")
        qr.print_ascii()
        print(D)
    except Exception:
        pass

    print(f"  {invoice}\n")
    print(f"  Pay with any Lightning wallet. Waiting for payment...\n")

    # Poll for payment
    for _ in range(200):  # ~10 min max
        time.sleep(3)
        try:
            if client.check_payment(payment_hash):
                new_balance = client.get_balance()
                print(
                    f"\n  {G}Payment received! "
                    f"New balance: {new_balance:,} sats{D}\n"
                )
                time.sleep(2)
                return new_balance
        except Exception:
            pass
        sys.stdout.write(".")
        sys.stdout.flush()

    print(f"\n\n  {R}Invoice expired.{D} Try again.")
    time.sleep(2)
    return client.get_balance()


def _show_usage(client):
    """Display usage statistics inline."""
    try:
        stats = client.usage(30)
        print(f"""
  {W}Usage (last 30 days){D}
    Queries:      {stats.get('total_queries', 0)}
    Sats spent:   {stats.get('total_sats', 0):,}
    Tokens in:    {stats.get('total_tokens_in', 0):,}
    Tokens out:   {stats.get('total_tokens_out', 0):,}
    Balance:      {G}{stats.get('balance_sats', 0):,}{D} sats
""")
    except Exception as e:
        print(f"\n  {R}Error:{D} {e}\n")
