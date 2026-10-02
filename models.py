"""
models.py
---------
الكلاسات اللي بتمثل البيانات (Employee, Manager).
دول مالهمش علاقة بـ SQL خالص - هما بس "شكل" البيانات في الذاكرة.
الاستعلامات نفسها هتكون في repositories.py (Separation of Concerns).
"""

from datetime import date


class Employee:
    """main class for employees."""

    def __init__(self, id, name, email, position, salary,
                 hire_date, department_id, manager_id, department_name=None):
        self.id = id
        self.name = name
        self.email = email
        self.position = position
        self._salary = salary          # underscore = property هتحميه
        self.hire_date = hire_date
        self.department_id = department_id
        self.manager_id = manager_id
        self.department_name = department_name  # بيتملي من الـ repository لما يعمل JOIN

    # -------- Property Decorator: منع المرتب يبقى سالب --------
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise InvalidSalaryError("salary cannot be a negative number")
        self._salary = value

    # -------- Dunder Methods --------
    def __repr__(self):
        return (f"Employee(id={self.id}, name='{self.name}', "
                f"position='{self.position}', salary={self._salary})")

    def __str__(self):
        return f"{self.name} - {self.position} ({self.department_name or 'no department'})"

    def __eq__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        return self.id == other.id

    # -------- Method عادي --------
    def years_of_service(self):
        """calculate years of service approximately."""
        if not self.hire_date:
            return None
        today = date.today()
        return today.year - self.hire_date.year - (
            (today.month, today.day) < (self.hire_date.month, self.hire_date.day)
        )


class Manager(Employee):
    """
    subclass of Employee, with a team of direct reports."""

    def __init__(self, *args, team=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.team = team or []   # قائمة الموظفين التابعين له (هتتملى من الـ repository)

    def team_size(self):
        return len(self.team)

    def __repr__(self):
        return (f"Manager(id={self.id}, name='{self.name}', "
                f"team_size={self.team_size()})")


# -------- Custom Exception --------
class InvalidSalaryError(Exception):
    """raised when an employee's salary is set to a negative number."""
    pass
