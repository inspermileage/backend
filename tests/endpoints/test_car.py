from starlette.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_car_by_name():
    insert_data = { "name": "Teste",
                    "description":"Teste", 
                    "creation_date": "2020-06-02"}
    car_response=client.post("/api/car/", json=insert_data)

    assert car_response.status_code == 200
    read_name = car_response.json()["name"]

    read_response = client.get(f"/api/car/{read_name}")
    response_data = car_response.json()
    assert read_response.status_code == 200
    assert insert_data["description"] == response_data["description"]
    assert insert_data["creation_date"] == response_data["creation_date"]

def test_read_car():
    read_response = client.get(f"/api/car/")
    assert read_response.status_code == 200
    assert type(read_response.json()) == list
    
def test_delete_car():
    read_response = client.get(f"/api/car/")
    name_list = [name["name"] for name in read_response.json()]
    for name_remove in name_list:
        delete_response = client.delete(f"/api/car/{name_remove}")
        assert delete_response.status_code == 200
        assert delete_response.json()["name"] ==name_remove

