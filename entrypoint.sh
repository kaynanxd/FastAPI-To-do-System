#!/bin/sh

# Executa as migrações do banco de dados
run alembic upgrade head

# Inicia a aplicação
run uvicorn --host 0.0.0.0 --port 8000 backend.app:app
