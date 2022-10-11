from .user import User
from .library import Library


class Registration:
    def add_user(self, user: User, library: Library):
        if self.contains_user(user.user_id, library.user_records):
            return f"User with id = {user.user_id} already registered in the library!"

        return self.add_to_user_records(library.user_records,user)

    def remove_user(self, user: User, library: Library):
        if not self.contains_user(user.user_id, library.user_records):
            return "We could not find such user to remove!"

        return self.remove_from_user_records(library.user_records, user)

    def change_username(self, _id: int, new_username, library: Library):
        user_to_change = self.contains_user(_id, library.user_records)
        if not user_to_change:
            return f'There is no user with id = {_id}!'
        if user_to_change.username == new_username:
            return "Please check again the provided username - it should be different than the username used so far!"

        return self.change_name(user_to_change, new_username, _id, library)

    @staticmethod
    def contains_user(user: int, library):
        for x in library:
            if x.user_id == user:
                return x
        return None

    @staticmethod
    def add_to_user_records(records, user: User):
        records.append(user)

    @staticmethod
    def remove_from_user_records(records, user: User):
        records.remove(user)

    @staticmethod
    def change_name(old, new, _id, library):
        if old.username in library.rented_books.keys():
            library.rented_books[new] = library.rented_books.pop(old.username)
        old.username = new
        return f"Username successfully changed to: {new} for user id: {_id}"
