
game = True
# Artem Antonian
def encode():
    password = ""
    user = []
    user_input = input("Please enter your password: ")
    user.append(user_input)
    print("Your password has been encoded and stored!")
    print("")
    print(user[0])
    for i in user[0]:
        encoded_num = str(int(i) + 3)
        password += encoded_num
def main(game):
    while game:

        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")

        option = int(input("PLease enter an option: "))

        if option == 1:
            encode()
        elif option == 2:
            pass
        else:
            game = False




if __name__ == '__main__':
    main(game)
