# Help Desk Ticketing System

# Start Date 25/03/2024

# Author Glen Radovan 20240837

# Completed date

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


class Ticket:
    created_tickets = 0
    resolved_tickets = 0
    open_tickets = 0

    def __init__(self, staff_id, ticket_creator_name, contact_email, description):
        self.ticket_number = Ticket.created_tickets + 2001
        self.staff_id = staff_id
        self.ticket_creator_name = ticket_creator_name
        self.contact_email = contact_email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"
        Ticket.created_tickets += 1
        Ticket.open_tickets += 1

    def resolve_password_change(self):
        if "password change" in self.description.lower():
            new_password = self.staff_id[:2] + self.ticket_creator_name[:3]
            self.response = f"New password generated: {new_password}"
            self.status = "Closed"
            Ticket.resolved_tickets += 1
            Ticket.open_tickets -= 1

    def provide_response(self, response):
        self.response = response
        self.status = "Closed"
        Ticket.resolved_tickets += 1
        Ticket.open_tickets -= 1

    @staticmethod
    def get_ticket_stats():
        return {
            "Tickets Created": Ticket.created_tickets,
            "Tickets Resolved": Ticket.resolved_tickets,
            "Tickets To Solve": Ticket.open_tickets
        }

    def print_ticket_info(self):
        print("Ticket Number:", self.ticket_number)
        print("Ticket Creator:", self.ticket_creator_name)
        print("Staff ID:", self.staff_id)
        print("Email Address:", self.contact_email)
        print("Description:", self.description)
        print("Response:", self.response)
        print("Ticket Status:", self.status)
        print()


class Main:
    @staticmethod
    def submit_ticket():
        print("Submit Ticket")
        print("1. Enter Details")
        print("2. Use Predefined Details")
        choice = input("Enter your choice: ")

        if choice == "1":
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            staff_id = input("Staff ID: ")
            ticket_creator_name = first_name + " " + last_name
        elif choice == "2":
            # Use predefined details from environment variables
            staff_id = os.getenv("PREDEFINED_STAFF_ID")
            ticket_creator_name = os.getenv("PREDEFINED_TICKET_CREATOR_NAME")
            if staff_id is None or ticket_creator_name is None:
                print("Predefined staff ID or ticket creator name not found in .env file.")
                return
        else:
            print("Invalid choice.")
            return

        contact_email = input("Contact Email: ")
        description = input("Description of the Issue: ")

        new_ticket = Ticket(staff_id, ticket_creator_name, contact_email, description)
        new_ticket.resolve_password_change()  # Check if it's a password change request
        new_ticket.print_ticket_info()

    @staticmethod
    def respond_to_ticket(tickets):
        ticket_number = int(input("Enter the ticket number to respond to: "))
        response = input("Enter response: ")
        for ticket in tickets:
            if ticket.ticket_number == ticket_number:
                ticket.provide_response(response)
                ticket.print_ticket_info()
                break
        else:
            print("Ticket not found.")

    @staticmethod
    def reopen_ticket(tickets):
        ticket_number = int(input("Enter the ticket number to reopen: "))
        for ticket in tickets:
            if ticket.ticket_number == ticket_number:
                ticket.status = "Reopened"
                Ticket.open_tickets += 1
                Ticket.resolved_tickets -= 1
                ticket.print_ticket_info()
                break
        else:
            print("Ticket not found.")

    @staticmethod
    def display_ticket_statistics():
        stats = Ticket.get_ticket_stats()
        print("\nDisplaying Ticket Statistics\n")
        for key, value in stats.items():
            print(f"{key}: {value}")
        print()

    @staticmethod
    def main():
        tickets = []

        while True:
            print("1. Submit Ticket")
            print("2. Respond to Ticket")
            print("3. Reopen Ticket")
            print("4. Display Ticket Statistics")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                Main.submit_ticket()
            elif choice == "2":
                Main.respond_to_ticket(tickets)
            elif choice == "3":
                Main.reopen_ticket(tickets)
            elif choice == "4":
                Main.display_ticket_statistics()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    Main.main()
