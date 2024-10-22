print("library mangement system")
users=[]
list_books=[]
class lib_members:
    def __init__(self,name_user):
        self.name_user=name_user
        self.bookinhand=None
    def add_user(self):
        if self not in users:
            users.append(self)
            print("user added../")
        else:
            print(f"{self} already a user")

class library:
    def __init__(self,name,author):
        self.name=name
        self.author=author
        self.availability=True
        
    def add_book(self):
        if self not in list_books:
            list_books.append(self)
            print("book added../")
        else:
            print(f" the book {self.name} is already available..")
    @staticmethod
    def lend_book(user_name,name_book):
        user=next((user for user in users if user.name_user==user_name),None)
        book=next((book for book in list_books if book.name==name_book),None)
        if user and book:
            if book.availability:
                user.bookinhand=book.name
                book.availability=False
                print(f"{book.name} is lended to {user.name_user}")
            else:
                print("The book already lended../")
        else:
            if not user:
                print(f"{user_name} is not a member..")
            if not book:
                print(f"{name_book} is not available in the library..")
    @staticmethod
    def return_book(user_name,name_book):
            user=next((user for user in users if user_name==user.name_user),None)
            book=next((book for book in list_books if name_book==book.name),None)
            if user and book:
                if book.availability==False:
                    user.bookinhand=None
                    book.availability=True
                    print(f"{book.name} is returned and available../")
                if book.availability:
                    print("the book is not lended..")
            else:
                if not user:
                    print(f"{user} doesnt exist or is not an existing member../")
                if not book:
                    print(f"{book} is not available in this library")




        
while(True):
    try:
                print("1.create new user \n2.add new book \n3.lend book\n4.list of members \n5.books available\n6.return book\n7.exit")
                option=int(input("enter your choice:"))
                if option==1:
                    name=input("enter your name:")
                    user=lib_members(name)
                    user.add_user()
                elif option==2:
                    name=input("enter title of the book:")
                    author=input("enter name of author:")
                    book=library(name,author)
                    book.add_book()
                elif option==3:
                    user_name=input("enter user name:")
                    book_name=input("enter title of the book:")
                    library.lend_book(user_name,book_name)
                elif option==4:
                    print("/...list of members../")
                    for i,user in enumerate(users):
                        print(f"{i+1}){user.name_user}")
                elif option==5:
                    print("/..the list of book../ ")
                    for i,book in enumerate(list_books):
                        print(f"{i+1}){book.name} by {book.author} availability={book.availability}")
                elif option==6:
                    user_name=input("enter name:")
                    book=input("enter book name:")
                    library.return_book(user_name,book)


                else:
                    print("exiting../")
    except ValueError:
        print("invalid input")