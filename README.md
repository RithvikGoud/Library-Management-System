# Library Management System

This is a simple Library Management System that keeps track of books, authors, and library members. The system supports the following functionalities:

- Adding new books to the library
- Lending books to library members
- Returning books to the library
- Displaying the list of books and their statuses

## Features

### Book Information:
The library system stores details for each book, which include:
- `title`: The title of the book
- `author`: The author of the book
- `ISBN`: The unique identifier for the book
- `status`: The availability status of the book (`available` or `borrowed`)

### Member Information:
The system stores member details in a dictionary, where each member has:
- `member_id`: A unique identifier for the member
- `name`: The name of the member
- `email`: The email address of the member
- `borrowed_books`: A list of ISBNs of books borrowed by the member

## Requirements

The system is divided into two primary classes:

### `Library` Class
This class handles the following operations:
- `add_book(title, author, ISBN)`: Adds a new book to the library.
- `lend_book(ISBN, member_id)`: Lends a book to a member if the book is available.
- `return_book(ISBN, member_id)`: Returns a book to the library.
- `display_books()`: Displays a list of all books with their current statuses.

### `Member` Class
This class manages individual members and their borrowed books. It includes:
- `__init__(member_id, name, email)`: Initializes a new member.
- `borrow_book(ISBN)`: Adds a book to the member's list of borrowed books.
- `return_book(ISBN)`: Removes a book from the member's list of borrowed books.

## Instructions

### Setup the Environment:
- Initialize the list of books and a dictionary of members with some sample data.

### Implement the Library Class:
- Create a `Library` class that contains methods to manage the book collection and handle the lending process.

### Implement the Member Class:
- Create a `Member` class that stores member information and keeps track of borrowed books.

### Test the System:
Create a script to demonstrate the functionality of the system by performing the following actions:
1. Add new books to the library.
2. Register new members.
3. Lend books to members.
4. Return books to the library.
5. Display the list of books and their statuses.

## Sample Usage

Here is a quick overview of how the system can be used:

1. **Adding Books:**
   - Books are added to the library with a title, author, and ISBN.
   
2. **Registering Members:**
   - New members are added with a unique member ID, name, and email.

3. **Lending Books:**
   - A member can borrow books from the library if they are available. The system will update the book's status to `borrowed` and add the book to the member's borrowed list.

4. **Returning Books:**
   - Once a member is done reading a book, they can return it to the library. The system updates the book's status to `available` and removes it from the member's borrowed list.

5. **Displaying Books:**
   - The system displays a list of all books in the library, along with their current status (either `available` or `borrowed`).

## Conclusion

This system provides basic functionalities for managing a small library, including adding books, lending books to members, and tracking borrowed books. It can be further extended with features like book reservations, due dates for returned books, and fine calculations for overdue books.
