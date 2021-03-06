from starlette.testclient import TestClient

from main import app
from tests.utils.randomString import random_lower_string

client = TestClient(app)


# Creates a track so tests dont give a FK error on inserting round

# track_response = client.post("/api/track/", json={"name": "Test", "description": "Test"})
# track_id = track_response.json()["id"]


def test_create_round():
    car_response = client.post("/api/car/", json={"name": random_lower_string(
    ), "description": random_lower_string(), "creation_date": "2020-06-02"})
    car_id = car_response.json()["id"]

    track_response = client.post(
        "/api/track/", json={"name": random_lower_string(), "description": random_lower_string()})
    track_id = track_response.json()["id"]

    data = {"name": random_lower_string(),
            "description": random_lower_string(),
            "reason": "Test",
            "track_id": track_id,
            "car_id": car_id}
    response = client.post("/api/round/", json=data)
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert content["reason"] == data["reason"]
    assert content["track_id"] == data["track_id"]
    assert content["car_id"] == data["car_id"]
    assert "id" in content


def test_create_duplicate_round():
    car_response = client.post("/api/car/", json={"name": random_lower_string(
    ), "description": random_lower_string(), "creation_date": "2020-06-02"})
    car_id = car_response.json()["id"]

    track_response = client.post(
        "/api/track/", json={"name": random_lower_string(), "description": random_lower_string()})
    track_id = track_response.json()["id"]

    data = {"name": random_lower_string(),
            "description": random_lower_string(),
            "reason": "Test",
            "track_id": track_id,
            "car_id": car_id}

    first_response = client.post("/api/round/", json=data)
    assert first_response.status_code == 200
    second_response = client.post("/api/round/", json=data)
    assert second_response.status_code == 303


def test_update_round():
    car_response = client.post("/api/car/", json={"name": random_lower_string(
    ), "description": random_lower_string(), "creation_date": "2020-06-02"})
    car_id = car_response.json()["id"]

    track_response = client.post(
        "/api/track/", json={"name": random_lower_string(), "description": random_lower_string()})
    track_id = track_response.json()["id"]

    insert_data = {"name": random_lower_string(),
                   "description": random_lower_string(),
                   "reason": "Test",
                   "track_id": track_id,
                   "car_id": car_id}

    insert_response = client.post("/api/round/", json=insert_data)
    assert insert_response.status_code == 200
    update_id = insert_response.json()["id"]

    update_data = {
        "description": random_lower_string(),
        "ref_date": "2020-10-20"
    }

    update_response = client.put(f"/api/round/{update_id}", json=update_data)
    assert update_response.status_code == 200


def test_update_invalid_round():
    update_data = {
        "description": random_lower_string(),
        "ref_date": "2020-10-20"
    }

    update_response = client.put(f"/api/round/{0}", json=update_data)
    assert update_response.status_code == 303


def test_read_round():
    car_response = client.post("/api/car/", json={"name": random_lower_string(
    ), "description": random_lower_string(), "creation_date": "2020-06-02"})
    car_id = car_response.json()["id"]

    track_response = client.post(
        "/api/track/", json={"name": random_lower_string(), "description": random_lower_string()})
    track_id = track_response.json()["id"]

    insert_data = {"name": random_lower_string(),
                   "description": random_lower_string(),
                   "reason": "Test",
                   "track_id": track_id,
                   "car_id": car_id}

    insert_response = client.post("/api/round/", json=insert_data)
    assert insert_response.status_code == 200
    read_id = insert_response.json()["id"]

    read_response = client.get(f"/api/round/{read_id}")
    response_data = insert_response.json()
    assert read_response.status_code == 200
    assert insert_data["name"] == response_data["name"]
    assert insert_data["reason"] == response_data["reason"]
    assert insert_data["track_id"] == response_data["track_id"]
    assert insert_data["car_id"] == response_data["car_id"]


def test_read_invalid_round():
    update_response = client.get(f"/api/round/{0}")
    assert update_response.status_code == 404


def test_read_rounds():
    read_response = client.get(f'{"/api/round/"}')
    assert read_response.status_code == 200
    assert type(read_response.json()) == list


def test_delete_round():
    car_response = client.post("/api/car/", json={"name": random_lower_string(
    ), "description": random_lower_string(), "creation_date": "2020-06-02"})
    car_id = car_response.json()["id"]

    track_response = client.post(
        "/api/track/", json={"name": random_lower_string(), "description": random_lower_string()})
    track_id = track_response.json()["id"]

    data = {"name": random_lower_string(),
            "description": random_lower_string(),
            "reason": "Test",
            "track_id": track_id,
            "car_id": car_id}
    response = client.post("/api/round/", json=data)
    round_id = response.json()["id"]

    delete_response = client.delete(f"/api/round/{round_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["id"] == round_id


def test_delete_invalid_round():
    delete_response = client.delete(f"/api/round/{1}")
    assert delete_response.status_code == 303
