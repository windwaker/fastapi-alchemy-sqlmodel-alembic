import pytest
import requests


@pytest.mark.integration_test
def test_create_song_invalid_json_it():
    response = requests.post("http://localhost:8000/songs", data=json.dumps({"x": "y"}))
    assert response.status_code == 422