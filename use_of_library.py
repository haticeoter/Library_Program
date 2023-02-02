from library import *

print("""***********************************

Welcome to the Library Program.

Operations;

1. Show the Books

2. Look for a Book

3. Add a Book

4. Delete a Book

5. Increase the Edition

Type "E" to exit.
***********************************""")

library = Library()

while True:
    operation = input("Which operation would you like to do:")

    if (operation == "E"):
        print("Program is terminated.....")
        break
    elif (operation == "1"):
        library.show_books()

    elif (operation == "2"):
        name = input("Which book would you like ? ")
        print("Looking for the book...")
        time.sleep(2)

        library.inquiry_a_book(name)

    elif (operation == "3"):
        name = input("Name:")
        author = input("Author:")
        publisher = input("Publisher:")
        genre = input("Genre:")
        edition = int(input("Edition:"))

        new_book = Book(name,author,publisher,genre,edition)

        print("The book is added....")
        time.sleep(2)

        library.add_book(new_book)
        print("The book was added....")


    elif (operation == "4"):
        name = input("Which book would you like to delete ?")

        answer = input("Are you sure ? (Y/N)")
        if (answer == "Y"):
            print("The book is deleted...")
            time.sleep(2)
            library.delete_a_bool(name)
            print("The book was deleted....")


    elif (operation == "5"):
        name = input("Which book would you like to increase the edition ?")
        print("The edition is increased....")
        time.sleep(2)
        library.increase_edition(name)
        print("The edition was increased....")

    else:
        print("Invalid Operation...")