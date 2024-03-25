# Help Desk Ticketing System

# Start Date 25/03/2024
# Author Glen Radovan 20240837
# Completed date

# Here I have defined a class named Ticket that will encapsulate all the ticket-related functionalities.

class Ticket:
    counter = 0

    def __init__(self, staff_id, creator_name, contact_email, description):
        Ticket.counter += 1  # this increments the count by one when a new ticket is created
        self.ticket_number = Ticket.counter + 2000 # this starts the count at 2000
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"

# This next method (resolve_password_change) is used to handle password change requests for tickets
# If the description of the ticket contains "Password Change",  it generates a new password using
# the first two characters of the staff ID, concatenated with the first three characters of the
# creator's name

# I have used an f-string (which is a way to format strings), you can embed expressions inside curly
# braces {}, and they will be replaced with their values when the string is evaluated. This allows
# for easy interpolation of variables and expressions into strings. It's a concise and readable way
# to construct strings with dynamic content.

def resolve_password_change(self):
    if "password change" in self.description.lower():
        # Assuming contact_email contains the customer's email
        # Extracting the first part of the email as the basis for the new password
        customer_name = self.contact_email.split('@')[0]
        new_password = customer_name[:2].lower() + str(self.ticket_number)  # Generating new password
        self.response = f"New password generated: {new_password}"
        self.status = "Closed"

# In the next methods, respond() allows for updating the response of a ticket, while reopen() allows
# for reopening a closed ticket by changing its status to "Reopened"

    def respond(self, response):
        self.response = response

    def reopen(self):
        self.status = "Reopened"

    # The next method(print_ticket_info), is responsible for printing out all the information related to a ticket in a
    # structured format.

    def print_ticket_info(self):
        print(f"Ticket Number: {self.ticket_number}")
        print(f"Ticket Creator: {self.creator_name}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Email Address: {self.contact_email}")
        print(f"Description: {self.description}")
        print(f"Response: {self.response}")
        print(f"Ticket Status: {self.status}")

# The next method is defined as a static method(ticket_stats), within the Ticket class. It's purpose
# is to calculate ticket statistics, like how many have been created, resolved, and any open tickets,
# then returns a tuple containing the counts of created, resolved, and open tickets.

@staticmethod
def ticket_stats(tickets):
    created = len(tickets)
    resolved = sum(1 for ticket in tickets if ticket.status == "Closed")
    open_tickets = created - resolved
    return created, resolved, open_tickets

# here I have defined the Main class, in this method you will interact with the ticketing system.
class Main:
    @staticmethod
    def main():
        tickets = []
# The [] square brackets in this line create a new list object with no elements in it, so later in
# the code, this list can be used to store info of the Ticket class:

        #This piece prompts the user to create a ticket
        while True:
            create_more = input("Do you want to create a new ticket? (yes/no):")
            if create_more.lower() != "yes":  #this "lower()" ensures however the user types Yes, yEs,
                                             # or YES, it is converted to lowercase and remains case
                                             # sensitive"
                break
            new_ticket = Main.create_ticket_from_input()
            tickets.append(new_ticket)
        for ticket in tickets:
            ticket.resolve_password_change()

        Main.display_ticket_statistics(tickets)    #change statistics to Info?

        # Reopen one ticket and respond to another
        if tickets:  # Ensure there are tickets before performing actions
            tickets[0].reopen()  # Reopen the first ticket
            if len(tickets) > 1:
                tickets[1].respond("The monitor has been replaced.")

        #display updated ticket info
        Main.display_ticket_statistics(tickets)
        Main.print_tickets(tickets)

    @staticmethod
    def create_ticket_from_input():
        staff_id = input("Enter staff ID: ")
        creator_name = input("Enter ticket creator name: ")
        contact_email = input("Enter contact email: ")
        description = input("Enter description of the issue: ")
        return Ticket(staff_id, creator_name, contact_email, description)

    @staticmethod
    def display_ticket_statistics(tickets):
        created, resolved, open_tickets = Ticket.ticket_stats(tickets)
        print("\nDisplaying Ticket Statistics\n")
        print(f"Tickets Created: {created}")
        print(f"Tickets Resolved: {resolved}")
        print(f"Tickets To Solve: {open_tickets}\n")

    @staticmethod
    def print_tickets(tickets):
        print("Printing Tickets:\n")
        for ticket in tickets:
            ticket.print_ticket_info()
            print()


if __name__ == "__main__":
    Main.main()