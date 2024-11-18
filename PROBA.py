class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password

class User:
    """
    класс пользователя, содержащий атрибуты: логин, пароль.
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            if len(password) < 4 and len(password) > 8 :
                print("<4 or >8")
            elif password.islower():
                print("no upper")
            elif password.isupper():
                print("no lower")
            elif not password.isdecimal():
                print("no num")
            else:
                self.password = password

if __name__ == '__main__':
    database = Database()
    user = User(input('username:'), input("password:"), input("confirm password:"))
    database.add_user(user.username, user.password)
    print(database.data)