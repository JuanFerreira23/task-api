# Task API

API REST para gerenciamento de tarefas, desenvolvida com FastAPI, SQLAlchemy e SQLite.

O projeto foi criado para praticar desenvolvimento backend, persistência de dados, validação, filtros, paginação e testes automatizados.

## Funcionalidades

- Criar tarefas
- Listar tarefas
- Buscar tarefa por ID
- Atualizar tarefa completamente com PUT
- Atualizar parcialmente com PATCH
- Excluir tarefas
- Filtrar por status
- Pesquisar pelo título
- Paginar resultados
- Validar dados de entrada
- Persistir dados com SQLite
- Executar testes automatizados

## Tecnologias

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Pytest
- HTTPX
- Uvicorn

## Estrutura do projeto

```text
task-api/
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   └── schemas.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── .gitignore
├── README.md
└── requirements.txt