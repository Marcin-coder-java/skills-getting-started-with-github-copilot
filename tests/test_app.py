from fastapi.testclient import TestClient

from src.app import app, activities


def test_unregister_participant_removes_email():
    activities["Chess Club"]["participants"] = ["michael@mergington.edu", "daniel@mergington.edu"]

    with TestClient(app) as client:
        response = client.delete("/activities/Chess Club/participants/michael@mergington.edu")

    assert response.status_code == 200
    assert response.json()["message"] == "Removed michael@mergington.edu from Chess Club"
    assert "michael@mergington.edu" not in activities["Chess Club"]["participants"]
