# file = open("rockyou.txt")
# import getpass


repeat = True

while repeat == True:
    file = open("passwords.txt", "r")
    total = 0
    # pas = getpass.getuser()
    password = input("Enter your password: ")

    if password == "exit":
        repeat = False

    else:
        try:
            for line in file:
                if (len(line)) == (len(password) + 1):
                    if password in line:
                        print(f'Password is: {line}')
                        total += 1
        except UnicodeDecodeError:
            if total >= 1:
                print(f"***!!!!!!! Password found!!!!!!!***.")
            else:
                print(f"Password was not found")
            file.close()
            print('Type "exit" to quit')
