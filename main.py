import pickle
A=[]
B=[]
def NewBooks():
   L = []
   with open("Library.dat", "ab") as F:
       while True:
           BookID = int(input("Enter Book ID: "))
           Book = input("Enter Name Of Book: ")
           Category = input("Enter Category: ")
           Price = int(input("Enter Price: "))
           Quantity = int(input("Enter Quantity: "))
           PublisherName = input("Enter Publisher Name: ")
           L = [BookID, Book, Category, PublisherName, Price, Quantity]
           pickle.dump(L, F)
           Ch = input("More (Y/N)? ")
           if Ch in ["no", "n","N"]:
               break
def IssueTable():
   try:
      with open("IssueTable.dat","rb") as I:
          x=pickle.load(I)
          if len(x)!=0 :
           print(x)
   except FileNotFoundError:
       print("File Not Found")

def Issue2():
   global A
   A = []
   try:
       with open("Library.dat", "rb") as F:
           issued = False
           books = []
           while True:
               try:
                   book = pickle.load(F)
                   books.append(book)
               except EOFError:
                   break

           BookName = input("Enter Book which you want to issue: ")
           NewName = []

           for book in books:
               if book[1] == BookName and book[5] > 0:
                   print("Book Issued")
                   book[5] -= 1
                   A.append(book)
                   AddIssueTable()
                   print("Remaining Quantity Is", book[5])
                   issued = True
               NewName.append(book)

       with open("Library.dat", "wb") as F:
           for book in NewName:
               pickle.dump(book, F)
   except FileNotFoundError:
       print("File Not Found")

def AddIssueTable():
   global A
   try:
       with open("IssueTable.dat", "ab") as I:
           for i in A:
               pickle.dump(i, I)
       A.clear()
   except FileNotFoundError:
       print("File Not Found")

def ReturnBook():
   global B
   B = []
   try:
       with open("Library.dat", "rb") as F:
           books = []
           while True:
               try:
                   book = pickle.load(F)
                   books.append(book)
               except EOFError:
                   break

       ID = int(input("Enter Book ID: "))
       Time = int(input("Enter time of issue (in Days): "))
       if Time > 14:
           print("Pay 100 Rs fine")

       NewName = []
       for book in books:
           if book[0] == ID:
               book[5] += 1
               print("Details of the book are", book)
               B = book
               ReturnIssueTable()
           NewName.append(book)


        with open("Library.dat", "wb") as F:
           for book in NewName:
               pickle.dump(book, F)
   except FileNotFoundError:
       print("File Not Found")


def ReturnIssueTable():
   global B
   try:
       with open("IssueTable.dat", "rb") as I:
           IssuedBooks = []
           while True:
               try:
                   i = pickle.load(I)
                   IssuedBooks.append(i)
               except EOFError:
                   break

       update = []
       for i in IssuedBooks:
           if i != B:
               update.append(i)
       with open("IssueTable.dat", "wb") as I:
           for book in update:
               pickle.dump(book, I)
   except FileNotFoundError:
       print("File Not Found")


def View():
   try:
      with open("Library.dat","rb") as F:
        while True:
           try:
               IT=pickle.load(F)
               print(IT)
           except:
               break
   except FileNotFoundError():
       print(" Data Does Not Exist")

def SearchBookByBookName():
   try:
       with open("Library.dat", "rb") as F:
           BTitle = input("Enter the Book Name to be Searched: ")
           count = 0
           while True:
               try:
                   book = pickle.load(F) 
                   if book[1] == BTitle:
                       print(book)
                       count += 1
               except EOFError:
                   break
           if count > 0:
               print("Book with title", BTitle,"found ")
           else:
               print("Book not found.")
   except FileNotFoundError:
       print("File not Found!!!")

def SearchBookByBookID():
   try:
       with open("Library.dat", "rb") as F:
           BID = int(input("Enter Book ID to be Searched: "))
           count = 0
           while True:
               try:
                   book = pickle.load(F) 
                   if book[0] == BID:
                       print(book)
                       count += 1
               except EOFError:
                   break
           if count > 0:
               print("Book with Book ID ",BID,"found time.")
           else:
               print("Book with Book ID ",BID, "not found.")
   except FileNotFoundError:
       print("File not found!!!")

def ModifyPrice():
   try:
       books = []
       with open("Library.dat", "rb") as F:
           while True:
               try:
                   books.append(pickle.load(F))
               except EOFError:
                   break

       BN = input("Enter the Book name ")
       found = False
       for book in books:
           if book[1] == BN:
               print("Present Content:")
               print(book)
               newprice = int(input("Enter new price: "))
               book[4] = newprice
               found = True
               print("Price updated successfully.")
               break

       if not found:
           print("Book with name",BN,"not found")

       with open("Library.dat", "wb") as F:
           for book in books:
               pickle.dump(book, F)
   except FileNotFoundError:
       print("File Not Found!!!")

def Issue1():
        print("Following Books are Present in Library")
        View()

def ClearFile(filename):
   with open(filename, "w") as file:
       pass
def main():
   C=str(input(''' Enter What Operation To Perform
                   Issue Book: I
                   Add Book Record : A
                   View Book Record Table : VR
                   Search Book By Book ID : SI
                   Search Book By Book Name : SN
                   Modify Book Price : M
                   Return A Book : R
                   View Books Issued Table : VI '''))
   if C=="I":
       N=int(input("Enter No. Of Books to Issue"))
       for i in range (N):
           Issue1()
           Issue2()
   elif C=="A":
       NewBooks()
   elif C=="VR":
       View()
   elif C=="SI":
       SearchBookByBookID()
   elif C=="SN":
       SearchBookByBookName()
   elif C=="M":
       ModifyPrice()
   elif C=="R":
       ReturnBook()
   elif C=="VI":
       IssueTable()
   else:
       print("Invalid Input")
#Main 

while True:
   main()
   n=str(input("More (Y/N)"))
   if n=="N":
       ClearFile("Library.dat")
       ClearFile("IssueTable.dat")
       break
