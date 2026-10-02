"""
repositories.py
----------------
كل الاستعلامات (SQL) بتتحط هنا بس - مفيش SQL في أي مكان تاني في المشروع.
لو حبيت بعدين تغيّر من MySQL لقاعدة بيانات تانية، ده المكان الوحيد
اللي محتاج تعدّل فيه (مبدأ Abstraction).
"""

from models import Employee, Manager


class EmployeeRepository:
    def __init__(self, db):
        self.db = db  # كائن Database من db.py (Composition - مش وراثة)

    def _row_to_employee(self, row, department_name=None):
        """Converts a database row to an Employee object."""
        return Employee(
            id=row["id"], name=row["name"], email=row["email"],
            position=row["position"], salary=row["salary"],
            hire_date=row["hire_date"], department_id=row["department_id"],
            manager_id=row["manager_id"], department_name=department_name
        )

    # -------- تسجيل الدخول --------
    def find_by_credentials(self, name, email, emp_id):
        cursor = self.db.connection.cursor(dictionary=True)
        query = """
            SELECT e.id, e.name, e.email, e.position, e.salary,
                   e.hire_Date AS hire_date, e.department_id, e.manager_id,
                   d.Name AS department_name
            FROM employee e
            LEFT JOIN Department d ON e.department_id = d.ID
            WHERE e.id = %s AND e.email = %s AND e.name = %s
        """
        cursor.execute(query, (emp_id, email, name))
        row = cursor.fetchone()
        cursor.close()
        if not row:
            return None
        return self._row_to_employee(row, row.get("department_name"))

    def has_direct_reports(self, emp_id):
        """Returns True if the employee has direct reports (i.e., is a Manager)."""
        cursor = self.db.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM employee WHERE manager_id = %s", (emp_id,))
        count = cursor.fetchone()[0]
        cursor.close()
        return count > 0

    def build_manager(self, employee):
        """Converts a regular Employee to a Manager object with their team."""
        team = self.get_team(employee.id)
        return Manager(
            id=employee.id, name=employee.name, email=employee.email,
            position=employee.position, salary=employee.salary,
            hire_date=employee.hire_date, department_id=employee.department_id,
            manager_id=employee.manager_id, department_name=employee.department_name,
            team=team
        )

    # -------- Employee Inquiries --------
    def get_by_id(self, emp_id):
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT e.id, e.name, e.email, e.position, e.salary,
                   e.hire_Date AS hire_date, e.department_id, e.manager_id,
                   d.Name AS department_name
            FROM employee e
            LEFT JOIN Department d ON e.department_id = d.ID
            WHERE e.id = %s
        """, (emp_id,))
        row = cursor.fetchone()
        cursor.close()
        return self._row_to_employee(row, row.get("department_name")) if row else None

    def get_manager_name(self, emp_id):
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT m.name FROM employee e
            LEFT JOIN employee m ON e.manager_id = m.id
            WHERE e.id = %s
        """, (emp_id,))
        row = cursor.fetchone()
        cursor.close()
        return row["name"] if row and row["name"] else "No manager assigned"

    def get_projects_for_employee(self, emp_id):
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT p.name, p.start_date
            FROM employee_projects ep
            JOIN projects p ON ep.project_id = p.id
            WHERE ep.emp_id = %s
        """, (emp_id,))
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def get_salary_history(self, emp_id):
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT old_salary, new_salary, change_date
            FROM salary_history WHERE emp_id = %s
            ORDER BY change_date
        """, (emp_id,))
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def get_colleagues(self, emp_id, department_id):
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT id, name, position FROM employee
            WHERE department_id = %s AND id != %s
        """, (department_id, emp_id))
        rows = cursor.fetchall()
        cursor.close()
        return rows

    # -------- Manager Inquiries --------
    def get_team(self, manager_id):
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT id, name, position, salary FROM employee
            WHERE manager_id = %s
        """, (manager_id,))
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def update_salary(self, emp_id, new_salary):
        """
        Updates the salary + logs the change in salary_history within a single Transaction.
        If an error occurs at any step, both changes are rolled back.
        """
        cursor = self.db.connection.cursor()
        try:
            cursor.execute("SELECT salary FROM employee WHERE id = %s", (emp_id,))
            row = cursor.fetchone()
            if not row:
                raise ValueError("الموظف غير موجود")
            old_salary = row[0]

            # ملاحظة: الاتصال أصلًا autocommit=False بشكل افتراضي في mysql-connector،
            # يعني أول execute بيبدأ transaction ضمنيًا. مفيش داعي لـ start_transaction() يدويًا.
            cursor.execute(
                "INSERT INTO salary_history (emp_id, old_salary, new_salary, change_date) "
                "VALUES (%s, %s, %s, CURDATE())",
                (emp_id, old_salary, new_salary)
            )
            cursor.execute(
                "UPDATE employee SET salary = %s WHERE id = %s",
                (new_salary, emp_id)
            )
            self.db.connection.commit()
        except Exception as e:
            self.db.connection.rollback()
            raise e
        finally:
            cursor.close()

    # -------- Management Inquiries (CEO فقط) --------
    def average_salary_per_department(self):
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT d.Name AS department, AVG(e.salary) AS avg_salary,
                   COUNT(*) AS employee_count
            FROM Department d
            JOIN employee e ON e.department_id = d.ID
            GROUP BY d.Name
        """)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def team_size_per_manager(self):
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT m.name AS manager, COUNT(e.id) AS team_size
            FROM employee e
            JOIN employee m ON e.manager_id = m.id
            GROUP BY m.name
            ORDER BY team_size DESC
        """)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def total_headcount(self):
        cursor = self.db.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM employee")
        count = cursor.fetchone()[0]
        cursor.close()
        return count
