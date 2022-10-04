class Registration:

    def add_user(self, user, library):
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        return library.user_records.append(user)

    def remove_user(self, user, library):
        if user not in library.user_records:
            return "We could not find such user to remove!"
        return library.user_records.remove(user)

    def change_username(self, id: int, new_username,library):
        for x in library.user_records:
            if x.user_id == id:
                if x.username == new_username:
                    return "Please check again the provided username " +\
                            "- it should be different than the username used so far!"

                if x.username in library.rented_books.keys():
                    library.rented_books[new_username] = library.rented_books.pop(x.username)
                x.username = new_username
                return f"Username successfully changed to: {new_username} for user id: {id}"

        return f'There is no user with id = {id}!'

