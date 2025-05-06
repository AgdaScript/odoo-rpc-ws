from fastapi import FastAPI
import os
import sys

# Garante que a pasta app/ esteja no sys.path
CURRENT_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '..'))
sys.path.insert(0, BASE_DIR)

from api.birthday_api import app  # Importando a instância da API

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
