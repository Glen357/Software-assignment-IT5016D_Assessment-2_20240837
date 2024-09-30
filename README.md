Ticketing System Readme

Welcome to My IT Help Desk Ticketing System. This is simple program that I have created as part of My study curriculum. It can help to manage customer support tickets efficiently in a front-line IT customer service support environment. Whether you're a beginner developer or an experienced professional, this readme should be able to guide you through using and understanding the system. 

Getting Started
To get started, simply run the main.py file in your Python environment. This will launch the Ticketing System in your terminal or command prompt. Using the Ticketing System

Creating a Ticket: 
• When prompted, enter the details of the ticket, such as the staff ID, creator's name, customer contact email address, and a description of the issue. 
• If the issue is related to a password change, you can simply type “Password change” into the “description” field, and the system will automatically generate a login code and password based on the customer's name and ticket number. 
• After entering the ticket details, provide a solution description and indicate whether the issue has been rectified.

Searching for a Ticket: 
• If you need to search for an existing ticket select “2” in the main menu. When prompted, provide the ticket number. (The Initial ticket created will be 2001) 
• The system will display the details of the ticket if it exists, allowing you to review or edit it if needed.

Responding to a Ticket:
• You can respond to any ticket by selecting “3” in the main menu. When prompted, provide the ticket number. (The Initial ticket created will be 2001)
• The system will display the details of the ticket if it exists, allowing you to review and respond to it.
• If the ticket you are responding to is also going to be complete after your response. Simply add “closed” after the period ending your response. (eg: Completed response. Closed) This will set the ticket status to closed

Ticket Status: 
• Tickets have two possible statuses: "Open" or "Closed". 
• If you need to update an existing tickets status, select “2” in the main menu, which will reopen a ticket if a correct ticket number is added. When prompted, provide the ticket number. (The Initial ticket created will be 2001
• If the issue has been rectified, change the status to "Closed", by typing “Closed” into either the new description or respond to ticket fields. Otherwise, it remains "Open" or is set to "To Solve" in the ticket statistics display.

Ticket Statistics
• If you would like to view all the ticket statistics (Tickets created, Resolved, or Tickets left to solve) you can select “4” in the main menu. This will display a list of stats, and reopen the main menu.

Features 
• Automatic Generation of Login Code and Password: For password change requests, the system automatically generates a login code and password based on the first two characters of the staffID, followed by the first three characters of the ticket creator name.
. • Easy Ticket Management: With the ability to create, search, and reopen tickets, the system helps you keep track of customer issues and resolutions. 
• Simple User Interface: The system operates entirely in the terminal or command prompt, making it easy to use for developers of all skill levels.

Contributing If you'd like to contribute to the Ticketing System, feel free to fork the repository, make your changes, and submit a pull request. Your contributions are welcome and appreciated.

