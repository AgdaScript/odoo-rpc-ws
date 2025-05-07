from datetime import datetime
from tools.odoo_session import get_odoo_session

def get_employees_by_birthday(month: int = None, day: int = None):
    session = get_odoo_session()
    employee = session['hr.employee']

    fields = ['name', 'birthday', 'work_email']
    employees = employee.search_read([], fields=fields)

    birthday_employees = []
    for emp in employees:
        birthday = emp.get('birthday')
        if birthday:
            birthday_date = datetime.strptime(birthday, '%Y-%m-%d')

            if month and day:
                if birthday_date.month == month and birthday_date.day == day:
                    birthday_employees.append(emp)
            elif month:
                if birthday_date.month == month:
                    birthday_employees.append(emp)
            else:
                birthday_employees.append(emp)

    return birthday_employees

