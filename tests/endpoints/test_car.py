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

def test_update_car():
    insert_data = {"name": "Teste",
                    "description":"Teste", 
                    "creation_date": "2020-06-04"}

    insert_response = client.post("/api/car/", json=insert_data)
    update_id = insert_response.json()["id"]
    assert insert_response.status_code == 200
    update_data = {
        "name": "Teste updated",
        "description": "Description updated",
        "creation_date": "2020-06-05"
        }
    update_response = client.put(f"/api/car/{update_id}", json=update_data)
    assert update_response.status_code == 200
    assert update_response.json()["name"] == update_data["name"]
    assert update_response.json()["description"] == update_data["description"]
    assert update_response.json()["creation_date"] == update_data["creation_date"]
    

    
def test_delete_car():
    read_response = client.get(f"/api/car/")
    name_list = [name["name"] for name in read_response.json()]
    for name_remove in name_list:
        delete_response = client.delete(f"/api/car/{name_remove}")
        assert delete_response.status_code == 200
        assert delete_response.json()["name"] ==name_remove

