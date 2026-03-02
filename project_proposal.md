# Johnny Apple Trees Ledger  
## Capstone Project Proposal – Milestone 1

**Student:** John Notter  
**Repository:** JAT-Ledger  
**Project Type:** Full-Stack Web Application  

---

# 1. Problem Definition & Objectives

## Problem Statement

Small property owners and independent landlords often rely on spreadsheets or generic accounting tools to manage rental income, expenses, and tenant records. These tools are not specifically designed for property-level financial tracking and often lack structured reporting, tenant workflow organization, and centralized data management.

Johnny Apple Trees LLC requires a dedicated system to track rental property performance, organize tenant information, and calculate profitability in a structured and scalable way.

## Project Objective

The Johnny Apple Trees Ledger will be a full-stack web application designed to:

- Manage multiple rental properties
- Track rental income and operational expenses
- Store tenant information and payment history
- Calculate property-level profitability
- Generate financial summaries and reports

## Measurable Outcomes

By the end of the semester, the application will:

- Support authenticated user access
- Persist all financial and tenant data in a relational database
- Implement business logic to calculate:
  - Net operating income
  - Monthly cash flow
  - Expense categorization totals
- Provide reporting views beyond basic CRUD functionality
- Demonstrate use of data structures and algorithmic logic for sorting, filtering, and aggregating financial data

---

# 2. Scope & Feasibility

## In Scope

The application will include:

- User authentication system
- Property management module
- Tenant management module
- Income tracking functionality
- Expense tracking functionality
- Financial dashboard with reporting summaries
- RESTful API layer
- Database persistence
- Documented testing

## Out of Scope

The following features will not be included in this semester project:

- Direct bank integrations
- Automated tax filing
- Mobile-native application
- Multi-organization SaaS scaling

## Feasibility

The project scope is realistic for a single developer over one semester. The system focuses on core functionality required to manage rental property finances without introducing unnecessary complexity. Development will follow an iterative approach to ensure manageable progress and timely completion.

---

# 3. Technology Stack Selection

## Architecture

The system will follow a layered client-server architecture:

- Front-End (Client Interface)
- API Layer
- Business Logic Layer
- Database Layer

This architecture ensures separation of concerns, maintainability, and scalability.

## Technologies

### Front-End
- React.js
- HTML5 / CSS3

React enables a dynamic and component-based user interface suitable for dashboards and reporting tools.

### Back-End
- Node.js with Express.js

Express provides a structured environment for building RESTful APIs and implementing business logic.

### Database
- PostgreSQL

PostgreSQL is a relational database management system well-suited for structured financial data and complex queries.

### Version Control
- Git and GitHub

GitHub will be used to maintain version history and demonstrate iterative development.

---

# 4. Project Plan & Timeline

Development will follow an iterative sprint-based model.

## Phase 1 – Planning & Design
- Finalize requirements
- Design database schema
- Establish project structure
- Create architecture outline

## Phase 2 – Backend Development
- Implement database models
- Build API endpoints
- Develop business logic for financial calculations

## Phase 3 – Frontend Development
- Build dashboard interface
- Implement forms for transactions and tenants
- Integrate frontend with backend APIs

## Phase 4 – Testing & Refinement
- Unit testing
- API testing
- Bug fixes
- Performance improvements
- Documentation updates

---

# 5. Collaboration & Feedback Plan (Solo Development)

This project is being developed by a single student. The developer will assume responsibility for architecture, backend, frontend, database design, and testing.

To meet collaboration requirements:

- Structured feedback will be gathered from at least two external users.
- Instructor feedback will be incorporated during milestone reviews.
- Documented design adjustments will demonstrate how feedback influenced the final implementation.

---

# 6. Success Criteria

The project will be considered successful if:

- The application runs reliably.
- All core features are implemented.
- Financial calculations are accurate.
- Data persists correctly in the database.
- Testing activities are documented.
- The final presentation clearly demonstrates functionality and system design.

---

# Conclusion

The Johnny Apple Trees Ledger addresses a real-world property management need through a structured full-stack application. The scope is appropriate for a semester-long capstone and demonstrates core computer science concepts including database management, API development, business logic implementation, and iterative software development practices.
