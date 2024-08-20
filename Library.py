from book_member_data import book_data,members   

class Library:
    # Add a new book to the library if it does not already exist.
    def add_book(self,title,author,ISBN,status='available'):
        for book in book_data:
            if book['ISBN'] == ISBN:
                print(f"Book with ISBN {ISBN} already exists in the library.")
                return
        new_book_data={'title':title,'author':author,'ISBN':ISBN,'status':status}
        book_data.append(new_book_data)
        return print(f"\nBook {title} added into Library Successfully!")

    # Lend a book to a member if the book is available.
    def lend_book(self,ISBN,member_id):
        for book in book_data:
            if book['ISBN']==ISBN:
                if book['status']=='available':
                    book['status']='borrowed'
                    members[member_id]['borrowed_book'].append(ISBN)
                    return print("\nBook Lend Successfully!")
                else:
                    return print("\nBook already borrowed from library!")
        print("\nBook is not available!")

    # Return a borrowed book to the library.
    def return_book(self,ISBN,member_id):
        for book in book_data:
            if book['ISBN']==ISBN:
                if book["status"] == "borrowed" and ISBN in members[member_id]["borrowed_book"]:
                    members[member_id]['borrowed_book'].remove(ISBN)
                    book['status']='available'
                    return print(f"\nBook '{book['title']}' returned successfully by {members[member_id]['name']}")
                else:
                    return print(f"\nBook '{book['title']}' is not borrowed by member {member_id}.")
        print(f"\nBook with ISBN {ISBN} not found in the library.")

    # Display all books in the library.
    def display_book(self):
        if book_data is not None:
            for i,book in enumerate(book_data):
                print(f'{i+1}) Title: {book['title']} \n   Author: {book['author']} \n   ISBN: {book['ISBN']} \n   status: {book['status']}') 
        else:
            print("\nBooks not registered yet!!")       
