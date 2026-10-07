import pytest


def test_cto_portfolio(api_client):
    status, data = api_client.get("/api/cto/portfolio")
    assert status == 200
    assert "projects" in data


def test_cto_directives(api_client):
    status, data = api_client.get("/api/cto/directives")
    assert status == 200
    assert "directives" in data
    assert isinstance(data["directives"], list)


def test_cto_approvals(api_client):
    status, data = api_client.get("/api/cto/approvals")
    assert status == 200
    assert "approvals" in data


def test_cto_latest_directive(api_client):
    status, data = api_client.get("/api/cto/latest-directive")
    assert status == 200
    assert "directive" in data


def test_revenue_metrics(api_client):
    status, data = api_client.get("/api/revenue/metrics")
    assert status == 200
    assert "metrics" in data
    assert "projects" in data
    assert "live_projects" in data
    assert "recent_transactions" in data


def test_ollama_status(api_client):
    status, data = api_client.get("/api/ollama/status")
    assert status == 200
    assert isinstance(data, dict)
