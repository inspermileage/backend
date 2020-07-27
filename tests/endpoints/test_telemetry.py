from starlette.testclient import TestClient

from main import app

client = TestClient(app)



def test_create_telemetry():
    # Creates a track so tests dont give a FK error on inserting round
    track_response = client.post("/api/track/", json={"name": "teste track", "description": "Test track"})
    track_id = track_response.json()["id"]

    car_response=client.post("/api/car/", json={ "name": "Teste car", "description":"Teste car", "creation_date": "2020-06-02"})
    car_id=car_response.json()["id"]

    # Creates a round so tests dont give a FK error on inserting round
    round_response = client.post("/api/round/", json={
    "name": "string123",
    "description": "string4563",
    "reason": "Test",
    "ref_date": "2020-07-26",
    "track_id": track_id,
    "car_id": car_id
    })
    round_id = track_response.json()["id"]


    data = {
            "speed": 0,
            "distance": 0,
            "engine_temp": 0,
            "creation_time": "2020-07-26T18:14:17.37890",
            "energy_cons": 0,
            "rpm": 0,
            "battery": 0,
            "round_id": round_id
            }

    telemetry_response=client.post("/api/telemetry/", json=data)
    telemetry_id =telemetry_response.json()["id"]

    assert telemetry_response.status_code == 200
    content = telemetry_response.json()
    assert content["speed"] == data["speed"]
    assert content["distance"] == data["distance"]
    assert content["engine_temp"] == data["engine_temp"]
    assert content["creation_time"] == data["creation_time"]
    assert content["energy_cons"] == data["energy_cons"]
    assert content["rpm"] == data["rpm"]
    assert content["battery"] == data["battery"]
    assert content["round_id"] == data["round_id"]
    assert "id" in content

def test_create_duplicate_telemetry():
    track_response = client.post("/api/track/", json={"name": "Test1283", "description": "Test4uu3"})
    track_id = track_response.json()["id"]

    car_response=client.post("/api/car/", json={ "name": "Teste12344", "description":"Test4322e", "creation_date": "2020-06-02"})
    car_id=car_response.json()["id"]

    # Creates a round so tests dont give a FK error on inserting round
    round_response = client.post("/api/round/", json={
    "name": "string3444",
    "description": "string44322",
    "reason": "Test",
    "ref_date": "2020-07-26",
    "track_id": track_id,
    "car_id": car_id
    })
    round_id = track_response.json()["id"]
    data = {
            "speed": 0,
            "distance": 0,
            "engine_temp": 0,
            "creation_time": "2020-07-26T18:14:17.378Z",
            "energy_cons": 0,
            "rpm": 0,
            "battery": 0,
            "round_id": round_id
            }

    first_response = client.post("/api/telemetry/", json=data)
    assert first_response.status_code == 200
    second_response = client.post("/api/telemetry/", json=data)
    assert second_response.status_code == 303

def test_read_telemetry_by_id():
    track_response = client.post("/api/track/", json={"name": "Test3333", "description": "Test232e"})
    track_id = track_response.json()["id"]

    car_response=client.post("/api/car/", json={ "name": "Testeewdd", "description":"Testeefef", "creation_date": "2020-06-02"})
    car_id=car_response.json()["id"]

    # Creates a round so tests dont give a FK error on inserting round
    round_response = client.post("/api/round/", json={
    "name": "string33",
    "description": "st3ee3ering",
    "reason": "Test",
    "ref_date": "2020-07-26",
    "track_id": track_id,
    "car_id": car_id
    })
    round_id = track_response.json()["id"]

    insert_data = {
            "speed": 0,
            "distance": 0,
            "engine_temp": 0,
            "creation_time": "2020-07-26T18:14:17.378Z",
            "energy_cons": 0,
            "rpm": 0,
            "battery": 0,
            "round_id": round_id
            }
    telemetry_response=client.post("/api/telemetry/", json=insert_data)

    assert car_response.status_code == 200
    read_id = telemetry_response.json()["id"]


    read_response = client.get(f"/api/telemetry/{read_id}")
    response_data = telemetry_response.json()
    assert read_response.status_code == 200
    assert insert_data["speed"] == data["speed"]
    assert insert_data["distance"] == data["distance"]
    assert insert_data["engine_temp"] == data["engine_temp"]
    assert insert_data["creation_time"] == data["creation_time"]
    assert insert_data["energy_cons"] == data["energy_cons"]
    assert insert_data["rpm"] == data["rpm"]
    assert insert_data["battery"] == data["battery"]
    assert insert_data["round_id"] == data["round_id"]

def test_read_telemetry():
    read_response = client.get(f"/api/telemetry/")
    assert read_response.status_code == 200
    assert type(read_response.json()) == list

def test_read_invalid_telemetry():
    update_response = client.get(f"/api/telemetry/{0}")
    assert update_response.status_code == 404

def test_read_invalid_telemetry_two():
    update_response = client.get(f"/api/telemetryy/", headers={"id": 0})
    assert update_response.status_code == 404


def test_delete_telemetry():
    read_response = client.get(f"/api/telemetry/")
    id_list = [id["id"] for id in read_response.json()]
    for id_remove in id_list:
        delete_response = client.delete(f"/api/telemetry/{id_remove}")
        assert delete_response.status_code == 200
        assert delete_response.json()["id"] ==id_remove

def test_delete_invalid_telemetry():
    delete_response = client.delete(f"/api/telemetry/{0}")
    assert delete_response.status_code == 303
