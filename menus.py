"""
menus.py
--------
كل قائمة (menu) هي دالة منفصلة - بتاخد الـ repo والموظف الحالي،
وبتعرض خيارات وتنفذ الاستعلام المناسب.
"""

from models import InvalidSalaryError


def employee_menu(repo, employee):
    while True:
        print(f"\n--- Employee Inquiries: {employee.name} ---")
        print("1. show my data")
        print("2. direct manager's name")
        print("3. projects I'm working on")
        print("4. salary change history")
        print("5. colleagues in my department")
        print("0. logout")
        choice = input("choose: ").strip()

        if choice == "1":
            print(employee)
            print(f"years of service: {employee.years_of_service()}")
        elif choice == "2":
            print("direct manager's name:", repo.get_manager_name(employee.id))
        elif choice == "3":
            projects = repo.get_projects_for_employee(employee.id)
            if not projects:
                print("no projects registered.")
            for p in projects:
                print(f"- {p['name']} (started on {p['start_date']})")
        elif choice == "4":
            history = repo.get_salary_history(employee.id)
            if not history:
                print("no salary change history found.")
            for h in history:
                print(f"- {h['change_date']}: {h['old_salary']} → {h['new_salary']}")
        elif choice == "5":
            colleagues = repo.get_colleagues(employee.id, employee.department_id)
            for c in colleagues:
                print(f"- {c['name']} ({c['position']})")
        elif choice == "0":
            break
        else:
            print("invalid choice.")


def manager_menu(repo, manager):
    while True:
        print(f"\n--- Manager Inquiries: {manager.name} (فريق: {manager.team_size()}) ---")
        print("1. show my data")
        print("2. show my team")
        print("3. update employee salary")
        print("0. logout")
        choice = input("choose: ").strip()

        if choice == "1":
            print(manager)
        elif choice == "2":
            for member in manager.team:
                print(f"- {member['name']} ({member['position']}) - {member['salary']} جنيه")
        elif choice == "3":
            try:
                target_id = int(input("ID employee: ").strip())
                # تأكد إن الموظف فعلاً في فريقه (صلاحية بسيطة)
                team_ids = [m["id"] for m in manager.team]
                if target_id not in team_ids:
                    print("the employee is not in your team.")
                    continue
                new_salary = float(input("new salary: ").strip())
                repo.update_salary(target_id, new_salary)
                manager.team = repo.get_team(manager.id)  # تحديث الفريق بعد التعديل
                print("salary updated successfully.")
            except (ValueError, InvalidSalaryError) as e:
                print(f"خطأ: {e}")
        elif choice == "0":
            break
        else:
            print("invalid choice.")


def management_menu(repo, ceo):
    while True:
        print(f"\n--- Management Inquiries: {ceo.name} ---")
        print("1. average salaries per department")
        print("2. team size per manager")
        print("3. total number of employees")
        print("0. logout")
        choice = input("choose: ").strip()

        if choice == "1":
            for row in repo.average_salary_per_department():
                print(f"- {row['department']}: average {row['avg_salary']:.2f} "
                      f"({row['employee_count']} employee)")
        elif choice == "2":
            for row in repo.team_size_per_manager():
                print(f"- {row['manager']}: {row['team_size']} employee)")
        elif choice == "3":
            print("Total number of employees:", repo.total_headcount())
        elif choice == "0":
            break
        else:
            print("invalid choice.")
