import os
import sys

# Garante que a pasta app/ esteja no sys.path
CURRENT_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '..'))
sys.path.insert(0, BASE_DIR)

from services.birthday import get_employees_with_birthday_in_month

def print_birthday_employees(employees):
    if not employees:
        print("Nenhum aniversariante encontrado.")
    else:
        for emp in employees:
            print(f"Nome: {emp['name']}")
            print(f"Email: {emp.get('work_email', '---')}")
            print(f"Data de Nascimento: {emp.get('birthday', '---')}")
            print('-' * 40)

if __name__ == '__main__':
    try:
        # Pode passar o mês aqui, ex: 1 para Janeiro
        birthday_employees = get_employees_with_birthday_in_month()
        print_birthday_employees(birthday_employees)
    except Exception as e:
        print(f"Erro ao listar aniversariantes: {e}")
