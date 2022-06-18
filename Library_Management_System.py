class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks
        self.issued = []

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print("\t *" + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Pleased keep it safe and return it within 30 days")
            self.issued.append(bookName)
            self.books.remove(bookName)
        elif bookName in self.issued:
            print("Sorry, This book has already been issued to someone else. Please wait until the book is returned")
        else:
            print("Sorry, This book is not available in the library")

    def  returnBook(self, bookName):
        if bookName in self.issued:
            self.books.append(bookName)
            print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")
        else:
            print("This book do not belong to this library")

    def donateBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for donating a book to this library. Have a great day!")
    
class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book

    def donateBook(self):
        self.book = input("Enter the name of the book you want to donate: ")
        return self.book
         
if __name__ == "__main__":
    
    centralLibrary = Library(['Three men in a boat', 'Euphoria', 'Heer Ranjha', 'Black Widow', 'jallianwala bagh massacre', 'S. Chand', 'R.D. Sharma', 'Let us C', 'Morris Mano', 'The pidepiper', 'Panchtantra', 'Julius Caeser', 'Diary of a young girl'])

    student = Student()

    while(True):
        welcomeMsg = '''\n=====Welcome to Central Library=====
        Please choose an option:
        1. Listing all the books
        2. Request a book
        3. Return a book
        4. Donate a book
        5. Exit the Library
        '''
        print(welcomeMsg)

        try:

            a = int(input("Enter a choice: "))

            if a == 1:
                centralLibrary.displayAvailableBooks()
            elif a == 2:
                centralLibrary.borrowBook(student.requestBook())
            elif a == 3:
                centralLibrary.returnBook(student.returnBook())
            elif a == 4:
                centralLibrary.donateBook(student.donateBook())
            elif a == 5:
                print("Thanks for choosing Central Library! Have a great day ahead")
                exit()
            else:
                print("Invalid Choice!")

            print("_______________________________________\n")

        except ValueError as e:
            print("Please Enter a valid value") 
