import dateOP
from library import librarian

dateOP.printdate()




while True:
    print("""
===== Book Management Menu =====
1. Add a New Book
2. View All Books
3. Remove Book
4. Checkout a Book
5. Return a Book
6. Exit
""")
    choice = int(input("Select one of the options: "))
    if choice == 1:
        title = input("Title: ")
        author = input("Author: ")
        isbn = input("ISBN: ")
        librarian.add_book(librarian.library,title,author,isbn)
        librarian.save_library(librarian.library)

    elif choice == 2:
        librarian.display_books(librarian.library)
    elif choice == 3:
        isbn = input("Please Enter the ISBN of the Book: ")
        librarian.remove_book(librarian.library,isbn)
        librarian.save_library(librarian.library)
    elif choice == 4:
        isbn = input("Please Enter the ISBN of the Book: ")
        librarian.check_out_book(librarian.library,isbn)
        librarian.save_library(librarian.library) 
    elif choice == 5:
        isbn = input("Please Enter the ISBN of the Book: ")
        librarian.return_book(librarian.library,isbn)
        librarian.save_library(librarian.library)
    elif choice == 6:
        print("Thank You")
        break
    else:
        print("Invalid choice")
    

        
    
