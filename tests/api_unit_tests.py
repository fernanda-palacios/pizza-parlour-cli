from API import app

def test_pizza():
    response = app.test_client().get('/menu')

    assert response.status_code == 200
    # assert response.data == b'Welcome to Pizza Planet!'
