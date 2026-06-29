from fastapi.testclient import TestClient

from src.app import app, activities


def test_unregister_participant_removes_email():
    # Arrange
    activities["Chess Club"]["participants"] = ["michael@mergington.edu", "daniel@mergington.edu"]
    client = TestClient(app)

    # Act
    response = client.delete("/activities/Chess Club/participants/michael@mergington.edu")

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == "Removed michael@mergington.edu from Chess Club"
    assert "michael@mergington.edu" not in activities["Chess Club"]["participants"]
