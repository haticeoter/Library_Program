import sqlite3

import time

class Book():

    def __init__(self,name,author,publisher,genre,edition):

        self.name = name
        self.author = author
        self.publisher = publisher
        self.genre = genre
        self.edition = edition

    def __str__(self):

        return "Name of the Book: {}\nAuthor: {}\nPublisher: {}\nGenre: {}\nEdition: {}\n".format(self.name,self.author,self.publisher,self.genre,self.edition)


class Library():

    def __init__(self):

        self.get_connect()

    def get_connect(self):

        self.connect = sqlite3.connect("kütüphane.db")

        self.cursor = self.connect.cursor()

        inquiry = "Create Table If not exists books (name TEXT,author TEXT,publisher TEXT,genre TEXT,edition INT)"

        self.cursor.execute(inquiry)

        self.connect.commit()
    def disconnect(self):
        self.connect.close()

    def show_books(self):

        inquiry =  "Select * From books"

        self.cursor.execute(inquiry)

        books = self.cursor.fetchall()

        if (len(books) == 0):
            print("There is no book in the library...")
        else:
            for i in books:

                book = Book(i[0],i[1],i[2],i[3],i[4])
                print(book)

    def inquiry_a_book(self,name):

        inquiry = "Select * From books where name = ?"

        self.cursor.execute(inquiry,(name,))

        books = self.cursor.fetchall()

        if (len(books) == 0):
            print("The book you were looking for was not found.....")
        else:
            book = Book(books[0][0],books[0][1],books[0][2],books[0][3],books[0][4])

            print(book)
    def add_book(self,book):

        inquiry = "Insert into books Values(?,?,?,?,?)"

        self.cursor.execute(inquiry,(book.name,book.author,book.publisher,book.genre,book.edition))

        self.connect.commit()

    def delete_a_book(self,name):

        inquiry = "Delete From books where name = ?"

        self.cursor.execute(inquiry,(name,))

        self.connect.commit()

    def increase_edition(self,name):

        inquiry = "Select * From books where name = ?"

        self.cursor.execute(inquiry,(name,))


        books = self.cursor.fetchall()

        if (len(books) == 0):
            print("There is no such book...")
        else:
            edition = books[0][4]

            edition += 1

            inquiry2 = "Update books set edition = ? where name = ?"

            self.cursor.execute(inquiry2,(edition,name))

            self.connect.commit()