

def generate_password(default_length=8):
    inputted_length = input("How long should the password be? Please provide a number or hit enter for default length of 8: ")
    password_length = 8 if len(inputted_length) == 0 else int(inputted_length)
    print(password_length)

generate_password()

