import random
import string
from typing import Dict

from starlette.testclient import TestClient

from main import app
from tests.utils.randomString import random_lower_string

client = TestClient(app)


def test_create_car():

    data = {"name": random_lower_string(),
            "description": random_lower_string(),
            "creation_date":  "2020-06-04"
            }

    car_response = client.post("/api/car/", json=data)
   # car_id =car_response.json()["id"]

    assert car_response.status_code == 200
    content = car_response.json()
    assert content["name"] == data["name"]
    assert content["description"] == data["description"]
    assert content["creation_date"] == data["creation_date"]
    assert "id" in content


def test_create_duplicate_car():

    data = {"name": random_lower_string(),
            "description": random_lower_string(),
            "creation_date":  "2020-06-04"
            }

    first_response = client.post("/api/car/", json=data)
    assert first_response.status_code == 200
    second_response = client.post("/api/car/", json=data)
    assert second_response.status_code == 303


def test_read_car_by_name():
    insert_data = {"name": random_lower_string(),
                   "description": random_lower_string(),
                   "creation_date": "2020-06-02"}
    car_response = client.post("/api/car/", json=insert_data)

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


def test_read_invalid_car():
    update_response = client.get(f"/api/car/{0}")
    assert update_response.status_code == 404


def test_read_invalid_car_two():
    update_response = client.get(f"/api/carr/", headers={"name": "car"})
    assert update_response.status_code == 404


def test_update_car():
    insert_data = {"name": random_lower_string(),
                   "description": random_lower_string(),
                   "creation_date": "2020-06-04"}

    insert_response = client.post("/api/car/", json=insert_data)
    update_id = insert_response.json()["id"]
    assert insert_response.status_code == 200
    update_data = {
        "name":  random_lower_string(),
        "description":  random_lower_string(),
        "creation_date": "2020-06-05"
    }
    update_response = client.put(f"/api/car/{update_id}", json=update_data)
    assert update_response.status_code == 200
    assert update_response.json()["name"] == update_data["name"]


def test_update_invalid_car():
    update_data = {
        "name": random_lower_string(),
        "description": random_lower_string(),
        "creation_date": "2020-06-05"
    }

    update_response = client.put(f"/api/car/{0}", json=update_data)
    assert update_response.status_code == 404


def test_delete_car():

    data = {"name": random_lower_string(),
            "description": random_lower_string(),
            "creation_date":  "2020-06-04"
            }

    car_response = client.post("/api/car/", json=data)
    car_name = car_response.json()["name"]
    #read_response = client.get(f"/api/car/{car_name}")

    delete_response = client.delete(f"/api/car/{car_name}")
    assert delete_response.status_code == 200
    assert delete_response.json()["name"] == car_name
    # name_list = [name["name"] for name in read_response.json()]
    # for name_remove in name_list:
    #     delete_response = client.delete(f"/api/car/{name_remove}")
    #     assert delete_response.status_code == 200
    #     assert delete_response.json()["name"] ==name_remove


def test_delete_invalid_car():
    delete_response = client.delete(f"/api/car/{0}")
    assert delete_response.status_code == 303
