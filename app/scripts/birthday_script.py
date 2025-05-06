from datetime import datetime
import os
import sys

# Garante que a pasta app/ esteja no sys.path
CURRENT_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '..'))
sys.path.insert(0, BASE_DIR)

from services.birthday_service import get_employees_by_birthday

def print_birthday_employees(employees):
    if not employees:
        print("Nenhum aniversariante encontrado.")
    else:
        for emp in employees:
            print(f"Nome: {emp['name']}")
            print(f"Email: {emp.get('work_email', '---')}")
            
            birthday = emp.get('birthday')
            if birthday:
                try:
                    # Convertendo a data de nascimento para o formato desejado
                    birthday_date = datetime.strptime(birthday, '%Y-%m-%d')  # Odoo retorna data no formato YYYY-MM-DD
                    day_month = birthday_date.strftime('%d-%m')  # Formato dia-mês
                    print(f"Dia Aniversário: {day_month}")
                except ValueError:
                    print(f"Data de aniversário inválida para {emp['name']}")
            else:
                print(f"Dia Aniversário: ---")
            
            print('-' * 40)

if __name__ == '__main__':
    try:
        # Obtém todos os aniversariantes para o dia 14 de maio
        birthday_employees = get_employees_by_birthday(5, 14)
        print_birthday_employees(birthday_employees)
    except Exception as e:
        print(f"Erro ao listar aniversariantes: {e}")
