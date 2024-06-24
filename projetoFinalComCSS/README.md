# LISTA DE TAREFAS

Um simples gerenciador de tarefas usando FastAPI, SQLAlchemy, e Jinja2.

## Estrutura do Projeto

ULTRA PROJETO TASK MANAGER - definitivo/
│
├── app/
│ ├── main.py
│ ├── models.py
│ ├── schemas.py
│ ├── crud.py
│ ├── database.py
│ ├── templates/
│ │ ├── base.html
│ │ ├── index.html
│ │ ├── create.html
│ │ ├── update.html
│ ├── static/
│ ├── styles.css
│
├── requirements.txt
├── README.md

## Configuração

Instale as dependências:


"""
 pip install -r requirements.txt
"""


Execute a aplicação:

"""
uvicorn app.main:app --reload
"""

Se pedir, instale tb: 

"""
pip install python-multipart
"""

A aplicação estará disponível em http://127.0.0.1:8000.