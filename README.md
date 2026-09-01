# ApplyTrack

A simple command-line tool to track job and internship applications — built in pure Python, no external libraries.

## Why I built this

Job hunting means applying to many companies and losing track of who replied, who's still pending, and who rejected you. ApplyTrack keeps all of that organized in one place, right from the terminal.

## Features

- **Add** a new job application (company, role, status)
- **View** all saved applications
- **Update** the status of any application (e.g. applied → interview → rejected)
- **Filter** applications by status
- **Persistent storage** — your data is saved to a file and automatically reloaded the next time you run the program
- **Input validation** — the program won't let you save empty/blank entries

## How to run it

1. Make sure you have Python 3 installed
2. Clone this repository
3. Run the file:
   ```
   python applytrack.py
   ```
4. Follow the on-screen menu to add, view, update, or filter your applications

## What I learned building this

- Working with Python data structures (lists and dictionaries) to model real data
- Writing modular code using functions
- File handling — reading from and writing to files so data persists between runs
- Basic input validation and loop control (`while` loops, flags)

## Possible future improvements

- Switch data storage to JSON for more reliable structure
- Add a "response rate" statistic
- Add the ability to delete an application

---

Built by Uzma Shafi
