# Import the resource/controllers we're testing
from resources.book import *

def test_get_book(client):
    response = client.get("/books/1")
    assert response.status_code == 200
    assert response.json == {
        "id": 1, 
        "title": "Python for Dummies"
    }
