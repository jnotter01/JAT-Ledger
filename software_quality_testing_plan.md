# Software Quality & Testing Plan

## 1. Testing Strategy Overview

JAT Ledger will use a structured testing process to make sure the application is reliable before deployment. The project will use a combination of unit testing, integration testing, system/end-to-end testing, and manual user testing. Unit tests will be used to verify small pieces of logic, such as financial calculations, form validation, and filtering. Integration tests will be used to make sure different parts of the application work together correctly, such as forms saving data to the database and reports pulling the correct transaction totals. End-to-end testing will be used to confirm that full user workflows work from start to finish.

The main testing tools will be Django’s built-in testing framework, Python’s `unittest` tools, and manual testing through the browser. During development, tests will be run before major commits and at the end of each sprint. Bugs found during testing will be documented in GitHub Issues or in a testing notes section of the repository.

Since this is a solo capstone project, the project owner is responsible for writing tests, running tests, documenting defects, and confirming that defects are resolved. Testing will be part of each sprint instead of being saved only for the end of the project. Each sprint should include time for building features, testing them, fixing defects, and documenting results.

---

## 2. Unit Test Plan

The following units are planned for unit testing. These focus on the most important parts of the system: transaction validation, financial calculations, filtering, and ownership/security checks.

### Unit 1: `get_total_income(transactions)`

**What it does:**  
Calculates the total amount of all income transactions from a list or queryset of transactions.

| Test Case | Input | Expected Output |
|---|---|---|
| Normal case | Income transactions of 750.00 and 100.00 | 850.00 |
| Multiple mixed transactions | Income transactions of 750.00 and 50.00, with expense transactions ignored | 800.00 |
| Edge case | No income transactions | 0.00 |

---

### Unit 2: `get_total_expenses(transactions)`

**What it does:**  
Calculates the total amount of all expense transactions from a list or queryset of transactions.

| Test Case | Input | Expected Output |
|---|---|---|
| Normal case | Expense transactions of 200.00 and 75.00 | 275.00 |
| Multiple mixed transactions | Expense transactions of 100.00 and 25.00, with income transactions ignored | 125.00 |
| Edge case | No expense transactions | 0.00 |

---

### Unit 3: `get_net_profit(total_income, total_expenses)`

**What it does:**  
Calculates net profit by subtracting total expenses from total income.

| Test Case | Input | Expected Output |
|---|---|---|
| Normal profit | Income: 1000.00, Expenses: 400.00 | 600.00 |
| Break-even | Income: 500.00, Expenses: 500.00 | 0.00 |
| Edge case | Income: 300.00, Expenses: 700.00 | -400.00 |

---

### Unit 4: `TransactionForm`

**What it does:**  
Validates transaction data before saving it to the database.

| Test Case | Input | Expected Output |
|---|---|---|
| Valid transaction | Property, category, income type, amount 750.00, valid date | Form is valid |
| Missing amount | Property, category, income type, blank amount, valid date | Form is invalid |
| Edge case | Amount is 0 or negative | Form is invalid |

---

### Unit 5: `filter_transactions_by_date(transactions, start_date, end_date)`

**What it does:**  
Filters transactions so reports can show results within a selected date range.

| Test Case | Input | Expected Output |
|---|---|---|
| Normal range | Transactions from January and February; filter January 1–31 | Only January transactions returned |
| Full range | Transactions from January through March; filter January 1–March 31 | All matching transactions returned |
| Edge case | Date range has no matching transactions | Empty result set |

---

### Unit 6: `get_property_summary(property)`

**What it does:**  
Creates a summary for one property, including total income, total expenses, and net profit.

| Test Case | Input | Expected Output |
|---|---|---|
| Normal case | Property with 1000.00 income and 300.00 expenses | Income: 1000.00, Expenses: 300.00, Net: 700.00 |
| Expense-only property | Property with no income and 200.00 expenses | Income: 0.00, Expenses: 200.00, Net: -200.00 |
| Edge case | Property with no transactions | Income: 0.00, Expenses: 0.00, Net: 0.00 |

---

### Planned Test File Location

Unit tests will be stored in:

```text
ledger/tests.py
```
---

## 3. Integration Test Plan

Integration testing will confirm that different parts of the application work together correctly.

### Integration Test 1: Transaction Form to Database

**Components being tested:**  
Transaction form, transaction view, Django model, and database.

**What is being validated:**  
The test will confirm that when a user submits a valid transaction form, the transaction is saved correctly in the database and connected to the correct user, property, and category.

**Expected Result:**  
A new transaction appears in the transaction list and is stored in the database with the correct amount, type, property, category, and date.

**Failure Scenario:**  
The transaction does not save because a required field is missing, the amount is invalid, or the property/category relationship is incorrect.

---

### Integration Test 2: Authentication and Protected Pages

**Components being tested:**  
Login system, user session, protected views, and page redirects.

**What is being validated:**  
The test will confirm that only logged-in users can access property, transaction, and report pages.

**Expected Result:**  
A logged-in user can access the dashboard, properties, transactions, and reports. A user who is not logged in is redirected to the login page.

**Failure Scenario:**  
An unauthenticated user is able to access private financial records, or a valid logged-in user is incorrectly blocked.

---

### Integration Test 3: Reports and Database Transactions

**Components being tested:**  
Database, transaction model, report service logic, and report template.

**What is being validated:**  
The test will confirm that reports correctly retrieve transactions from the database and calculate income, expenses, and net profit.

**Expected Result:**  
The report page displays accurate totals based on the transactions stored in the database.

**Failure Scenario:**  
The report shows incorrect totals, ignores transactions, includes another user’s transactions, or fails when no transactions exist.

---

### Integration Test 4: Property and Transaction Relationship

**Components being tested:**  
Property model, transaction model, transaction creation view, and database.

**What is being validated:**  
The test will confirm that every transaction is correctly connected to a valid property.

**Expected Result:**  
Transactions appear under the correct property, and property-specific reports only include that property’s transactions.

**Failure Scenario:**  
A transaction is saved without a property, linked to the wrong property, or appears in the wrong property report.

---

## 4. System / End-to-End Test Scenarios

### Scenario 1: User Creates a Property and Records Rent Income

**Step-by-Step Actions:**

1. User opens the JAT Ledger application.
2. User logs in with valid credentials.
3. User opens the property page.
4. User creates a new rental property with name, address, city, state, and zip code.
5. User opens the transaction page.
6. User creates a new income transaction for rent.
7. User selects the correct property and income category.
8. User enters the rent amount and transaction date.
9. User saves the transaction.
10. User opens the report summary page.

**Expected Outcome:**  
The property is created successfully. The rent transaction is saved successfully. The report page shows the rent amount as income and updates the net profit total.

**Possible Failure Points:**

- Login fails with correct credentials.
- Property form does not save required fields.
- Transaction form does not connect to the correct property.
- Report page does not include the new income transaction.
- Incorrect total is displayed.

---

### Scenario 2: User Records a Repair Expense and Reviews Net Profit

**Step-by-Step Actions:**

1. User logs in.
2. User confirms that at least one property exists.
3. User opens the transaction creation page.
4. User selects a property.
5. User selects an expense category such as Repairs.
6. User enters the repair cost.
7. User enters a transaction date and optional description.
8. User saves the expense transaction.
9. User opens the transaction list to verify the record.
10. User opens the summary report to review updated expenses and net profit.

**Expected Outcome:**  
The repair expense is saved and appears in the transaction list. The report page updates total expenses and subtracts the expense from net profit.

**Possible Failure Points:**

- Expense category is missing.
- Negative or invalid amount is accepted.
- Transaction saves but does not appear in the transaction list.
- Report page does not update after the expense is added.
- Net profit calculation is incorrect.

---

### Scenario 3: Invalid Transaction Entry Is Rejected

**Step-by-Step Actions:**

1. User logs in.
2. User opens the transaction creation page.
3. User selects a property and category.
4. User enters an invalid amount, such as 0 or a negative number.
5. User attempts to save the transaction.

**Expected Outcome:**  
The system rejects the transaction and displays a clear validation message. The invalid transaction is not saved to the database.

**Possible Failure Points:**

- Invalid amount is accepted.
- Error message is unclear.
- Transaction partially saves even though the form is invalid.
- User is redirected without knowing what went wrong.

---

## 5. Non-Functional Testing Considerations

### Performance Concerns

The application should load property lists, transaction lists, and reports quickly for a small rental business. Since the first version will likely have a limited number of properties and transactions, major performance issues are not expected. However, reports should still be tested with multiple properties and many transactions to make sure calculations remain fast and accurate.

### Security Concerns

The system stores business financial information, so access control is important. Users should not be able to view, edit, or delete records that do not belong to them. Pages that display financial information should require login. Password handling should rely on Django’s built-in authentication system instead of custom password storage.

### Input Validation

All forms should validate required fields, data types, and allowed values. Transaction amounts should be positive decimal values. Transaction type should only allow valid choices such as Income or Expense. Dates should be valid dates, and records should not save if required relationships such as property or category are missing.

### Error Handling

The system should provide clear error messages when forms are incomplete or invalid. Reports should not crash when there are no transactions. Missing records, invalid IDs, and permission problems should be handled with redirects, error pages, or user-friendly messages instead of unhandled server errors.

---

## 6. Defect Tracking Method

Bugs and defects will be tracked using GitHub Issues. Each bug report will include a short title, description of the problem, steps to reproduce, expected result, actual result, severity, and current status. Labels such as `bug`, `testing`, `high priority`, and `fixed` may be used to organize defects.

Defects will be documented in the project’s GitHub repository so that testing and fixes are connected to the same location as the code. Since this is a solo project, the project owner is responsible for creating issues, fixing bugs, updating issue status, and confirming that the defect has been resolved.

A typical defect record will include:

```text
Title: Transaction report shows incorrect net profit

Description:
The summary report does not subtract expenses correctly from income.

Steps to Reproduce:
1. Log in.
2. Create one income transaction for 1000.00.
3. Create one expense transaction for 250.00.
4. Open the summary report.

Expected Result:
Net profit should show 750.00.

Actual Result:
Net profit shows 1000.00.

Status:
Open

Resolution:
Pending
```
Before a defect is closed, the related feature will be retested to confirm that the problem no longer occurs.
