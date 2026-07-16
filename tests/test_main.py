from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Task API funcionando"
    }


def test_create_task():
    task_data = {
        "title": "Tarefa de teste",
        "description": "Testar criação de tarefa",
        "completed": False,
    }

    response = client.post(
        "/tasks/",
        json=task_data,
    )

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


def test_filter_tasks_by_completed():
    response = client.get(
        "/tasks/",
        params={"completed": "false"},
    )

    assert response.status_code == 200

    tasks = response.json()

    assert all(
        task["completed"] is False
        for task in tasks
    )


def test_search_tasks_by_title():
    task_data = {
        "title": "Estudar FastAPI",
        "description": "Testar busca por título",
        "completed": False,
    }

    create_response = client.post(
        "/tasks/",
        json=task_data,
    )

    assert create_response.status_code == 201

    response = client.get(
        "/tasks/",
        params={"search": "FastAPI"},
    )

    assert response.status_code == 200

    tasks = response.json()

    assert len(tasks) >= 1

    assert all(
        "fastapi" in task["title"].lower()
        for task in tasks
    )


def test_filter_and_search_tasks():
    task_data = {
        "title": "Estudar SQLAlchemy",
        "description": "Testar filtros combinados",
        "completed": False,
    }

    create_response = client.post(
        "/tasks/",
        json=task_data,
    )

    assert create_response.status_code == 201

    response = client.get(
        "/tasks/",
        params={
            "completed": "false",
            "search": "SQL",
        },
    )

    assert response.status_code == 200

    tasks = response.json()

    assert len(tasks) >= 1

    assert all(
        task["completed"] is False
        and "sql" in task["title"].lower()
        for task in tasks
    )


def test_task_pagination():
    response = client.get(
        "/tasks/",
        params={
            "skip": 0,
            "limit": 2,
        },
    )

    assert response.status_code == 200

    tasks = response.json()

    assert isinstance(tasks, list)
    assert len(tasks) <= 2


def test_partially_update_task():
    task_data = {
        "title": "Testar atualização parcial",
        "description": "Tarefa criada para testar PATCH",
        "completed": False,
    }

    create_response = client.post(
        "/tasks/",
        json=task_data,
    )

    assert create_response.status_code == 201

    created_task = create_response.json()
    task_id = created_task["id"]

    update_response = client.patch(
        f"/tasks/{task_id}",
        json={"completed": True},
    )

    assert update_response.status_code == 200

    updated_task = update_response.json()

    assert updated_task["id"] == task_id
    assert updated_task["title"] == task_data["title"]
    assert updated_task["description"] == task_data["description"]
    assert updated_task["completed"] is True