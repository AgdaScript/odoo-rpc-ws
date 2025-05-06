from datetime import datetime
from tools.odoo_session import get_odoo_session

def get_employees_with_birthday_in_month(month=None):
    """
    Retorna uma lista de funcionários com aniversários no mês especificado.
    
    :param month: Mês para procurar aniversariantes (ex: 1 para Janeiro, 2 para Fevereiro, etc.).
                  Se None, retorna todos os aniversariantes do ano.
    """
    session = get_odoo_session()
    employee_obj = session['hr.employee']
    
    # Se não for passado mês, busca todos os aniversariantes
    today = datetime.today()
    month = month or today.month

    # Busca todos os funcionários
    all_employees = employee_obj.search_read([], fields=['name', 'birthday', 'work_email'])

    # Filtra aniversariantes do mês
    birthday_employees = [
        emp for emp in all_employees
        if emp.get('birthday') and datetime.strptime(emp['birthday'], '%Y-%m-%d').month == month
    ]
    
    return birthday_employees
