#payroll - платежная ведомость
#paycheck - зарплата

class PayrollPolicy:
    def __init__(self):
        self.hours_worked = 0

    def track_work(self, hours):
        self.hours_worked += hours


class LTDPolicy:
    _reduction_factor = 0.6

    def __init__(self):
        self._base_policy = None

    def apply_to_policy(self, base_policy):
        self._base_policy = base_policy

    def track_work(self, hours):
        self._check_base_policy()
        self._base_policy.track_work(hours)

    def calculate_payroll(self):
        return self._base_policy.calculate_payroll() * self._reduction_factor

    def _check_base_policy(self):
        if not self._base_policy:
            raise RuntimeError("Base policy is not defined ")


class SalaryPolicy(PayrollPolicy):
    def __init__(self, weekly_salary):
        super().__init__()
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyPolicy(PayrollPolicy):
    def __init__(self, hour_rate):
        super().__init__()
        self.hours_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hours_rate


class CommissionPolicy(SalaryPolicy):
    def __init__(self, weekly_salary, commission_per_sale):
        super().__init__(weekly_salary)
        self.commission_per_sale = commission_per_sale

    def commission(self):
        sales = int(self.hours_worked / 5)
        return sales * self.commission_per_sale

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission()


class _PayrollSystem:
    def __init__(self):
        self._employee_policies = {
            1: SalaryPolicy(3000),
            2: SalaryPolicy(1500),
            3: CommissionPolicy(1000, 100),
            4: HourlyPolicy(15),
            5: HourlyPolicy(9)
        }

    def get_policy(self, employee_id):
        policy = self._employee_policies.get(employee_id)
        if not policy:
            raise ValueError('invalid employee_id')
        return policy

    def calculate_payroll(self, employees):
        print("\nCalculating Payroll")
        print("===================")
        for employee in employees:
            print(f"\nPayroll for: {employee.id} - {employee.name}")
            print(f"- Check Amount: {employee.calculate_payroll()}")
            if employee.address:
                print("- Sent to: ", employee.address)


_payroll_system = _PayrollSystem()


def get_policy(employee_id: int):
    return _payroll_system.get_policy(employee_id)


def calculate_payroll(employees):
    _payroll_system.calculate_payroll(employees)

