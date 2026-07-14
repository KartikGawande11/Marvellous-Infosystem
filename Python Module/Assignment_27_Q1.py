'''1: Write a Python program to implement a class named BookStore with the following specifications:

The class should contain two instance variables:

Name (Book Name)

Author (Book Author)

The class should contain one class variable:

NoOfBooks (initialize it to 0)

Define a constructor (init) that accepts Name and Author and initializes instance variables.

Inside the constructor, increment the class variable NoOf Books by 1 whenever a new object is created.

Implement an instance method:

Display()-should display book details in the format:

<BookName> by <Author>. No of books: <NoOfBooks'''
 
class BookStore():
     
     # Class variable to count total number of books
    NoOfBooks=0
    
    
     # Constructor to initialize book name and author
    def __init__(self,name,Author):
        self.name = name
        self.Author = Author
        
        BookStore.NoOfBooks += 1
        
    def Display(self):
        print(f"BookName:{self.name} by: {self.Author } No of books: {BookStore.NoOfBooks}")
       
       
obj1=BookStore("Python Programming", "Guido van Rossum")
print("Books 1")
obj1.Display()
        
        
obj1=BookStore("Data Science", "Andrew Ng")
print("Books 2")
obj1.Display()
        
        
        