class library:
    
    def __init__(self,name,*books):
        self.name=name
        self.books=[]
        self.no_of_books=0
        for book in books:
            self.books.append(book)
            self.no_of_books+=1
    
    def addBook(self,*books):
        for book in books:
            self.books.append(book)
            self.no_of_books+=1     
    def getNoOfBooks(self):
        return self.no_of_books
    def check(self):
        return True if self.no_of_books==len(self.books) else False
library1=library("Prabhat's Library","theory of relativity","Einstein","Maths")  
print(library1.books)  
library1.addBook("Science","physics")
print(library1.books)    