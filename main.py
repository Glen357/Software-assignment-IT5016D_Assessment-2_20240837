# Help Desk Ticketing System

# Start Date 25/03/2024

# Author Glen Radovan 20240837

# Completed date


class Ticket:
    counter = 0

    def __init__(self, team_member_name, team_member_login, customer_name, email_address, login_code, password,
                 description):
        Ticket.counter += 1
        self.ticket_number = Ticket.counter + 2000
        self.team_member_name = team_member_name
        self.team_member_login = team_member_login
        self.customer_name = customer_name
        self.email_address = email_address
        self.login_code = login_code
        self.password = password
        self.description = description
        self.solution_description = None
        self.issue_rectified = False

    def print_ticket_info(self):
        print("Ticket Details:")
        print(f"Ticket Number: {self.ticket_number}")
        print(f"Team Member Name: {self.team_member_name}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Email Address: {self.email_address}")
        print(f"Login Code: {self.login_code}")
        print(f"Password: {self.password}")
        print(f"Description: {self.description}")
        if self.solution_description:
            print(f"Solution Description: {self.solution_description}")

        # Display "Issue Rectified" only if the issue has been rectified
        if self.issue_rectified:
            print(f"Issue Rectified: {'Yes' if self.issue_rectified else 'No'}")

    def resolve_password_change(self):
        if "password change" in self.description.lower():
            self.login_code = self.customer_name[:3] + str(self.ticket_number)[-2:].zfill(2)
            self.password = self.login_code

    def provide_solution(self, solution_description):
        self.solution_description = solution_description

    def rectify_issue(self):
        self.issue_rectified = True


class Main:
    @staticmethod
    def main():
        tickets = []

        while True:
            team_member_name = input("Team member name: ").capitalize()
            team_member_login = input("Team member login: ").lower()
            search_option = input("Search? (yes/no): ").lower()

            if search_option == "yes":
                ticket_number_input = input("Enter ticket number to reopen: ")
                if ticket_number_input:
                    ticket_number = int(ticket_number_input)
                    found_ticket = None
                    for ticket in tickets:
                        if ticket.ticket_number == ticket_number:
                            found_ticket = ticket
                            break
                    if found_ticket:
                        found_ticket.print_ticket_info()
                    else:
                        print("Ticket not found.")
                    continue
                else:
                    print("Ticket number cannot be empty.")
                    continue

            customer_name = input("Customer name: ").capitalize()
            email_address = input("Email address: ")
            login_code = input("Login code: ")
            if not login_code:
                login_code = customer_name[:3] + "00"
            password = input("Password: ")
            if not password:
                password = login_code
            description = input("Enter description of the issue: ")

            new_ticket = Ticket(team_member_name, team_member_login, customer_name, email_address, login_code,
                                password, description)
            new_ticket.resolve_password_change()

            new_ticket.print_ticket_info()

            solution_description = input("Enter solution description: ")
            new_ticket.provide_solution(solution_description)

            issue_rectified_input = input("Has the issue been rectified? (yes/no): ").lower()
            if issue_rectified_input == "yes":
                new_ticket.rectify_issue()
                print("You have solved the customer's issue. Thank them for the opportunity to help them and "
                      "complete the call.")
                tickets.append(new_ticket)
                continue  # Return to the start of the loop for new ticket creation
            elif issue_rectified_input == "no":
                print("Lets restart go back to the proposed solution?")
                tickets.append(new_ticket)  # Add the new ticket to the list

if __name__ == "__main__":
    Main.main()