from app import app

def test_health():
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200

def test_hello():
    client = app.test_client()
    resp = client.get("/hello")
    assert resp.status_code == 200

def test_add():
    client = app.test_client()
    resp = client.get("/add")
    assert resp.status_code == 200

def test_health_content():
    client = app.test_client()
    resp = client.get("/health")
    assert resp.get_json()["status"] == "ok"

def test_hello_content():
    client = app.test_client()
    resp = client.get("/hello")
    assert "hello" in resp.get_json()["message"]
