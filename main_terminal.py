"""
main.py
--------
Entry point of the Hostel Room Allocation System (Terminal Version).
Run this file to start the application:

    python main.py

No GUI library is required - this is a pure terminal (command-line)
application. You interact with it by typing menu numbers and pressing Enter.
"""

from database.db_setup import initialize_database
from interface.student_menu import student_menu
from interface.room_menu import room_menu
from interface.allocation_menu import allocation_menu
from interface.view_allocations_menu import view_allocations_menu


def main_menu():
    """The main dashboard menu loop. This is the first thing the user sees."""
    while True:
        print("\n==========================================")
        print("   HOSTEL ROOM ALLOCATION SYSTEM")
        print("==========================================")
        print("1. Student Management")
        print("2. Room Management")
        print("3. Room Allocation")
        print("4. View Allocations")
        print("5. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            student_menu()
        elif choice == "2":
            room_menu()
        elif choice == "3":
            allocation_menu()
        elif choice == "4":
            view_allocations_menu()
        elif choice == "5":
            print("Exiting Hostel Room Allocation System. Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    # Step 1: Make sure the database and all tables exist
    initialize_database()

    # Step 2: Start the terminal menu loop
    main_menu()
