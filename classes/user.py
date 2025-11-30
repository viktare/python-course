class User:

    def __init__(self,  name, surname, age, email) -> None:
        self.name = name
        self.surname = surname
        self. age = age
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        return f" The user is {self.name} {self.surname} and has {self.age}"
    
    def add_login_attempt(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:

    def __init__(self, *privileges) -> None:
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)
    
class Admin(User):

    def __init__(self, name, surname, age, email) -> None:
        super().__init__(name, surname, age, email)
        self.privileges = Privileges('can see users', 'can edit users', 'can delete users')

    
viktor = Admin('Viktor', 'Stevanovic', 26, 'stevanovic.viktor@gmail.com')

viktor.privileges.show_privileges()
    