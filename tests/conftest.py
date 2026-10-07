import os
import sys
import socket
import socketserver
import threading
import urllib.request
import json
import pytest

# Add parent directory to sys.path so server can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from server import IncubatorHandler


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True


@pytest.fixture(scope="session")
def server_url():
    """Starts an in-memory HTTP server on an ephemeral port for testing."""
    server = ThreadedTCPServer(("127.0.0.1", 0), IncubatorHandler)
    ip, port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    server_thread.start()
    
    url = f"http://127.0.0.1:{port}"
    yield url
    
    server.shutdown()
    server.server_close()


class TestApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        req = urllib.request.Request(url, method="GET")
        with urllib.request.urlopen(req) as response:
            status = response.status
            body = response.read().decode("utf-8")
            try:
                data = json.loads(body)
            except Exception:
                data = body
            return status, data

    def post(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        payload = json.dumps(data if data is not None else {}).encode("utf-8")
        req = urllib.request.Request(
            url,
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        try:
            with urllib.request.urlopen(req) as response:
                status = response.status
                body = response.read().decode("utf-8")
                try:
                    res_data = json.loads(body)
                except Exception:
                    res_data = body
                return status, res_data
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8")
            try:
                res_data = json.loads(body)
            except Exception:
                res_data = body
            return e.code, res_data


@pytest.fixture
def api_client(server_url):
    """Provides a TestApiClient instance configured with the test server URL."""
    return TestApiClient(server_url)
