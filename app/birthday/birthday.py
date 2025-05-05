import sys
import os
from dotenv import load_dotenv

# Adiciona a pasta pai ao path para importar os módulos corretamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Carrega variáveis do .env
load_dotenv()

from tools.rpc import OdooRPC
from services.employees import employees_with_upcoming_birthday

# Variáveis de ambiente
URL = os.getenv('ODOO_URL')
DB_NAME = os.getenv('ODOO_DB')
USERNAME = os.getenv('ODOO_USER')
PASSWORD = os.getenv('ODOO_PASS')

session = OdooRPC(URL, DB_NAME, USERNAME, PASSWORD)
session.connect()

result = employees_with_upcoming_birthday(session, days=5)

for emp in result:
    print(f"{emp['name']} faz anos em {emp['birthday']}")
