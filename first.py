class Employee:
    def _init_(self, name):
        self.__name = name  

    def get_name(self):
        return self.__name

    def calculate_salary(self, base_salary):
        return base_salary


class OvertimeCalculator(Employee):
    def _init_(self, name, hours_worked):
        super()._init_(name)
        self.__hours_worked = hours_worked

    def calculate_salary(self, base_salary):
        overtime_rate = 1.5
        overtime_hours_threshold = 40

        overtime_hours = max(0, self.__hours_worked - overtime_hours_threshold)
        overtime_pay = overtime_hours * (base_salary / 40) * overtime_rate
        total_salary = base_salary + overtime_pay

        return total_salary