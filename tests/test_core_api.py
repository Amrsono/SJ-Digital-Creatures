import pytest


def test_get_current_project(api_client):
    status, data = api_client.get("/api/project/current")
    assert status == 200
    assert isinstance(data, dict)


def test_get_recent_projects(api_client):
    status, data = api_client.get("/api/projects/recent")
    assert status == 200
    assert "recents" in data
    assert isinstance(data["recents"], list)


def test_get_company_status(api_client):
    status, data = api_client.get("/api/company/status")
    assert status == 200
    assert "paused" in data
    assert isinstance(data["paused"], bool)


def test_detect_projects(api_client):
    status, data = api_client.get("/api/projects/detect")
    assert status == 200
    assert "candidates" in data
    assert isinstance(data["candidates"], list)


def test_portfolio_excluded(api_client):
    status, data = api_client.get("/api/portfolio/excluded")
    assert status == 200
    assert "excluded" in data
    assert isinstance(data["excluded"], list)


def test_portfolio_state(api_client):
    status, data = api_client.get("/api/portfolio/state")
    assert status == 200
    assert "tenants" in data
    assert "count" in data
    assert isinstance(data["tenants"], list)


def test_engine_status(api_client):
    status, data = api_client.get("/api/engine/status")
    assert status == 200
    assert isinstance(data, dict)


def test_agent_actions_live(api_client):
    status, data = api_client.get("/api/agent/actions/live")
    assert status == 200
    assert isinstance(data, dict)
