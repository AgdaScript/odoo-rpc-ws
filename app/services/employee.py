from tools.odoo_session import get_odoo_session

def list_all_employees():
    """
    Retorna todos os funcionários com informações úteis.
    """
    session = get_odoo_session()
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
