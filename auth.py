"""
auth.py
-------
مسؤول عن حاجة واحدة بس: تسجيل الدخول وتحديد دور المستخدم.
"""


class AuthenticationError(Exception):
    """raised when login credentials are invalid."""
    pass


def login(repo):
    """
    prompts the user for login credentials, checks them against the repository,
    and returns the authenticated employee and their role.   
    """
    print("===login===")
    name = input("Name: ").strip()
    email = input("Email: ").strip()
    try:
        emp_id = int(input("Employee ID: ").strip())
    except ValueError:
        raise AuthenticationError("Employee ID must be a number")

    employee = repo.find_by_credentials(name, email, emp_id)
    if not employee:
        raise AuthenticationError("Invalid login credentials")

    # تحديد الدور
    if employee.position == "CEO":
        role = "management"
    elif repo.has_direct_reports(employee.id):
        role = "manager"
        employee = repo.build_manager(employee)   # نحوّله لكائن Manager
    else:
        role = "employee"

    return employee, role
