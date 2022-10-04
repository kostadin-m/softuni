from .user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if book_name in self.books_available.get(author):
            user.books.append(book_name)
            self.books_available[author].remove(book_name)

            if user.username not in self.rented_books.keys():
                self.rented_books[user.username] = {}
            self.rented_books[user.username].update({book_name: days_to_return})
            return f"{book_name} successfully rented for the next {days_to_return} days!"

        return f'The book "{book_name}" is already rented and will be available in {self.rented_books[user.username][book_name]} days!'

    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books:
            user.books.remove(book_name)
            self.books_available[author].append(book_name)
            del self.rented_books[user.username][book_name]
            return ''
        return f"{user.username} doesn't have this book in his/her records!"




