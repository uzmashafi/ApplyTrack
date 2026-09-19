# ApplyTrack

A command-line tool to track job and internship applications — built in Python, backed by a real MySQL database.

## Why I built this

Job hunting means applying to many companies and losing track of who replied, who's still pending, and who rejected you. ApplyTrack keeps all of that organized in one place, right from the terminal.

## Features

- **Add** a new job application (company, role, status)
- **View** all saved applications
- **Update** the status of any application (e.g. applied → interview → rejected)
- **Filter** applications by status
- **Delete** an application
- **MySQL database** for persistent, reliable storage — no data lost between runs
- **Input validation** — the program won't let you save empty/blank entries, and matching is case- and whitespace-insensitive (e.g. "Google" and "  google " are treated the same)

## How to run it

1. Make sure you have Python 3 and MySQL installed and running
2. Clone this repository
3. Create the database and table:
   ```sql
   CREATE DATABASE applytrack;
   USE applytrack;

   CREATE TABLE jobs (
       id INT AUTO_INCREMENT PRIMARY KEY,
       company VARCHAR(100),
       role VARCHAR(100),
       status VARCHAR(50)
   );
   ```
4. Install dependencies:
   ```
   pip install mysql-connector-python python-dotenv
   ```
5. Create a `.env` file in the project folder (see `.env.example`) and add your MySQL password:
   ```
   DB_PASSWORD=your_mysql_password_here
   ```
6. Run the file:
   ```
   python applytrack.py
   ```
7. Follow the on-screen menu to add, view, update, filter, or delete your applications

## What I learned building this

- Working with Python data structures (lists and dictionaries) to model real data
- Writing modular code using functions
- File handling — reading from and writing to files so data persists between runs
- SQL fundamentals — `INSERT`, `SELECT`, `UPDATE`, `DELETE`, and using `WHERE` to target specific rows
- Connecting a Python program to a real MySQL database using `mysql-connector-python`
- Keeping sensitive data (like database passwords) out of source code using environment variables
- Basic input validation and loop control (`while` loops)

## Possible future improvements

- Add a "response rate" statistic
- Build a simple web interface using Flask

---

Built by Uzma Shafi
