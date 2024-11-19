'''
набросок регистрации пользователя
'''
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
            if len(password) < 4 :
                print("<4")
                print("try again")
                exit()
            elif len(password) > 5 :
                print(">5")
                print("try again")
                exit()
            elif password.islower():
                print("no upper")
                print("try again")
                exit()
            elif password.isupper():
                print("no lower")
                print("try again")
                exit()
            elif not any(i.isdigit() for i in password1):
                print("no num")
                print("try again")
                exit()
            else:
                self.password = password
        else:
            print("passwords are not the same")
            print("try again")
            exit()

if __name__ == '__main__':
    database = Database()
    while True:
        choise = int(input('Hi! Chose you destiny: \n1 - in\n2 - reg\n'))
        if choise == 1:
            username = input("login: ")
            password = input("password: ")
            if username in database.data:
                if password == database.data[username]:
                    print(f'You welcome, {username} ')
            else:
                print("go away!")
                continue
        if choise == 2:
            user = User(username := input('username:'), password1 := input("password:"),
                        password2 := input("confirm password:"))
            database.add_user(user.username, user.password)
        print(database.data)
