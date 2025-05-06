# app/birthday/list_all_birthdays.py

import sys
import os

# Adiciona a pasta pai ao sys.path para importar módulos corretamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.odoo_session import get_odoo_session
from services.employees import get_all_employees  # assumindo que existe ou vamos criar

# Conecta com o Odoo
session = get_odoo_session()

# Busca todos os funcionários
employees = get_all_employees(session)

# Filtra os que têm data de nascimento registrada
birthdays = [emp for emp in employees if emp.get('birthday')]

# Exibe os aniversariantes
for emp in birthdays:
    print(f"{emp['name']} faz anos em {emp['birthday']}")
