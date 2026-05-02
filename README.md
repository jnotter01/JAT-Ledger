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
```

The summary can also be filtered by property and date range, allowing users to review specific financial periods or rental units.

---

## Local Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/jnotter01/JAT-Ledger.git
cd JAT-Ledger
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

On Windows PowerShell:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

---

## How to Use the App

1. Create an account or log in.
2. Add at least one rental property.
3. Add at least one transaction category, such as Rent or Repairs.
4. Add income or expense transactions.
5. View transactions in the transaction list.
6. Edit or delete transactions if needed.
7. Open the summary report to view total income, total expenses, and net profit.
8. Use report filters to view summaries by property or date range.

---

## Testing

The project includes automated tests for key features.

To run the test suite:

```bash
python manage.py test
```

Current tests cover:

- Summary calculation logic
- Empty transaction summary behavior
- Transaction form validation
- Valid transaction form submission
- Login protection for protected pages
- Setup guard for users without properties or categories

The test suite has been run locally and passes.

---

## Version Control

This project is maintained using Git and GitHub. The repository includes commits for:

- Project planning documentation
- System architecture documentation
- Software quality and testing plan
- Structured code review and quality audit
- Django project setup
- Data models
- User-facing property management
- User-facing category management
- Transaction create/edit/delete functionality
- Summary report filters
- Login/logout/signup pages
- Automated tests

---

## Current Limitations

The current version is functional but still has room for improvement. Current limitations include:

- Styling is simple and not fully polished
- SQLite is currently used for development
- User roles are not yet separated into admin, manager, or read-only roles
- Reports are basic and do not yet include charts or downloadable exports
- No receipt/image upload feature yet
- Deployment configuration may need adjustment depending on the hosting platform

---

## Future Improvements

Planned improvements include:

- Improve responsive UI styling
- Add role-based permissions for owner, manager, and read-only users
- Add property-specific dashboards
- Add charts for income, expenses, and net profit
- Add receipt upload support
- Add export options for reports
- Add more automated tests
- Collect external user feedback and document changes based on that feedback

---

## Project Status

JAT Ledger currently has a working Django application with authentication, database-backed records, transaction management, summary reporting, validation, filtering, and automated tests. The project is ready for final documentation, deployment, and final demonstration.
