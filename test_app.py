from app import app

# test home page for flask server.
def test_home_page():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"Role" in response.data
    assert b"Context" in response.data
    assert b"Style" in response.data
    assert b"Task" in response.data
    assert b"Constraints" in response.data
    assert b"Submit" in response.data