from dotenv import load_dotenv
import os

load_dotenv()

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("DB_PASSWORD"),
    database="applytrack"
)

cursor = db.cursor()

jobs = []

# Adds a new job application to the database
def add_job():
    company = input("Company name: ")
    while company.strip() == "":
        company = input("Company name: ")
    company = company.strip()

    role = input("Role: ")
    while role.strip() == "":
        role = input("Role: ")
    role = role.strip()
    
    status = "Applied"

    sql = "INSERT INTO jobs (company, role, status) VALUES (%s, %s, %s)"
    values = (company, role, status)

    cursor.execute(sql, values)
    db.commit()

    print(f"Added {role} at {company}!")

# Shows all saved job applications from the database
def view_jobs():
    cursor.execute("SELECT * FROM jobs")
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("No jobs added yet.")
        return

    for row in rows:
        print(f"{row[1]} - {row[2]} - {row[3]}")

# Updates the status of a job by matching the company name
def update_status():
    update_company = input("Enter the company name to update: ")
    new_status = input("Update the status: ")

    sql = "UPDATE jobs SET status = %s WHERE company = %s"
    values = (new_status, update_company)

    cursor.execute(sql, values)
    db.commit()

    if cursor.rowcount == 0:
        print("Company not found.")
    else:
        print(f"Updated {update_company} to {new_status}!")

# Shows only jobs that match a chosen status
def filter_by_status():
    filter_status = input("Filter by status (e.g. Applied, Interview, Rejected): ")

    sql = "SELECT * FROM jobs WHERE status = %s"
    values = (filter_status,)

    cursor.execute(sql, values)
    rows = cursor.fetchall()

    if len(rows) == 0:
        print(f"No jobs found with status '{filter_status}'.")
        return

    for row in rows:
        print(f"{row[1]} - {row[2]} - {row[3]}")

# Removes a job application by matching the company name
def delete_job():
    delete_company = input("Enter the company name to delete: ")

    sql = "DELETE FROM jobs WHERE company = %s"
    values = (delete_company,)

    cursor.execute(sql, values)
    db.commit()

    if cursor.rowcount == 0:
        print("Company not found.")
    else:
        print(f"Deleted {delete_company} from your list!")

#menu system
while True:
    print("\n1. Add job\n2. View jobs\n3. Update status\n4. Filter by status\n5. Delete job\n6. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_job()
    elif choice == "2":
        view_jobs()
    elif choice == "3":
        update_status()
    elif choice == "4":
        filter_by_status()
    elif choice == "5":
        delete_job()
    elif choice == "6":
        break
    else:
        print("Invalid choice, try again.")