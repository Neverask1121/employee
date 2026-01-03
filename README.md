# Employee Data Management System

A simple, database-driven **Employee Data Management System** built to practice backend development, CRUD operations, and real-world data handling using Flask and SQLite.

This project focuses on **clean logic**, **data validation**, and **practical full‑stack flow** rather than fancy UI.

---

## Why this project?

Almost every real application deals with structured data like users or employees. This project was built to understand:

* How data is stored and retrieved from a database
* How forms interact with backend logic
* Input validation and error handling
* Structuring a Flask application properly

This is a **foundational backend project** that mirrors real internal tools used in companies.

---

## Features

* Add employee details through a form
* Store employee data in a database
* Display stored employee records
* Input validation on server-side
* Persistent data storage using SQLite
* Clean and minimal UI

---

## Tech Stack

**Backend**

* Python
* Flask

**Database**

* SQLite (sqlite3)

**Frontend**

* HTML
* CSS
* JavaScript
* Jinja Templates

**Version Control / Deployment**

* Git & GitHub

---

## Project Structure

```
employee-data-system/
│
├── app.py
├── database.db
├── templates/
│   ├── index.html
│   └── layout.html
├── static/
│   ├── styles.css
│   └── script.js
└── README.md
```

---

## Data Fields

Each employee record contains:

* Employee ID
* Name
* Date of Birth
* Email

All fields are validated before insertion into the database.

---

## How it works (High-level)

1. User submits employee details via the form
2. Backend validates each input
3. Valid data is inserted into the SQLite database
4. Stored employee records are fetched and displayed
5. Data persists across server restarts

---

## Validation Logic

* Employee ID must be a valid integer
* Required fields cannot be empty
* Email format is checked before insertion

This prevents bad or malformed data from entering the database.

---

## Setup Instructions

Clone the repository:

```bash
git clone https://github.com/neverask1121/employee.git
cd employee
```

Install dependencies:

```bash
pip install flask
```

Run the application:

```bash
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000
```

---

## What I Learned

* CRUD-style backend logic
* SQLite database integration with Flask
* Handling form submissions securely
* Server-side validation
* Jinja templating and dynamic rendering

---

## Future Improvements

* Edit and delete employee records
* Search and filter functionality
* Pagination for large datasets
* User authentication
* Deployment with environment variables

---

## Disclaimer

This project is built for **learning and demonstration purposes**.
It is not intended for production use.

---

## Author

**Adi**
Student | Aspiring Software Engineer
Focused on backend development, databases, and real-world problem solving

---

Feedback is welcome. Every project here is a step forward.
