from .user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if book_name not in self.books_available.get(author):
            return f'The book "{book_name}" is already rented and will be available in {self.rented_books[user.username][book_name]} days!'
        self.add_to_user_books(user, book_name)
        self.remove_from_available_books(author, book_name)
        self.add_to_rented_books(user.username, book_name, days_to_return)

    def return_book(self, author: str, book_name: str, user: User):
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"
        self.remove_from_user_books(user, book_name)
        self.add_to_available_books(author, book_name)
        self.remove_from_rented_books(user.username,book_name)


    def add_to_available_books(self, author, book):
        self.books_available[author].append(book)

    def remove_from_available_books(self, author, book):
        self.books_available[author].remove(book)

    def add_to_rented_books(self, name, book, days_to_return):
        self.rented_books[name] = self.rented_books.get(name, {})
        self.rented_books[name].update({book: days_to_return})
        return f"{book} successfully rented for the next {days_to_return} days!"

    def remove_from_rented_books(self,name,book):
        del self.rented_books[name][book]

    def add_to_user_books(self, user, book):
        user.books.append(book)

    def remove_from_user_books(self,user,book):
        user.books.remove(book)
