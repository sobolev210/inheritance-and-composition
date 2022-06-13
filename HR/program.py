import json

from hr import calculate_payroll, LTDPolicy
from productivity import track
from employees import employee_database


def print_dict(d):
    print(json.dumps(d, indent=2))


employees = employee_database.employees
sales_employee = employees[2]
secretary_employee = employees[1]
sales_employee.apply_payroll_policy(LTDPolicy)
secretary_employee.apply_payroll_policy(LTDPolicy)
track(employees, 40)
calculate_payroll(employees)
