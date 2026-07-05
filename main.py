"""
main.py
--------
Entry point of the Hostel Room Allocation System (Desktop GUI Version).
Run this file to start the application:

    python main.py

This opens a Tkinter desktop window (Dashboard). Tkinter is part of core
Python, so nothing extra needs to be installed.

Note: A terminal (text-menu) version is also included as main_terminal.py
in case you ever need it - both use the same database, models, and
algorithm code, only the front end is different.
"""

from database.db_setup import initialize_database
from gui.dashboard import run_app


if __name__ == "__main__":
    # Step 1: Make sure the database and all tables exist
    initialize_database()

    # Step 2: Launch the Tkinter desktop application
    run_app()
