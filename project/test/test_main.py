import json


def test_create_song_invalid_json(test_app):
    response = test_app.post("/songs", data=json.dumps({"x": "y"}))
    assert response.status_code == 422

    response = test_app.post("/songs", data=json.dumps({"x": "y", "z": "a"}))
    assert response.status_code == 422

