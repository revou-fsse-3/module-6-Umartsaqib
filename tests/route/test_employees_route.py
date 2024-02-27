
def test_get_all_employees(client):
    
    response = client.get("/employees", follow_redirects=True)
    assert response.status_code == 200
    

def test_get_employee_by_id(client):
    
    response = client.get("/employees/1", follow_redirects=True)
    assert response.status_code == 404  

def test_create_employee(client):
    
    data = {
        "name": "Test Employee",
        "gender": "Test Gender",
        "phone": 1234567890,
        "address": "Test Address"
    }
    response = client.post("/employees", json=data, follow_redirects=True)
    assert response.status_code == 200 

def test_update_employee(client):
   
    data = {
        "name": "Updated Employee",
        "gender": "Updated Gender",
        "phone": 9876543210,
        "address": "Updated Address"
    }
    response = client.put("/employees/1", json=data, follow_redirects=True)
    assert response.status_code == 404  

def test_delete_employee(client):
    # Test deleting an existing employee by ID
    response = client.delete("/employees/1", follow_redirects=True)
    assert response.status_code == 404  
