from typing import Type

from productivity import get_role
from hr import get_policy, LTDPolicy
from contacts import get_employee_address
from representations import AsDictionaryMixin


class _EmployeeDatabase:
    name_key = "name"
    role_key = "role"

    def __init__(self):
        self._employees = {
            1: {
                'name': 'Mary Poppins',
                'role': 'manager'
            },
            2: {
                'name': 'John Smith',
                'role': 'secretary'
            },
            3: {
                'name': 'Kevin Bacon',
                'role': 'sales'
            },
            4: {
                'name': 'Jane Doe',
                'role': 'factory'
            },
            5: {
                'name': 'Robin Williams',
                'role': 'secretary'
            }
        }

    @property
    def employees(self):
        return [Employee(_id) for _id in self._employees]

    def get_employee_info(self, employee_id):
        employee_info = self._employees.get(employee_id)
        if not employee_info and not str(employee_id).isnumeric():
            raise ValueError("Wrong format of employee_id.")
        elif not employee_info:
            raise ValueError(f"Employee with id {employee_id} not found.")
        return employee_info


class Employee(AsDictionaryMixin):
    def __init__(self, id: int):
        self.id = id
        info = employee_database.get_employee_info(self.id)
        self.name = info.get(employee_database.name_key)
        self._role = get_role(info.get(employee_database.role_key))
        self.address = get_employee_address(self.id)
        self._payroll = get_policy(self.id)

    def work(self, hours) -> None:
        print(f"Employee {self.id} - {self.name}:")
        print(f"- {self._role.work(hours)}")
        print("")
        self._payroll.track_work(hours)

    def calculate_payroll(self) -> None:
        return self._payroll.calculate_payroll()

    def apply_payroll_policy(self, new_policy_class: Type[LTDPolicy]) -> None:
        new_policy = new_policy_class()
        new_policy.apply_to_policy(self._payroll)
        self._payroll = new_policy


employee_database = _EmployeeDatabase()
