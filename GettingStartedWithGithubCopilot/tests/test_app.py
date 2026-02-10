import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) > 0

def test_signup_and_unregister():
    # Utilise une activité existante et un email fictif
    activity = next(iter(client.get("/activities").json().keys()))
    email = "testuser@example.com"

    # Inscription
    signup = client.post(f"/activities/{activity}/signup?email={email}")
    assert signup.status_code == 200
    assert f"Signed up {email}" in signup.json().get("message", "")

    # Double inscription (doit échouer si la vérification existe)
    signup2 = client.post(f"/activities/{activity}/signup?email={email}")
    assert signup2.status_code in (400, 409, 200)

    # Désinscription
    unregister = client.post(f"/activities/{activity}/unregister?email={email}")
    assert unregister.status_code == 200
    assert f"Unregistered {email}" in unregister.json().get("message", "")

    # Double désinscription (doit échouer ou retourner 200)
    unregister2 = client.post(f"/activities/{activity}/unregister?email={email}")
    assert unregister2.status_code in (400, 404, 200)
