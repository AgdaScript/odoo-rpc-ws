import sys
import os
from dotenv import load_dotenv

# Adiciona a pasta app/ ao sys.path
CURRENT_DIR = os.path.dirname(__file__)
APP_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '..'))
sys.path.insert(0, APP_DIR)

# Agora os imports funcionam
from tools.rpc import OdooRPC
from services.employees import list_all_employees



# Carrega variáveis do .env
load_dotenv()

URL = os.getenv("URL")
DB_NAME = os.getenv("DB_NAME")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

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
