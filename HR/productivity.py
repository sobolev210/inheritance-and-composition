from abc import ABC, abstractmethod
from typing import List, Union


class Role(ABC):
    @abstractmethod
    def work(self, hours):
        raise NotImplementedError


class ManagerRole(Role):
    def work(self, hours):
        return f'manages people for {hours} hours.'


class SecretaryRole(Role):
    def work(self, hours):
        return f'expends {hours} hours doing office paperwork.'


class SalesRole(Role):
    def work(self, hours):
        return f'expends {hours} hours on the phone.'


class FactoryRole(Role):
    def work(self, hours):
        return f'manufactures gadjets for {hours} hours.'


class _ProductivitySystem:
    def __init__(self):
        self._roles = {
            "manager": ManagerRole,
            "secretary": SecretaryRole,
            "sales": SalesRole,
            "factory": FactoryRole
        }

    def get_role(self, role_id: str) -> Role:
        role_type = self._roles.get(role_id)
        if role_type is None:
            raise ValueError(f"Invalid role_id: {role_id}")
        return role_type()

    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('==============================')
        for employee in employees:
            employee.work(hours)
        print("")


_productivity_system = _ProductivitySystem()


def get_role(role_id: str):
    return _productivity_system.get_role(role_id)


def track(employees: List['Employee'], hours: Union[int, float]):
    _productivity_system.track(employees, hours)

