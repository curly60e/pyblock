"""Tests for query classification."""

from __future__ import annotations

from oraclevision.addresses import AddressQueryError, classify_query, parse_address_query
from oraclevision.tx_service import parse_tx_query


def test_classify_txid() -> None:
    txid = "ab" * 32
    kind, value = classify_query(txid)
    assert kind == "txid"
    assert value == txid


def test_classify_address() -> None:
    addr = "bc1qtestaddressxxxxxxxxxxxxxxxxxxxxxx"
    kind, value = classify_query(addr)
    assert kind == "address"
    assert value == addr


def test_parse_tx_query_normalizes() -> None:
    txid = "AB" * 32
    assert parse_tx_query(txid) == txid.lower()


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