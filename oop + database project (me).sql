create database company;
use company;

CREATE TABLE Department 
(
 ID INT AUTO_INCREMENT primary key ,
 Name varchar(30) Not null
);

Create table employee
(
id int auto_increment primary key,
name  varchar(50) not null ,
salary decimal(9,2)  check (salary>=0),
position varchar(70) ,
hire_Date date,
department_id int ,
email varchar(70) not null,
manager_id int ,
foreign key (department_id) references Department(ID),
foreign key (manager_id) references employee(id)
);

create table projects 
(
id int auto_increment primary key ,
name varchar(100) not null,
start_date date
);


create table employee_projects
(
emp_id int ,
project_id int ,
primary key (emp_id,project_id), # for the foreign keys beone unit not seperated.. if they were seperated they hadto be unique from each other
foreign key (emp_id) references employee(id),
foreign key (project_id) references projects(id)
);


create table salary_history
(
id int auto_increment primary key,
emp_id int ,
old_salary decimal(9,2),
new_salary decimal(9,2),
change_date date,
foreign key (emp_id) references employee(id)
); 

INSERT INTO Department (name) VALUES 
('HR'),
('IT'),
('Customer Service'),
('Warehouse');

INSERT INTO employee (id, name, salary, position, hire_date, department_id, email, manager_id) VALUES 
(1, 'Omar El-Sayed', 150000.00, 'CEO', '2021-01-10', NULL, 'omar.elsayed@company.eg', NULL),
(2, 'Mona Hassan', 75000.00, 'Head of HR', '2021-02-15', 1, 'mona.hassan@company.eg', 1),
(3, 'Ahmed Youssef', 95000.00, 'Head of IT', '2021-01-20', 2, 'ahmed.youssef@company.eg', 1),
(4, 'Dina Mahmoud', 65000.00, 'Head of Customer Service', '2021-03-05', 3, 'dina.mahmoud@company.eg', 1),
(5, 'Tarek Ibrahim', 55000.00, 'Head of Warehouse', '2021-04-12', 4, 'tarek.ibrahim@company.eg', 1),
(6, 'Salma Ali', 25000.00, 'HR Specialist', '2021-08-01', 1, 'salma.ali@company.eg', 2),
(7, 'Kareem Mostafa', 22000.00, 'Recruiter', '2022-01-15', 1, 'kareem.mostafa@company.eg', 2),
(8, 'Noha Hussein', 28000.00, 'Payroll Coordinator', '2021-11-20', 1, 'noha.hussein@company.eg', 2),
(9, 'Heba Adel', 18000.00, 'HR Assistant', '2023-05-10', 1, 'heba.adel@company.eg', 2),
(10, 'Mohamed Salah', 55000.00, 'Senior Software Engineer', '2021-06-15', 2, 'mohamed.salah@company.eg', 3),
(11, 'Yasmine Samir', 48000.00, 'Software Engineer', '2022-03-10', 2, 'yasmine.samir@company.eg', 3),
(12, 'Amr Wael', 42000.00, 'System Administrator', '2022-07-22', 2, 'amr.wael@company.eg', 3),
(13, 'Sara Fathy', 45000.00, 'Network Engineer', '2021-09-05', 2, 'sara.fathy@company.eg', 3),
(14, 'Hisham Zaki', 28000.00, 'IT Support', '2023-01-11', 2, 'hisham.zaki@company.eg', 3),
(15, 'Nour Sherif', 26000.00, 'IT Support', '2023-08-30', 2, 'nour.sherif@company.eg', 3),
(16, 'Ali Hassan', 52000.00, 'Software Engineer', '2021-12-01', 2, 'ali.hassan@company.eg', 3),
(17, 'Rania Taha', 35000.00, 'QA Engineer', '2022-10-18', 2, 'rania.taha@company.eg', 3),
(18, 'Mahmoud Saad', 40000.00, 'Data Analyst', '2022-05-12', 2, 'mahmoud.saad@company.eg', 3),
(19, 'Aya Fouad', 22000.00, 'Helpdesk Technician', '2024-02-15', 2, 'aya.fouad@company.eg', 3),
(20, 'Hoda Nabil', 18000.00, 'Customer Service Shift Lead', '2021-04-20', 3, 'hoda.nabil@company.eg', 4),
(21, 'Youssef Kamal', 15000.00, 'Customer Service Agent', '2021-10-10', 3, 'youssef.kamal@company.eg', 4),
(22, 'Nada Amin', 15000.00, 'Customer Service Agent', '2022-01-05', 3, 'nada.amin@company.eg', 4),
(23, 'Mostafa Galal', 14500.00, 'Customer Service Agent', '2022-06-12', 3, 'mostafa.galal@company.eg', 4),
(24, 'Mai Rady', 14500.00, 'Customer Service Agent', '2022-08-21', 3, 'mai.rady@company.eg', 4),
(25, 'Hussein Farid', 16000.00, 'Customer Service Agent', '2021-09-15', 3, 'hussein.farid@company.eg', 4),
(26, 'Ramy Adel', 13500.00, 'Customer Service Agent', '2023-03-10', 3, 'ramy.adel@company.eg', 4),
(27, 'Farida Shawky', 14000.00, 'Customer Service Agent', '2023-01-25', 3, 'farida.shawky@company.eg', 4),
(28, 'Mazen Atef', 13000.00, 'Customer Service Agent', '2023-11-01', 3, 'mazen.atef@company.eg', 4),
(29, 'Laila Mansour', 13500.00, 'Customer Service Agent', '2023-07-14', 3, 'laila.mansour@company.eg', 4),
(30, 'Karim Ayman', 12500.00, 'Customer Service Agent', '2024-01-10', 3, 'karim.ayman@company.eg', 4),
(31, 'Sherine Nader', 12500.00, 'Customer Service Agent', '2024-02-28', 3, 'sherine.nader@company.eg', 4),
(32, 'Waleed Essam', 12000.00, 'Customer Service Agent', '2024-05-15', 3, 'waleed.essam@company.eg', 4),
(33, 'Hassan Fawzy', 12000.00, 'Customer Service Agent', '2024-06-20', 3, 'hassan.fawzy@company.eg', 4),
(34, 'Reem Hossam', 12000.00, 'Customer Service Agent', '2024-08-05', 3, 'reem.hossam@company.eg', 4),
(35, 'Said Gomaa', 18000.00, 'Warehouse Supervisor', '2021-05-01', 4, 'said.gomaa@company.eg', 5),
(36, 'Khaled Yassin', 14000.00, 'Inventory Clerk', '2021-11-15', 4, 'khaled.yassin@company.eg', 5),
(37, 'Ehab Ramzy', 12500.00, 'Warehouse Worker', '2022-02-20', 4, 'ehab.ramzy@company.eg', 5),
(38, 'Tamer Safwat', 12500.00, 'Warehouse Worker', '2022-04-10', 4, 'tamer.safwat@company.eg', 5),
(39, 'Ayman Ezzat', 12000.00, 'Warehouse Worker', '2022-09-05', 4, 'ayman.ezzat@company.eg', 5),
(40, 'Essam Mounir', 11500.00, 'Warehouse Worker', '2023-01-18', 4, 'essam.mounir@company.eg', 5),
(41, 'Reda Helal', 11500.00, 'Warehouse Worker', '2023-05-22', 4, 'reda.helal@company.eg', 5),
(42, 'Magdy Sobhy', 11000.00, 'Warehouse Worker', '2023-10-11', 4, 'magdy.sobhy@company.eg', 5),
(43, 'Fawzy Bahaa', 11000.00, 'Warehouse Worker', '2024-01-08', 4, 'fawzy.bahaa@company.eg', 5),
(44, 'Gaber Salem', 10500.00, 'Warehouse Worker', '2024-03-25', 4, 'gaber.salem@company.eg', 5),
(45, 'Mahmoud Othman', 10500.00, 'Warehouse Worker', '2024-07-15', 4, 'mahmoud.othman@company.eg', 5);

INSERT INTO projects (id, name, start_date) VALUES 
(1, 'Cairo Office Expansion', '2024-01-10'),
(2, 'New HR Portal Implementation', '2024-03-15'),
(3, 'Cloud Infrastructure Migration', '2024-05-01'),
(4, 'CRM System Upgrade', '2024-08-20'),
(5, 'Warehouse Automation Phase 1', '2024-10-05'),
(6, 'Customer Feedback System Revision', '2025-01-12'),
(7, 'Q1 2025 Hiring Drive', '2025-02-01'),
(8, 'Network Security Audit', '2025-04-15'),
(9, 'Inventory Management Overhaul', '2025-06-20'),
(10, 'Employee Wellness Initiative', '2025-09-10'),
(11, 'Call Center Routing Optimization', '2026-02-05'),
(12, 'Data Privacy Compliance Review', '2026-04-10');

INSERT INTO employee_projects (emp_id, project_id) VALUES 
(1, 1), (1, 3), (1, 12),
(2, 2), (2, 7), (2, 10),
(3, 2), (3, 3), (3, 8),
(4, 4), (4, 6), (4, 11),
(5, 5), (5, 9),
(6, 2), (6, 7),
(7, 7),
(8, 2),
(10, 2), (10, 3),
(11, 3), (11, 4),
(12, 3), (12, 8),
(13, 3), (13, 8),
(14, 1),
(16, 4), (16, 6),
(17, 2), (17, 4), (17, 6),
(18, 6), (18, 11),
(20, 6), (20, 11),
(21, 6),
(25, 11),
(35, 5), (35, 9),
(36, 5), (36, 9),
(37, 5),
(38, 5);

INSERT INTO salary_history (emp_id, old_salary, new_salary, change_date) VALUES 
(1, 110000.00, 130000.00, '2022-01-10'),
(1, 130000.00, 150000.00, '2024-01-10'),
(2, 55000.00, 65000.00, '2022-02-15'),
(2, 65000.00, 75000.00, '2024-02-15'),
(3, 75000.00, 85000.00, '2022-01-20'),
(3, 85000.00, 95000.00, '2024-01-20'),
(4, 50000.00, 58000.00, '2022-03-05'),
(4, 58000.00, 65000.00, '2024-03-05'),
(5, 45000.00, 50000.00, '2022-04-12'),
(5, 50000.00, 55000.00, '2024-04-12'),
(6, 20000.00, 22500.00, '2022-08-01'),
(6, 22500.00, 25000.00, '2024-08-01'),
(10, 45000.00, 50000.00, '2022-06-15'),
(10, 50000.00, 55000.00, '2024-06-15'),
(11, 40000.00, 44000.00, '2023-03-10'),
(11, 44000.00, 48000.00, '2025-03-10'),
(12, 35000.00, 38500.00, '2023-07-22'),
(12, 38500.00, 42000.00, '2025-07-22'),
(13, 38000.00, 41500.00, '2022-09-05'),
(13, 41500.00, 45000.00, '2024-09-05'),
(16, 42000.00, 47000.00, '2023-01-01'),
(16, 47000.00, 52000.00, '2025-01-01'),
(20, 14000.00, 16000.00, '2022-04-20'),
(20, 16000.00, 18000.00, '2024-04-20'),
(21, 12000.00, 13500.00, '2022-10-10'),
(21, 13500.00, 15000.00, '2024-10-10'),
(25, 13000.00, 14500.00, '2022-09-15'),
(25, 14500.00, 16000.00, '2024-09-15'),
(35, 14000.00, 16000.00, '2022-05-01'),
(35, 16000.00, 18000.00, '2024-05-01'),
(36, 11000.00, 12500.00, '2023-01-15'),
(36, 12500.00, 14000.00, '2025-01-15'),
(37, 10500.00, 11500.00, '2023-02-20'),
(37, 11500.00, 12500.00, '2025-02-20'),
(38, 10500.00, 11500.00, '2023-04-10'),
(38, 11500.00, 12500.00, '2025-04-10');

show databases;
show tables;
select *  from employee;

select e.id , e.name , d.name as department ,e.position , e.salary 
from employee e
join Department d on e.department_id = d.id ;

select employee_projects.emp_id , employee.name ,projects.name as project_name
from employee_projects
join employee on employee_projects.emp_id = employee.id
join  projects on employee_projects.project_id = projects.id 
limit 0,500;

select e.name as employee ,e.position ,e.salary,m.name as manager
from employee e
left join employee m on e.manager_id = m.id; 
 
 select d.name as department , avg(e.salary) as avg_salary , count(*) as number_of_employee
 from Department d
 join employee e on e.department_id = d.ID
 group by d.name;
 
 select m.name as manager , count(e.id) as number_of_team
 from  employee e
 join employee m on e.manager_id=m.id
 group by manager
 order by number_of_team desc;
  
select sh.emp_id , e.name as employee_name ,count(*) as raise_count
from salary_history sh
join employee e on emp_id=e.id
group by sh.emp_id,e.name
order by raise_count desc;

