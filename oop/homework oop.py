class User:
    def __init__(self, first_name, last_name, email, phone_number, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.password = password

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def update_password(self, new_password):
        if len(new_password) >= 8:
            self.password = new_password
            print('Updated password')
        else:
            raise ValueError('Password can not be less then 8 characters')

    def update_email(self, new_email):
        if "@" in new_email and "." in new_email:
            self.email = new_email
            print('Updated email')
        else:
            raise ValueError('Invalid email address')


user = User("Shawn", "Ruz", "shawn@uzautotransinc.com", "720-704-5566", "12345678")
print(user.full_name())
print(str(user))

user.update_password("newpass123")
user.update_email("john@uzautotransinc.com")