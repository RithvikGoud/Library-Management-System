from book_member_data import book_data,members
from Member import Member
from Library import Library

# Create an instance of the Library class
a=Library()
def main():
    k=3
    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Lend Book")
        print("4. Return Book")
        print("5. Display Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            while True:
                ISBN = input("Enter book ISBN: ")
                if len(ISBN)==13:
                    a.add_book(title, author, int(ISBN))
                    break
                else:
                    print("Invalid ISBN! Please enter a 13-digit ISBN.")     

        elif choice == "2":
            ID=int(input("Enter member ID: "))
            name=input("Enter name: ")
            email=input("Enter email: ")
            b=Member(ID,name,email)
            b.add_member()

        elif choice == "3":
            ISBN = int(input("Enter book ISBN: "))
            member_id = int(input("Enter member ID: "))
            if member_id in members:
                a.lend_book(ISBN, member_id)
            else:
                print("Member ID not found!")

        elif choice == "4":
            ISBN = int(input("Enter book ISBN: "))
            member_id = int(input("Enter member ID: "))
            if member_id in members:
                a.return_book(ISBN, member_id)
            else:
                print("Member ID not found!")
        
        elif choice == "5":
            a.display_book()
        
            
        elif choice == "6":
            print("===============Exiting......................")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()