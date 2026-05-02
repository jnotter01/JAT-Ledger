# JAT Ledger

JAT Ledger is a full-stack rental property management and financial tracking system built for Johnny Apple Trees LLC. The purpose of the application is to help authorized internal users track rental properties, income, expenses, transaction categories, and basic financial summaries in one organized system.

This application is intended for business staff or managers, not tenants/customers. Users of the system are people responsible for managing the rental property ledger.

---

## Project Purpose

Johnny Apple Trees needs a simple way to organize rental property financial records. Instead of tracking rental income and repair expenses manually, JAT Ledger provides a database-backed web application where authorized users can create properties, define income/expense categories, record transactions, and view summary reports.

The project demonstrates a real-world full-stack application with front-end pages, back-end logic, database persistence, form validation, authentication, testing, and version control.

---

## Current Features

- User signup, login, and logout
- Dashboard with getting-started guidance
- User-specific property records
- User-specific income and expense categories
- Create, view, edit, and delete transactions
- Transaction amount validation
- Validation for category/type matching
- Summary report showing:
  - Total income
  - Total expenses
  - Net profit
- Summary report filters by:
  - Property
  - Start date
  - End date
- New-user setup guard before adding transactions
- Django admin access for administrative review
- Automated tests for service logic, form validation, and access control

---

## Technology Stack

- Python
- Django
- SQLite for development database
- HTML / CSS through Django templates
- Git and GitHub for version control

---

## Application Architecture

JAT Ledger follows a layered Django architecture:

- **Templates:** Front-end display and page layout
- **Views:** Request handling and page routing
- **Forms:** Input validation and form processing
- **Models:** Database structure for properties, categories, and transactions
- **Services:** Business logic, such as financial summary calculations
- **Database:** Persistent storage for application records

This separation helps keep the project maintainable by preventing display logic, database logic, validation, and business calculations from being mixed together.

---

## Main Models

### Property

Stores rental property information, including name, address, city, state, ZIP code, active status, and owner/user relationship.

### Category

Stores transaction categories such as Rent, Repairs, Maintenance, Service Fees, or other income/expense categories.

### Transaction

Stores income and expense records. Each transaction belongs to a user, property, and category. Transactions include type, amount, description, and date.

---

## Business Logic

The main business logic currently calculates financial summary data from transaction records.

The summary report calculates:

```text
Net Profit = Total Income - Total Expenses
