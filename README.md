# Task API

Uma API REST para gerenciamento de tarefas desenvolvida com **FastAPI**, **PostgreSQL**, **SQLAlchemy** e **Docker**.

O projeto foi desenvolvido para praticar conceitos modernos de desenvolvimento backend, incluindo arquitetura em camadas, persistência de dados, migrações de banco, conteinerização, validação de dados, filtros, paginação e testes automatizados.

---

# Funcionalidades

- Criar tarefas
- Listar tarefas
- Buscar tarefa por ID
- Atualizar tarefas (PUT)
- Atualização parcial (PATCH)
- Excluir tarefas
- Filtrar por status (`completed`)
- Pesquisar por título (`search`)
- Paginação (`skip` e `limit`)
- Definir prioridade (`low`, `medium`, `high`)
- Registro automático de data de criação
- Registro automático de última atualização
- Validação de dados com Pydantic
- Documentação automática com Swagger/OpenAPI
- Migrações de banco com Alembic
- Testes automatizados

---

# Tecnologias

- Python 3.12
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Docker
- Docker Compose
- Pydantic
- Pytest
- HTTPX
- Uvicorn

---

# Arquitetura

```
Cliente
    │
    ▼
FastAPI
    │
    ▼
SQLAlchemy ORM
    │
    ▼
PostgreSQL
```

---

# Estrutura do Projeto

```text
task-api/
│
├── app/
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   └── schemas.py
│
├── migrations/
│   ├── env.py
│   └── versions/
│
├── tests/
│
├── Dockerfile
├── compose.yaml
├── alembic.ini
├── requirements.txt
└── README.md
```

---

# Como executar

## 1. Clonar o projeto

```bash
git clone https://github.com/SEU-USUARIO/task-api.git
```

```bash
cd task-api
```

---

## 2. Criar ambiente virtual

Windows

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

Linux/Mac

```bash
source .venv/bin/activate
```

---

## 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 4. Executar

```bash
uvicorn app.main:app --reload
```

---

# Executando com Docker

Construir os containers

```bash
docker compose build
```

Subir o projeto

```bash
docker compose up -d
```

---

# Aplicar Migrações

```bash
alembic upgrade head
```

---

# Documentação da API

Swagger

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# Executar os testes

```bash
pytest
```

---

# Endpoints

| Método | Endpoint | Descrição |
|---------|----------|-----------|
| GET | /tasks | Lista tarefas |
| GET | /tasks/{id} | Busca tarefa |
| POST | /tasks | Cria tarefa |
| PUT | /tasks/{id} | Atualiza tarefa |
| PATCH | /tasks/{id} | Atualização parcial |
| DELETE | /tasks/{id} | Remove tarefa |

---

# Exemplo de requisição

```json
{
    "title": "Estudar FastAPI",
    "description": "Criar API REST",
    "completed": false,
    "priority": "high"
}
```

Resposta

```json
{
    "id": 1,
    "title": "Estudar FastAPI",
    "description": "Criar API REST",
    "completed": false,
    "priority": "high",
    "created_at": "...",
    "updated_at": "..."
}
```

---

# Melhorias futuras

- Autenticação JWT
- Cadastro de usuários
- Controle de acesso por usuário
- Deploy em nuvem
- CI/CD com GitHub Actions

---

# Licença

Este projeto foi desenvolvido para fins de estudo e construção de portfólio.