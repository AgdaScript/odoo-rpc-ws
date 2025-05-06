import os
import sys

# Garante que a pasta app/ esteja no sys.path
CURRENT_DIR = os.path.dirname(__file__)
APP_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '..'))
sys.path.insert(0, APP_DIR)

from services.employee import list_all_employees

def print_employees(employees):
    for emp in employees:
        print(f"Nome: {emp['name']}")
        print(f"Cargo: {emp.get('job_id', [''])[1] if emp.get('job_id') else '---'}")
        print(f"Departamento: {emp.get('department_id', [''])[1] if emp.get('department_id') else '---'}")
        print(f"Email: {emp.get('work_email', '---')}")
        print(f"Telefone: {emp.get('work_phone', '---')}")
        print(f"Data de Nascimento: {emp.get('birthday', '---')}")
        print(f"Ativo: {'Sim' if emp.get('active') else 'Não'}")
        print('-' * 40)

if __name__ == '__main__':
    try:
        employees = list_all_employees()
        print_employees(employees)
    except Exception as e:
        print(f"Erro ao listar funcionários: {e}")
