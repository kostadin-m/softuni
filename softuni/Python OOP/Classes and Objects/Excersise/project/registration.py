from .user import User
from .library import Library


class Registration:
    def add_user(self, user: User, library: Library):
        if self.contains_user(user.user_id, library.user_records):
            return f"User with id = {user.user_id} already registered in the library!"
        return library.user_records.append(user)

    def remove_user(self, user: User, library: Library):
        if not self.contains_user(user.user_id, library.user_records):
            return "We could not find such user to remove!"
        return library.user_records.remove(user)

    def change_username(self, _id: int, new_username, library: Library):
        user_to_change = self.contains_user(_id, library.user_records)
        if not user_to_change:
            return f'There is no user with id = {_id}!'
        if user_to_change.username == new_username:
            return "Please check again the provided username " +\
                        "- it should be different than the username used so far!"

        if user_to_change.username in library.rented_books.keys():
            library.rented_books[new_username] = library.rented_books.pop(user_to_change.username)
        user_to_change.username = new_username
        return f"Username successfully changed to: {new_username} for user id: {_id}"

    def contains_user(self, user: int, library):
        for x in library:
            if x.user_id == user:
                return x
        return False



