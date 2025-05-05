def list_all_employees(session):
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
