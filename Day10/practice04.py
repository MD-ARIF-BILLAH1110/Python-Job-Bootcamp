class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


    def show_book_deatils(self):
        print(f"\nTitle: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")


title = input("Enter Title: ")
author = input("Enter Author: ")
price = float(input("Enter Price: "))

book = Book(title, author, price)
book.show_book_deatils()
        