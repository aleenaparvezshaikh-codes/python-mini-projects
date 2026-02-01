class Library:
    def __init__(self):
        self.books = ["Python", "C#", "C++", "DSA", "Java"]
    
    def display(self):
        if not self.books:
            print("No books available")
        else:
            print("\nAvailable books:")
            for book in self.books:
                print("-", book)
    
    def issue_book(self):
        book = input("Enter the book name to issue: ").title()
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book}' issued successfully!")
        else:
            print("Book not available in the library.")
    
    def return_book(self):
        book = input("Enter the book name to return: ").title()
        if book in self.books:
            print(f"Book '{book}' is already in the library.")
        else:
            self.books.append(book)
            print(f"Book '{book}' returned successfully!")
    
    def donate_book(self):
        book = input("Enter the book name to donate: ").title()
        if book in self.books:
            print(f"Book '{book}' is already available in the library.")
        else:
            self.books.append(book)
            print(f"Book '{book}' added successfully to the library!")

# Main program
library = Library()

while True:
    print("\n------------- Library Menu -------------")
    print("1. Display Books")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Donate Book")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        library.display()
    elif choice == "2":
        library.issue_book()
    elif choice == "3":
        library.return_book()
    elif choice == "4":
        library.donate_book()
    elif choice == "5":
        print("Thank you for using the library system!")
        break
    else:
        print("Invalid choice! Please try again.")
