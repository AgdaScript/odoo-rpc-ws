from datetime import datetime
from tools.odoo_session import get_odoo_session

def get_employees_by_birthday(month: int, day: int):
    # Simulação da sessão Odoo (substitua pela lógica real de conexão com o Odoo)
    session = get_odoo_session()  # Esta função precisa estar implementada em outro lugar no seu código.
    employee = session['hr.employee']

    # Buscar todos os funcionários, sem filtrar pela data de nascimento diretamente no domínio
    fields = ['name', 'birthday', 'work_email']  # Campos necessários
    employees = employee.search_read([], fields=fields)

    # Filtrando os aniversariantes pela data de nascimento (mês e dia)
    birthday_employees = []
    for emp in employees:
        # Convertendo a data de nascimento para o formato de data
        birthday = emp.get('birthday')
        if birthday:
            birthday_date = datetime.strptime(birthday, '%Y-%m-%d')  # Odoo retorna data no formato YYYY-MM-DD
            if birthday_date.month == month and birthday_date.day == day:
                birthday_employees.append(emp)

    return birthday_employees
