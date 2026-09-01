jobs = []

# Adds a new job application to the list
def add_job():
    company = input("Company name: ")
    while company == "":
        company = input("Company name: ")

    role = input("Role: ")
    while role == "":
        role = input("Role: ")
    
    status = "applied"

    job = {
        "company": company,
        "role": role,
        "status": status
    }

    jobs.append(job)
    print(f"Added {role} at {company}!")

# Shows all saved job applications
def view_jobs():
    if len(jobs) == 0:
        print("No jobs added yet.")
        return

    for job in jobs:
        print(f"{job['company']} - {job['role']} - {job['status']}")

# Updates the status of a job by matching the company name
def update_status():
    update_company = input("Enter the company name to update: ")
    found = False

    for job in jobs:
        if update_company == job['company']:
            new_status = input("Update the status: ")
            while new_status == "":
                new_status = input("Update the status: ")
            
            job['status'] = new_status
            print(f"Updated {job['company']} to {new_status}!")
            found = True

    if not found:
        print("Company not found.")

# Shows only jobs that match a chosen status
def filter_by_status():
    filter_status = input("Filter by status (e.g. applied, interview, rejected): ")
    found = False

    for job in jobs:
        if filter_status == job['status']:
            print(f"{job['company']} - {job['role']} - {job['status']}")
            found = True

    if not found:
        print(f"No jobs found with status '{filter_status}'.")

# Saves all jobs to a text file(so they aren't lost)
def save_jobs():
    file = open("jobs.txt", "w")

    for job in jobs:
        file.write(f"{job['company']} - {job['role']} - {job['status']}\n")

    file.close()

# Loads previously saved jobs back into the program when it starts
def load_jobs():
    file = open("jobs.txt", "r")
    content = file.read()
    file.close()

    lines = content.splitlines()

    for line in lines:
        parts = line.split(" - ")
        job = {
            "company": parts[0],
            "role": parts[1],
            "status": parts[2]
        }
        jobs.append(job)

load_jobs()

#menu system
while True:
    print("\n1. Add job\n2. View jobs\n3. Update status\n4. Filter by status\n5. Exit")
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
        save_jobs()
        break
    else:
        print("Invalid choice, try again.")




