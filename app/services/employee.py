from tools.odoo_rpc import OdooRPC
from tools.odoo_session import get_odoo_session

session = get_odoo_session()

def list_all_employees():
    """
    Retorna todos os funcionários com informações úteis.
    """
    employee_obj = session['hr.employee']
    fields = [
        'name',
        'work_email',
        'work_phone',
        'job_id',
        'department_id',
        'birthday',
        'active',
    ]
    return employee_obj.search_read([], fields=fields)


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
    employees = list_all_employees()
    print_employees(employees)
