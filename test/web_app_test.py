# test/web_app_test.py
import pytest
from web_app import create_app

@pytest.fixture(scope="module")
def test_client():
    app = create_app()
    app.config.update({"TESTING": True})
    return app.test_client()

def test_home(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"Welcome Home" in response.data

def test_about(test_client):
    response = test_client.get("/about")
    assert response.status_code == 200
    assert b"About Me" in response.data

def test_hello(test_client):
    response = test_client.get("/hello")
    assert response.status_code == 200
    assert b"Hello, World!" in response.data

    response = test_client.get("/hello?name=Hollie")
    assert b"Hello, Hollie!" in response.data

def test_rps(test_client):
    response = test_client.get("/rps/form")
    assert response.status_code == 200
    assert b"Rock, Paper, Scissors" in response.data

    response = test_client.post("/rps/play", data={"user_choice": "rock"})
    assert response.status_code == 200
    assert b"You chose: <strong>rock</strong>" in response.data

def test_stocks(test_client):
    response = test_client.get("/stocks/form")
    assert response.status_code == 200
    assert b"Stocks Form" in response.data

    response = test_client.get("/stocks/dashboard?symbol=IBM")
    assert response.status_code == 200
    assert b"Stocks Dashboard (IBM)" in response.data
    assert b"Latest Close" in response.data

    # a fake symbol should send the user back to the form (302 = redirect)
    response = test_client.get("/stocks/dashboard?symbol=OOPSIE")
    assert response.status_code == 302