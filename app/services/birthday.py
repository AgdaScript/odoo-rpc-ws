from tools.lazy_loader import build_date_range
from tools.odoo_session import get_odoo_session
from datetime import datetime

def get_employees_by_birthday(month: int, day: int, direction="center", days=14):
    session = get_odoo_session()
    employee = session['hr.employee']

    # Define intervalo de datas
    center_date = datetime(datetime.now().year, month, day)
    start, end = build_date_range(center_date, days, direction)

    # Formata para strings 'MM-DD'
    start_str = start.strftime('%m-%d')
    end_str = end.strftime('%m-%d')

    # Filtro em string porque birthday é tipo char 'YYYY-MM-DD'
    domain = [('birthday', '>=', f'0000-{start_str}'), ('birthday', '<=', f'9999-{end_str}')]

    fields = ['name', 'birthday', 'job_id', 'department_id']
    return employee.search_read(domain, fields=fields)
