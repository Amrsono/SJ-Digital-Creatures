import pytest


def test_auth_status(unauthenticated_api_client):
    status, data = unauthenticated_api_client.get("/api/auth/status")
    assert status == 200
    assert "authenticated" in data
    assert "auth_enabled" in data


def test_login_failure(unauthenticated_api_client):
    status, data = unauthenticated_api_client.post("/api/auth/login", {
        "username": "Moeen",
        "password": "wrong_password"
    })
    assert status == 401
    assert data.get("ok") is False
    assert "Invalid" in data.get("error", "")


def test_login_success(unauthenticated_api_client):
    status, data = unauthenticated_api_client.post("/api/auth/login", {
        "username": "Moeen",
        "password": "Password@26"
    })
    assert status == 200
    assert data.get("ok") is True
    assert "token" in data
    assert data.get("user") == "moeen"


def test_logout(api_client):
    logout_status, logout_data = api_client.post("/api/auth/logout", {})
    assert logout_status == 200
    assert logout_data.get("ok") is True
