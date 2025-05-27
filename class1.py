# Create a simple class for a Book with attributes like title and author.
# Then create two book objects and print their details.

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        
    def book_details(self):
            print(f"The book title is {self.title} and is written by {self.author}")
            
b1 = Book("wings of fire","Dr.apj abdul kalam")
b2 = Book("The Alchemist", "Paulo Coelho")

b1.book_details()
b2.book_details()
