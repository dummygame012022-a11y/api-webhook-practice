import csv

import pytest
from fastapi.testclient import TestClient

import webhook_fastapi
from webhook_fastapi import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def temp_csv(tmp_path, monkeypatch):
    path = tmp_path / "orders.csv"
    monkeypatch.setattr(webhook_fastapi, "CSV_PATH", path)
    return path


def test_valid_order_returns_ok():
    r = client.post("/webhook", json={"order": "A1", "item": "rice", "qty": 2})
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_order_is_written_to_csv(temp_csv):
    client.post("/webhook", json={"order": "A1", "item": "rice", "qty": 2})
    rows = list(csv.reader(temp_csv.open()))
    assert rows == [["A1", "rice", "2"]]


def test_missing_order_returns_422():
    r = client.post("/webhook", json={"item": "rice"})
    assert r.status_code == 422


def test_zero_qty_returns_422():
    r = client.post("/webhook", json={"order": "A1", "qty": 0})
    assert r.status_code == 422


def test_non_integer_qty_returns_422():
    r = client.post("/webhook", json={"order": "A1", "qty": "abc"})
    assert r.status_code == 422


def test_optional_fields_can_be_omitted(temp_csv):
    r = client.post("/webhook", json={"order": "A2"})
    assert r.status_code == 200
    assert list(csv.reader(temp_csv.open())) == [["A2", "", ""]]


def test_no_body_returns_422():
    r = client.post("/webhook")
    assert r.status_code == 422


def test_invalid_order_does_not_write_csv(temp_csv):
    client.post("/webhook", json={"item": "rice"})
    assert not temp_csv.exists()
