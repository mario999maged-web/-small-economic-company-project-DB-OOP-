"""
main.py
-------
نقطة تشغيل البرنامج. بيربط كل الأجزاء ببعض:
db -> repository -> auth (تسجيل دخول) -> القائمة المناسبة للدور.
"""

from db import Database
from repositories import EmployeeRepository
from auth import login, AuthenticationError
from menus import employee_menu, manager_menu, management_menu


def main():
    with Database(host="localhost", user="root", password="Mariomm2$", database="company") as db:
        repo = EmployeeRepository(db)

        try:
            employee, role = login(repo)
        except AuthenticationError as e:
            print(f"فشل تسجيل الدخول: {e}")
            return

        print(f"\nWelcome, {employee.name}! Your role in the system is: {role}")

        if role == "management":
            management_menu(repo, employee)
        elif role == "manager":
            manager_menu(repo, employee)
        else:
            employee_menu(repo, employee)


if __name__ == "__main__":
    main()
