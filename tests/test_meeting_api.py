import pytest


def test_meeting_data_get(api_client):
    status, data = api_client.get("/api/meeting/data?tab=planning&agenda=standup")
    assert status == 200
    assert isinstance(data, dict)


def test_meeting_minutes_get(api_client):
    status, data = api_client.get("/api/meeting/minutes")
    assert status == 200
    assert data.get("ok") is True
    assert "minutes" in data


def test_meeting_session_get(api_client):
    status, data = api_client.get("/api/meeting/session")
    assert status == 200
    assert data.get("ok") is True
    assert "session" in data


def test_meeting_convene_post(api_client):
    payload = {
        "tab": "planning",
        "project": "SJ Incubator",
        "initiator": "sono",
        "agenda": "standup"
    }
    status, data = api_client.post("/api/meeting/convene", payload)
    assert status == 200
    assert data.get("ok") is True
    assert "meeting" in data


def test_meeting_interject_post(api_client):
    payload = {
        "speaker": "Sono (CTO)",
        "message": "Let's align on next steps for performance optimization.",
        "project": "SJ Incubator"
    }
    status, data = api_client.post("/api/meeting/interject", payload)
    assert status == 200
    assert data.get("ok") is True
    assert "type" in data


def test_meeting_minutes_post(api_client):
    status, data = api_client.post("/api/meeting/minutes", {})
    assert status == 200
    assert data.get("ok") is True
    assert "minutes" in data


def test_meeting_clear_post(api_client):
    status, data = api_client.post("/api/meeting/clear", {})
    assert status == 200
    assert data.get("ok") is True
    assert data.get("message") == "Meeting session cleared"
