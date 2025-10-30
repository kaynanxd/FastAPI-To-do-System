# ✅ FastAPI To-Do System (Sistema de Tarefas Assíncrono)

Este projeto é um template de backend robusto e moderno, construído com **FastAPI**, focado em um sistema completo de gerenciamento de tarefas (To-Do List). Ele demonstra o uso das melhores práticas assíncronas do Python e a infraestrutura de contêineres para ambientes de desenvolvimento.

---

## ✨ Destaques do Projeto

O projeto é um template de alta qualidade, ilustrando as melhores práticas em Python:

* **Assincronicidade Completa (`async/await`):** A arquitetura utiliza o `asyncio` em todas as camadas, desde o servidor FastAPI até a comunicação com o banco de dados (SQLAlchemy 2.0+), garantindo alta performance e não-bloqueio do *event loop*.
* **SQLAlchemy 2.0 Assíncrono:** Uso do padrão **`AsyncSession`** e *Declarative Mapped* para definição de modelos e persistência de dados eficiente.
* **Segurança (JWT):** Implementação completa de autenticação e autorização via **JSON Web Tokens (JWT)**, gerenciada pelo `python-jose` e integrada à injeção de dependência do FastAPI.
* **Contêinerização Profissional:** Configuração robusta com **Docker e Docker Compose** para isolamento de ambiente e simplificação do *deploy*.
* **Testes de Integração:** Suíte completa de testes usando **Pytest** e *fixtures* assíncronas para garantir a funcionalidade de todas as rotas de CRUD e autenticação.

---

## ⚙️ Tecnologias Principais

| Categoria | Ferramenta | Propósito |
| :--- | :--- | :--- |
| **Framework** | FastAPI | Desenvolvimento rápido de API de alta performance e documentação automática. |
| **BD & ORM** | PostgreSQL & SQLAlchemy (Async) | Persistência de dados assíncrona e suporte ao driver `psycopg`. |
| **Gerenciamento de Pacotes** | `uv` (Rúst) | Instalação e gestão de dependências ultra-rápida. |
| **Segurança** | JWT (`python-jose`) & `pwdlib` | Autenticação, tokenização e *hashing* seguro de senhas. |
| **Contêineres** | Docker & Docker Compose | Ambiente de desenvolvimento isolado e replicável. |
| **Migrações** | Alembic | Gerenciamento de esquema de banco de dados. |

---

## 🚀 Como Executar o Projeto (Docker Compose)

A maneira mais recomendada de iniciar o projeto, garantindo que o banco de dados PostgreSQL esteja pronto para as migrações, é usando o Docker Compose.

### Pré-requisitos

* Docker e Docker Compose instalados.

### 1. Clonar e Construir

```bash
git clone https://github.com/kaynanxd/FastAPI-To-do-System
cd FastAPI-To-do-System

# Constrói a imagem da aplicação (lendo o Dockerfile)
docker compose build
docker compose up -d
```

3. Acessar a API
   
Servidor: A aplicação estará disponível em http://127.0.0.1:8000
Documentação Interativa (Swagger UI): Acesse http://127.0.0.1:8000/docs

