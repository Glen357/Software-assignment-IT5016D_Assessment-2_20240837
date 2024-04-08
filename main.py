# Help Desk Ticketing System

# Start Date 25/03/2024
# deleted+restarted date 28/03/2024

# Author Glen Radovan 20240837

# Completed date

import itertools


class Ticket:
    # Class variable to generate unique ticket numbers
    ticket_counter = itertools.count(start=2001)
    all_tickets = []

    def __init__(self, staff_id, creator_name, contact_email, description):
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description
        self.ticket_number = next(Ticket.ticket_counter)
        self.response = "Not Yet Provided"  # Placeholder for response
        self.status = "Open"  # Initial status of the ticket
        Ticket.all_tickets.append(self)

    def submit_ticket(self):
        print("Ticket submitted successfully.")
        print(f"Ticket number: {self.ticket_number}")
        print(f"Name: {self.creator_name}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Email Address: {self.contact_email}")
        print(f"Description: {self.description}")
        print(f"Response: {self.response}")
        print(f"Status: {self.status}")

    def respond_to_ticket(self, feedback):
        self.response = feedback
        print("Response added successfully.")

    def resolve_password_change(self):
        if "password change" in self.description.lower():
            # Generate the new password, The first two characters of the staffID, followed by
            # the first three characters of the ticket creator name.
            new_password = f"{self.staff_id[:2]}{self.creator_name[:3]}"
            # Set the response to include the new password
            self.response = f"New password generated: {new_password}"
            print("Password change resolved successfully.")

    def reopen_ticket(self, new_description=None, new_contact_email=None):
        self.status = "Reopened"
        if new_description:
            self.description = new_description


    def display_ticket_info(self):
        print("Ticket Information:")
        print(f"Ticket Number: {self.ticket_number}")
        print(f"Name: {self.creator_name}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Email Address: {self.contact_email}")
        print(f"Description: {self.description}")
        print(f"Response: {self.response}")
        print(f"Status: {self.status}")
        if "password change" in self.description.lower() and "new password generated" in self.response.lower():
            print(f"New Password: {self.response.split(':')[-1].strip()}")  # Extract and display the new password

    @staticmethod
    def display_ticket_statistics(ticket_list):
        total_tickets = len(ticket_list)
        resolved_tickets = sum(1 for ticket in ticket_list if ticket.status == "Closed")
        open_tickets = total_tickets - resolved_tickets

        print("Ticket Statistics:")
        print(f"Tickets Created: {total_tickets}")
        print(f"Tickets Resolved: {resolved_tickets}")
        print(f"Tickets To Solve: {open_tickets}")


def create_ticket():
    # Function to create a new ticket based on user input
    staff_id = input("Enter Staff ID: ")
    creator_name = input("Enter Creator Name: ")
    contact_email = input("Enter Contact Email: ")
    description = input("Enter Description: ")
    new_ticket = Ticket(staff_id, creator_name, contact_email, description)
    print(f"Ticket {new_ticket.ticket_number} created successfully!")  # Display ticket number
    if "password change" in description.lower():
        new_ticket.resolve_password_change()


def reopen_ticket():
    # Function to reopen a ticket
    ticket_number = int(input("Enter the ticket number to reopen: "))
    for ticket in Ticket.all_tickets:
        if ticket.ticket_number == ticket_number:
            print("Ticket found:")
            ticket.display_ticket_info()
            new_description = input("Enter new description (leave empty to keep current): ")
            ticket.reopen_ticket(new_description)
            print("Ticket reopened successfully.")
            return
    print("Ticket not found.")


def display_menu():
    print("\n===== Help Desk Ticketing System =====")
    print("1. Create a New Ticket")
    print("2. Reopen a Ticket")
    print("3. Display Ticket Statistics")
    print("4. Exit")


# Example usage
while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        create_ticket()
    elif choice == "2":
        reopen_ticket()
    elif choice == "3":
        Ticket.display_ticket_statistics(Ticket.all_tickets)
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
