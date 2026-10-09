# Employee Management System

A Python-based **Employee Management System** connected to a MySQL/MariaDB database.

The project demonstrates practical Object-Oriented Programming concepts, database integration, authentication, role-based menus, SQL repositories, transactions, and custom exceptions.

---

## 📌 Project Overview

The system provides different interfaces depending on the user's role:

* **Management (CEO)**
* **Manager**
* **Employee**

Users can log in using their account information, and the system automatically identifies their role and displays the appropriate menu.

---

## 🛠️ Technologies Used

* **Python 3**
* **MySQL / MariaDB**
* **mysql-connector-python**
* Object-Oriented Programming (OOP)
* SQL
* Database Transactions

---

## ✨ Main Features

### 🔐 Authentication

* User login system
* Automatic role identification
* Role-based access to system menus

### 👨‍💼 Employee Management

* Employee-related operations
* Employee and Manager classes
* Object-Oriented design using inheritance and properties

### 🗄️ Database

* MySQL / MariaDB integration
* Centralized SQL queries
* Transactions for database operations
* Database connection handled through a Context Manager

### 🧩 OOP Concepts

The project demonstrates:

* Classes
* Inheritance
* Composition
* Properties
* Dunder Methods
* Custom Exceptions
* Context Managers

---

## 📦 Installation

Install the required Python package:

```bash
pip install mysql-connector-python
```

---

## ⚙️ Setup

### 1. Create the Database

Run:

```text
schema_and_data.sql
```

using **MySQL/MariaDB**.

This script creates the `company` database, its tables, and the sample data.

### 2. Configure Database Connection

Open:

```text
main.py
```

and update the database connection information if necessary:

```text
host
user
password
```

### 3. Run the Application

```bash
python3 main.py
```

---

## 🔑 Sample Login Data

The project includes ready-to-use sample accounts:

| Role             | Name          | Email                                                     | ID |
| ---------------- | ------------- | --------------------------------------------------------- | -: |
| Management (CEO) | Omar El-Sayed | [omar.elsayed@company.eg](mailto:omar.elsayed@company.eg) |  1 |
| Manager          | Mona Hassan   | [mona.hassan@company.eg](mailto:mona.hassan@company.eg)   |  2 |
| Employee         | Salma Ali     | [salma.hassan@company.eg](mailto:salma.hassan@company.eg) |  6 |

---

## 📁 Project Structure

```text
Employee-Management-System/
│
├── schema_and_data.sql
├── db.py
├── models.py
├── repositories.py
├── auth.py
├── menus.py
├── main.py
└── README.md
```

### File Responsibilities

| File                  | Description                                                     |
| --------------------- | --------------------------------------------------------------- |
| `db.py`               | Handles database connections using a Context Manager            |
| `models.py`           | Contains `Employee` and `Manager` classes and OOP functionality |
| `repositories.py`     | Contains SQL queries, Composition, and Transactions             |
| `auth.py`             | Handles authentication and automatic role identification        |
| `menus.py`            | Contains Employee, Manager, and Management menus                |
| `main.py`             | Application entry point                                         |
| `schema_and_data.sql` | Creates the database structure and sample data                  |

---

## 🧠 OOP Concepts Demonstrated

This project was designed to apply several Python OOP concepts in a practical application:

```text
Employee
   │
   └── Manager
```

The project uses:

* **Inheritance** to extend employee functionality
* **Properties** for controlled attribute access
* **Dunder Methods** for customized object behavior
* **Composition** for organizing database operations
* **Custom Exceptions** for application-specific errors
* **Context Managers** for safe database connection handling

---

## 🚀 Running the Project

After configuring the database:

```bash
python3 main.py
```

Then log in using one of the sample accounts above.

The system will determine the user's role and display the corresponding menu.

---

## 🎯 Project Purpose

This project was built to practice combining:

**Python + OOP + SQL + MySQL + Authentication**

into a complete console-based application rather than working with these concepts separately.

---

## 👨‍💻 Project Status

**Completed — Educational Project**

The project focuses on demonstrating Python OOP and database programming concepts through a practical Employee Management System.
