from starlette.testclient import TestClient

from main import app

client = TestClient(app)




def test_create_track():
    

    data = {"name": "test_create_1",
            "description": "Test"
             }
    response = client.post("/api/track/", json=data)
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert content["description"] == data["description"]
    assert "id" in content

def test_create_duplicate_track():
    data = {"name": "test_create_2",
            "description": "Test"}

    first_response = client.post("/api/track/", json=data)
    assert first_response.status_code == 200
    second_response = client.post("/api/track/", json=data)
    assert second_response.status_code == 303

def test_update_track():
    insert_data = {"name": "test_update_1",
                   "description": "Test"}

    insert_response = client.post("/api/track/", json=insert_data)
    assert insert_response.status_code == 200
    update_name = insert_response.json()["name"]

    update_data = {
        "name": "Name updated",
        "description": "description updated"
    }

    update_response = client.put(f"/api/track/{update_name}", json=update_data)
    assert update_response.status_code == 200
    assert update_response.json()["name"] == update_data["name"]

def test_update_invalid_track():
    update_data = {
        "name": "name updated",
        "description": "invalid update "
    }

    update_response = client.put(f"/api/track/{0}", json=update_data)
    assert update_response.status_code == 303



def test_read_track():
    
    insert_data = {"name": "test_read_1",
                    "description": "reading data"}

    insert_response = client.post("/api/track/", json=insert_data)
    assert insert_response.status_code == 200
    read_name = insert_response.json()["name"]

    read_response = client.get(f"/api/track/{read_name}")
    response_data = insert_response.json()
    assert read_response.status_code == 200
    assert insert_data["name"] == response_data["name"]
    assert insert_data["description"] == response_data["description"]


def test_read_tracks():
    read_response = client.get(f"/api/track/")
    assert read_response.status_code == 200
    assert type(read_response.json()) == list


def test_read_invalid_track():
    update_response = client.get(f"/api/track/{0}")
    assert update_response.status_code == 404

  
def test_delete_track():
    read_response = client.get(f"/api/track/")
    name_list = [name["name"] for name in read_response.json()]
    for name_remove in name_list:
        delete_response = client.delete(f"/api/track/{name_remove}")
        assert delete_response.status_code == 200
        assert delete_response.json()["name"] == name_remove

def test_delete_invalid_track():
    delete_response = client.delete(f"/api/track/{1}")
    assert delete_response.status_code == 303