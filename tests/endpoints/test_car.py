from starlette.testclient import TestClient

from main import app

client = TestClient(app)





    
def test_delete_car():
    read_response = client.get(f"/api/car/")
    name_list = [name["name"] for name in read_response.json()]
    for name_remove in name_list:
        delete_response = client.delete(f"/api/car/{name_remove}")
        assert delete_response.status_code == 200
        assert delete_response.json()["name"] ==name_remove

