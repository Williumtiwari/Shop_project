class User():
    def login(self):
        self.login_user = input("Enter Username: ")
        self.login_password = input("Enter Password: ")
        try:
            with open("register.txt", "r") as file:
                for users in file.readlines():
                    data = users.split("~")
                    if self.login_user == data[0] and self.login_password == data[1]:
                        print("Login Successful!")
                        break
                    else:
                        print("Invalid Username or Password!")
        except FileNotFoundError:
            print("No User Accounts found. Please register first.")

    def register(self):
        self.login_user = input("Enter Username: ")
        self.login_password = input("Enter Password: ")
        self.check_password = input("Re-enter Password: ")
        self.email = input("Enter Email: ")

        if self.login_password == self.check_password:
            print("Password matched. You can login.")
            with open("register.txt", "a+") as file:
                file.write(f"{self.login_user}~{self.login_password}~{self.email}\n")
        else:
            print("Passwords did not match!")

user = User()
print("1 - Login\n2 - Register")
choice = int(input("> "))

if choice == 1:
    user.login()
elif choice == 2:
    user.register()
else:
    print("Invalid Choice!") 