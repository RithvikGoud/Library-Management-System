from book_member_data import book_data,members

class Member:
    # Initialize a new member with an ID, name, email, and an empty list of borrowed books.
    def __init__(self,member_id,name,email):
        self.member_id=member_id
        self.name=name
        self.email=email
        self.borrowed_books = []

    # Add a book to the member's borrowed list if it's not already borrowed.
    def borrow_book(self,ISBN):
        if ISBN not in self.borrowed_books:
            self.borrowed_books.append(ISBN)
            print(f"Book with ISBN {ISBN} borrowed by member {self.member_id}.")
        else:
            print(f"Member {self.member_id} already borrowed the book with ISBN {ISBN}.")
    
    # Register the member if the ID is unique, the email is valid, and not already used.
    def add_member(self):
        if self.member_id in members:
            print(f"Member with ID {self.member_id} already exists.")
        for member in members.values():
            if member['email'] == self.email:
                print(f"Email {self.email} is already associated with another member.")
                return
        if not self.email.endswith('@gmail.com'):
            print("Email entered is invalid! Please enter an email ending with '@gmail.com'.")
            return
        new_member = Member(self.member_id, self.name, self.email)
        members[self.member_id] = {"name": new_member.name, "email": new_member.email, "borrowed_book": new_member.borrowed_books}
        print(f"Member {self.name} registered successfully in Library Management System.")

    # Remove a book from the member's borrowed list if it was borrowed.
    def return_book(self,ISBN):
        if ISBN in self.borrowed_books:
            self.borrowed_books.remove(ISBN)
            print(f"Book with ISBN {ISBN} returned by member {self.member_id}.")
        else:
            print(f"Book with ISBN {ISBN} not found in the borrowed books of member {self.member_id}.")