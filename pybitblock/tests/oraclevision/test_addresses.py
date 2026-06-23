"""Tests for query classification."""

from __future__ import annotations

from oraclevision.addresses import (
    AddressQueryError,
    classify_query,
    is_txid_query,
    parse_address_query,
    script_type_from_validation,
)
from oraclevision.tx_service import parse_tx_query


def test_classify_txid() -> None:
    txid = "ab" * 32
    kind, value = classify_query(txid)
    assert kind == "txid"
    assert value == txid


def test_classify_address_bech32() -> None:
    addr = "bc1qtestaddressxxxxxxxxxxxxxxxxxxxxxx"
    kind, value = classify_query(addr)
    assert kind == "address"
    assert value == addr


def test_parse_address_query_p2pkh() -> None:
    addr = "1BoatSLRHtKNngkdXEeobR76b53LETtpyT"
    assert parse_address_query(addr) == addr


def test_parse_address_query_p2sh() -> None:
    addr = "3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy"
    assert parse_address_query(addr) == addr


def test_parse_tx_query_normalizes() -> None:
    txid = "AB" * 32
    assert parse_tx_query(txid) == txid.lower()


def test_is_txid_query() -> None:
    valid = "ab" * 32
    assert is_txid_query(valid) is True
    assert is_txid_query("ab" * 31) is False


def test_classify_query_empty_raises() -> None:
    try:
        classify_query("")
        raise AssertionError("expected ValueError")
    except ValueError:
        pass


def test_invalid_query_raises() -> None:
    try:
        classify_query("not-a-txid")
        raise AssertionError("expected AddressQueryError")
    except AddressQueryError:
        pass


def test_invalid_address_raises() -> None:
    try:
        parse_address_query("invalid-address")
        raise AssertionError("expected AddressQueryError")
    except AddressQueryError:
        pass


def test_script_type_from_validation_witness_v0() -> None:
    result = script_type_from_validation({
        "isvalid": True,
        "iswitness": True,
        "witness_version": 0,
        "scriptPubKey": "0014abcd",
    })
    assert result == "witness_v0_keyhash"


def test_script_type_from_validation_taproot() -> None:
    result = script_type_from_validation({
        "isvalid": True,
        "iswitness": True,
        "witness_version": 1,
        "scriptPubKey": "5120abcd",
    })
    assert result == "witness_v1_taproot"
