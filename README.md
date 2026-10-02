# Employee Management System

## المتطلبات
```
pip install mysql-connector-python
```

## التشغيل
1. شغّل `schema_and_data.sql` على MySQL/MariaDB عندك (بينشئ قاعدة بيانات `company` بكل الجداول والبيانات التجريبية).
2. عدّل بيانات الاتصال في `main.py` لو مختلفة عندك (host / user / password).
3. شغّل:
```
python3 main.py
```

## بيانات تجربة جاهزة لتسجيل الدخول
| الدور | الاسم | الإيميل | ID |
|---|---|---|---|
| Management (CEO) | Omar El-Sayed | omar.elsayed@company.eg | 1 |
| Manager | Mona Hassan | mona.hassan@company.eg | 2 |
| Employee | Salma Ali | salma.ali@company.eg | 6 |

## هيكل المشروع
- `db.py` — الاتصال بقاعدة البيانات (Context Manager)
- `models.py` — كلاسات `Employee` و `Manager` (Inheritance, Property, Dunder Methods, Custom Exception)
- `repositories.py` — كل استعلامات SQL (Composition، Transactions)
- `auth.py` — تسجيل الدخول وتحديد الدور تلقائيًا
- `menus.py` — القوائم الثلاثة (Employee / Manager / Management Inquiries)
- `main.py` — نقطة التشغيل
