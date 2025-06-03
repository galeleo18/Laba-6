class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password

users = [
    User("Анатолий", "1234"),
    User("Дмитрий", "qwerty"),
    User("Артём", "<PASSWORD>"),
    User("Андрей", "I_Love_C++"),
    User("Даниил", "BigBoss")
]

search_login = "Анатолий"
search_password = "1234"

for user in users:
    if user.login == search_login and user.password == search_password:
        print(f"Найден пользователь: {user.login}")