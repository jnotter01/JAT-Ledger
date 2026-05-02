# Milestone 3: Final Product, Presentation, and Documentation

## Project Name

JAT Ledger

## Group Members

- John Notter

---

## Project Overview

JAT Ledger is a full-stack rental property ledger application built for Johnny Apple Trees LLC. The purpose of the application is to help authorized internal users track rental properties, income, expenses, transaction categories, and financial summaries in one organized system.

This application is intended for business staff or managers, not tenants or customers. Users can create properties, create categories, record transactions, edit or delete transactions, and review financial summaries.

---

## Documentation Link

Project documentation is available in the GitHub repository:

https://github.com/jnotter01/JAT-Ledger

Main documentation file:

https://github.com/jnotter01/JAT-Ledger/blob/main/README.md

Additional project documentation includes:

- `system_architecture.md`
- `software_quality_testing_plan.md`
- `structured_code_review_quality_audit.md`
- `Milestone2.md`
- `milestone_3.md`

---

## Public Project Link

The deployed application is available here:

https://jnotter.pythonanywhere.com

The application will remain publicly available through finals week so other students can interact with it.

---

## Demo Video Link

Final demo video link:

youtube.com/datsatoilet

The video demonstrates the project overview, current functionality, documentation, public deployment, transaction workflow, summary reporting, validation, and testing progress.

---

## Final Implemented Features

The final version of JAT Ledger includes the following working features:

- User signup, login, and logout
- Dashboard with getting-started guidance
- User-specific property records
- User-specific income and expense categories
- User-facing property management
- User-facing category management
- Transaction creation
- Transaction editing
- Transaction deletion
- Transaction list view
- Transaction amount validation
- Category/type validation
- New-user setup guard before adding transactions
- Summary report showing:
  - Total income
  - Total expenses
  - Net profit
- Summary report filters by:
  - Property
  - Start date
  - End date
- Django admin access for administrative review
- Automated tests for service logic, form validation, and access control
- Public deployment through PythonAnywhere

---

## Technical Stack

JAT Ledger was built using:

- Python
- Django
- SQLite
- HTML and CSS through Django templates
- Git and GitHub
- PythonAnywhere for public deployment

---

## Architecture Summary

JAT Ledger follows a layered Django architecture.

- **Templates** handle front-end display and page layout.
- **Views** handle requests, routing, and responses.
- **Forms** handle input validation.
- **Models** define the database structure.
- **Services** contain business logic, such as summary calculations.
- **Database** stores user, property, category, and transaction data.

This structure helps keep the project maintainable because display logic, request handling, validation, business logic, and database structure are separated into different files.

---

## Database and Back-End Progress

The project includes three main custom data models:

### Property

Stores rental property information such as name, address, city, state, ZIP code, active status, and the user who owns the record.

### Category

Stores income and expense categories such as Rent, Repairs, Maintenance, Fees, or other transaction types.

### Transaction

Stores financial records. Each transaction belongs to a user, property, and category. Transactions include type, amount, description, and date.

The back-end supports data creation, retrieval, editing, deletion, validation, and reporting.

---

## Business Logic

The main business logic is the summary report. The application calculates:

```text
Net Profit = Total Income - Total Expenses
```

The summary report can also be filtered by property and date range. This allows users to review financial activity for a specific rental property or reporting period.

This goes beyond basic CRUD because the application processes transaction records and converts them into useful financial totals.

---

## Testing and Quality Assurance

Automated tests were added using Django’s testing framework.

The test suite covers:

- Summary calculation logic
- Empty transaction summary behavior
- Transaction form validation
- Valid transaction form submission
- Login protection for protected pages
- Setup guard for users without properties or categories

The tests were run locally using:

```bash
python manage.py test
```

The test suite passed successfully.

Manual testing was also completed by creating user accounts, adding properties, adding categories, creating transactions, editing transactions, deleting transactions, filtering reports, and testing the deployed public version on PythonAnywhere.

---

## Code Review and Quality Improvements

A structured self-review was completed because this is a solo project. The review focused on:

- Correctness
- Architecture alignment
- Readability and maintainability
- Security and validation
- Performance considerations

Important improvements made after review included:

1. Moving summary calculation logic out of `views.py` and into `services.py`.
2. Adding transaction amount validation.
3. Filtering user-owned data by the logged-in user.
4. Adding setup guidance for new users.
5. Adding automated tests.

---

## Deployment Summary

The application was deployed publicly using PythonAnywhere.

Deployment work included:

- Cloning the GitHub repository to PythonAnywhere
- Creating a virtual environment
- Installing dependencies from `requirements.txt`
- Applying database migrations
- Creating a deployed database
- Running `collectstatic`
- Configuring the WSGI file
- Configuring static files
- Updating allowed hosts and CSRF trusted origins
- Testing the public deployment

The deployed app was tested successfully by creating a new account and using the main application features.

---

## Reflection

This project helped demonstrate the full software development lifecycle from planning through deployment. Earlier milestones focused on requirements, architecture, testing plans, and code review. The final milestone required turning that planning into a functional deployed application.

The most important technical progress was building a working Django application with database-backed records, authentication, validation, transaction management, summary reporting, and deployment. The project also showed the importance of testing and code review because several improvements came from reviewing the structure and testing user workflows.

One challenge was deployment. The application worked locally, but deployment required additional configuration for allowed hosts, static files, WSGI settings, and CSRF trusted origins. Fixing those issues helped show the difference between local development and public deployment.

If the project continued, the next improvements would be better styling, role-based permissions, receipt uploads, charts, exportable reports, and more advanced property-specific dashboards.

---

## Final Status

JAT Ledger is functional and publicly available. It meets the main goals of the capstone project by providing a full-stack application with front-end pages, back-end logic, database persistence, business logic, authentication, testing, documentation, version control, and public deployment.
