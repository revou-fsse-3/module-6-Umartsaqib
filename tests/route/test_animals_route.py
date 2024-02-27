

def test_get_all_animals(client):
   
    response = client.get("/animals", follow_redirects=True)
    assert response.status_code == 200
    

def test_get_animal_by_id(client):
    
    response = client.get("/animals/1")
    assert response.status_code == 404 

def test_create_animal(client):
    
    data = {
        "name": "Test Animal",
        "age": 2,
        "type": "Test Type",
        "gender": "Test Gender"
    }
    response = client.post("/animals", json=data)
    assert response.status_code == 308  

def test_update_animal(client):
    
    animal_id = 1  
    data = {
        "name": "Updated Animal",
        "age": 3,
        "type": "Updated Type",
        "gender": "Updated Gender"
    }
    response = client.put(f"/animals/{animal_id}", json=data)
    assert response.status_code == 404  

def test_delete_animal(client):
    
    animal_id = 1  
    response = client.delete(f"/animals/{animal_id}")
    assert response.status_code == 404  
