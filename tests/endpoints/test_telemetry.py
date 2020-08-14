import random
import string
from typing import Dict

from starlette.testclient import TestClient

from main import app
from tests.utils.randomString import random_lower_string

client = TestClient(app)


def test_create_telemetry():
    # Creates a track so tests dont give a FK error on inserting round
    track_response = client.post(
        "/api/track/", json={"name": random_lower_string(), "description": random_lower_string()})
    track_id = track_response.json()["id"]

    car_response = client.post("/api/car/", json={"name": random_lower_string(
    ), "description": random_lower_string(), "creation_date": "2020-06-02"})
    car_id = car_response.json()["id"]

    round_response = client.post("/api/round/", json={"name": random_lower_string(),
                                                      "description": random_lower_string(),
                                                      "reason": "Test",
                                                      "track_id": track_id,
                                                      "car_id": car_id})
    round_id = round_response.json()['id']

    data = {
        "speed": 0.0,
        "distance": 0.0,
        "engine_temp": 10.0,
        "creation_time": "2020-07-26T18:14:17.378000",
        "energy_cons": 10,
        "rpm": 0,
        "battery": 0,
        "round_id": round_id

    }
    response = client.post("/api/telemetry/", json=data)
    assert response.status_code == 200
    content = response.json()
    assert content["speed"] == data["speed"]
    assert content["distance"] == data["distance"]
    assert content["engine_temp"] == data["engine_temp"]
    assert content["creation_time"] == data["creation_time"]
    assert content["energy_cons"] == data["energy_cons"]
    assert content["rpm"] == data["rpm"]
    assert content["battery"] == data["battery"]
    assert content["round_id"] == data["round_id"]
    assert "id" in content


# def test_create_duplicate_telemetry():
#     track_response = client.post("/api/track/", json={"name": random_lower_string(), "description": random_lower_string()})
#     track_id = track_response.json()["id"]

#     car_response=client.post("/api/car/", json={ "name": random_lower_string(), "description":random_lower_string(), "creation_date": "2020-06-02"})
#     car_id=car_response.json()["id"]

#     # Creates a round so tests dont give a FK error on inserting round
#     round_response = client.post("/api/round/", json={
#     "name": random_lower_string(),
#     "description": random_lower_string(),
#     "reason": "Test",
#     "ref_date": "2020-07-26",
#     "track_id": track_id,
#     "car_id": car_id
#     })
#     round_id = round_response.json()["id"]
#     data = {
#             "speed": 0,
#             "distance": 0,
#             "engine_temp": 0,
#             "creation_time": "2020-07-26T18:14:17.378Z",
#             "energy_cons": 0,
#             "rpm": 0,
#             "battery": 0,
#             "round_id": round_id
#             }

#     first_response = client.post("/api/telemetry/", json=data)
#     assert first_response.status_code == 200
#     second_response = client.post("/api/telemetry/", json=data)
#     assert second_response.status_code == 303


def test_read_telemetry_by_id():
    track_response = client.post(
        "/api/track/", json={"name": random_lower_string(), "description": random_lower_string()})
    track_id = track_response.json()["id"]

    car_response = client.post("/api/car/", json={"name": random_lower_string(
    ), "description": random_lower_string(), "creation_date": "2020-06-02"})
    car_id = car_response.json()["id"]

    # Creates a round so tests dont give a FK error on inserting round
    round_response = client.post("/api/round/", json={
        "name": random_lower_string(),
        "description": random_lower_string(),
        "reason": "Test",
        "ref_date": "2020-07-26",
        "track_id": track_id,
        "car_id": car_id
    })
    round_id = round_response.json()["id"]

    insert_data = {
        "speed": 0,
        "distance": 0,
        "engine_temp": 0,
        "creation_time": "2020-07-26T18:14:17.378000",
        "energy_cons": 0,
        "rpm": 0,
        "battery": 0,
        "round_id": round_id
    }
    telemetry_response = client.post("/api/telemetry/", json=insert_data)

    assert telemetry_response.status_code == 200
    read_id = telemetry_response.json()["id"]

    read_response = client.get(f"/api/telemetry/{read_id}")
    response_data = read_response.json()
    assert read_response.status_code == 200
    assert insert_data["speed"] == response_data["speed"]
    assert insert_data["distance"] == response_data["distance"]
    assert insert_data["engine_temp"] == response_data["engine_temp"]
    assert insert_data["creation_time"] == response_data["creation_time"]
    assert insert_data["energy_cons"] == response_data["energy_cons"]
    assert insert_data["rpm"] == response_data["rpm"]
    assert insert_data["battery"] == response_data["battery"]
    assert insert_data["round_id"] == response_data["round_id"]


def test_read_telemetry():
    read_response = client.get(f"/api/telemetry/")
    assert read_response.status_code == 200
    assert type(read_response.json()) == list


def test_read_invalid_telemetry():

    update_response = client.get(f"/api/telemetry/{0}")
    assert update_response.status_code == 404


def test_read_invalid_telemetry_two():
    update_response = client.get(f"/api/telemetryy/", headers={"id": "0"})
    assert update_response.status_code == 404


def test_delete_telemetry():
    read_response = client.get(f"/api/telemetry/")
    id_list = [id["id"] for id in read_response.json()]
    for id_remove in id_list:
        delete_response = client.delete(f"/api/telemetry/{id_remove}")
        assert delete_response.status_code == 200
        assert delete_response.json()["id"] == id_remove


def test_delete_invalid_telemetry():
    delete_response = client.delete(f"/api/telemetry/{0}")
    assert delete_response.status_code == 303
