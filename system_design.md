# System Design
## Johnny Apple Trees Ledger

## 1. System Overview

Johnny Apple Trees Ledger will be a web-based application designed to manage rental property financial data. The system will allow users to track properties, record income and expenses, and generate financial summaries.

The application will follow a standard full-stack architecture, separating the user interface, application logic, and data storage.

---

## 2. System Architecture

The system will use a three-layer architecture:

- **Presentation Layer (Frontend)**  
  Handles user interaction through web pages. Users will input and view data through forms and tables.

- **Application Layer (Backend)**  
  Processes user requests, applies business logic, and communicates with the database.

- **Data Layer (Database)**  
  Stores all property, income, and expense data.

---

## 3. Technologies

The following technologies will be used:

- **Programming Language:** Python  
- **Web Framework:** Django  
- **Frontend:** HTML, CSS  
- **Database:** SQLite (development), with potential for PostgreSQL in future versions  
- **Version Control:** Git and GitHub  

---

## 4. Data Design (Models)

### Property
- property_id
- address
- purchase_price
- notes

### Transaction
- transaction_id
- property_id (foreign key)
- type (income or expense)
- category
- amount
- date
- description

### Category
- category_id
- name
- type (income or expense)

---

## 5. System Workflow

1. The user logs into the system (future feature).
2. The user creates or selects a property.
3. The user enters income or expense data.
4. The backend processes the request and stores it in the database.
5. The system updates totals and summaries.
6. The user views ledger entries and financial summaries.

## 6. Diagram

```
[ User ]
   |
   v
[ Frontend (HTML/CSS) ]
   |
   v
[ Backend (Django Application) ]
   |
   v
[ Database (SQLite) ]
   |
   v
[ Reports / Summaries ]
```

## 7. Design Considerations

The system is designed to be simple and easy to expand. Future improvements may include:

- User authentication and roles
- Data visualization (charts and graphs)
- Exporting financial reports
- Cloud database integration

The design prioritizes clarity, maintainability, and scalability for future development.
