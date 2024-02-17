
class Library:
    def __init__(self,file_name):
        self.file = open(file_name, "a+")

    def __del__(self):
       self.file.close()

    def openFile(self):
        self.file = open("books.txt", "a+")

    def addBook(self):
        title = input("Enter the book title: ")
        author = input("Enter the author's name: ")
        first_release_year = input("Enter the first release year: ")
        num_pages = input("Enter the number of pages: ")
        book_info = f"{title},{author},{first_release_year},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def removeBook(self):
        title = input("Enter the title of the book to remove: ").lower()
        self.file.seek(0)
        books = self.file.readlines()

        found = False
        updated_books = []

        for book in books:
            book_info = book.strip().split(',')
            if title != book_info[0].lower():
               updated_books.append(book)
            else:
               found = True

        if found:
           self.file.seek(0)
           self.file.truncate()
           self.file.writelines(updated_books)
           print("Book removed successfully.")
        else:
           print("Book not found.")

    def listBooks(self):
        self.file.seek(0)
        books = self.file.readlines()
        print("\nBook List")
        for book in books:
            book_info = book.strip().split(',')
            print(f"Book: {book_info[0]}, Author: {book_info[1]}")
    
    def findBook(self):
        title = input("Enter the title of the book to find: ").lower()
        self.file.seek(0)
        books = self.file.readlines()
        found = False
        for book in books:
            if title in book.lower():
                book_info = book.strip().split(',')
                print(f"\nBook: {book_info[0]}, Author: {book_info[1]}, Release Year: {book_info[2]}, Number of Pages: {book_info[3]}")
                found = True
                break
        if not found:
            print("Book not found.")




def menu():
    print("\n*** MENU***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Find Book")
    print("q) Ouit\n")


def menuOptions(lib,choice):
  if choice == "1":
    lib.listBooks()
  elif choice == "2":
    lib.addBook()
  elif choice == "3":
    lib.removeBook()
  elif choice=="4":
    lib.findBook()
  elif choice == "q":
    del lib
  else:
    print("Invalid choice.")

def main():
    lib = Library("books.txt")
    while True:
          menu()
          choice = input("Enter your choice: ")
          print("\n")
          menuOptions(lib,choice)
          if choice=='q':
             break
            
main()