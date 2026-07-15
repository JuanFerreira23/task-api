from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Task API funcionando"}


def test_create_task():
    task_data = {
        "title": "Tarefa de teste",
        "description": "Testar criação de tarefa",
        "completed": False,
    }

    response = client.post("/tasks/", json=task_data)

    assert response.status_code == 201

    response_data = response.json()

    assert response_data["title"] == task_data["title"]
    assert response_data["description"] == task_data["description"]
    assert response_data["completed"] is False
    assert "id" in response_data


def test_list_tasks():
    response = client.get("/tasks/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)