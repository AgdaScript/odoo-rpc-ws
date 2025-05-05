import sys
import os
from dotenv import load_dotenv

# Caminho absoluto até a raiz do projeto
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, BASE_DIR)

from tools.rpc import OdooRPC
from services.employees import list_all_employees


# Carrega variáveis do .env
load_dotenv()

URL = os.getenv("ODOO_URL")
DB_NAME = os.getenv("ODOO_DB_NAME")
USERNAME = os.getenv("ODOO_USERNAME")
PASSWORD = os.getenv("ODOO_PASSWORD")

# Conecta com o Odoo
session = OdooRPC(URL, DB_NAME, USERNAME, PASSWORD)
session.connect()

# Busca e exibe todos os funcionários
employees = list_all_employees(session)

for emp in employees:
    print(f"Nome: {emp['name']}")
    print(f"Cargo: {emp.get('job_id', [''])[1] if emp.get('job_id') else '---'}")
    print(f"Departamento: {emp.get('department_id', [''])[1] if emp.get('department_id') else '---'}")
    print(f"Email: {emp.get('work_email', '---')}")
    print(f"Telefone: {emp.get('work_phone', '---')}")
    print(f"Data de Nascimento: {emp.get('birthday', '---')}")
    print(f"Ativo: {'Sim' if emp.get('active') else 'Não'}")
    print('-' * 40)
