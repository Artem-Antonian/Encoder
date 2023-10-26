game = True


# Artem Antonian
def encode(user):
    password = ""
    
    for i in user[0]:
        if int(i) < 7:
            encoded_num = str(int(i) + 3)
        elif int(i) == 7:
            encoded_num = "0"
        elif int(i) == 8:
            encoded_num = "1"
        else:
            encoded_num = "2"
        password += encoded_num
        return password

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
            user = []
            user_input = input("Please enter your password: ")
            user.append(user_input)
            
            print("Your password has been encoded and stored!")
            print("")
            encoded_password = encode(user)
        elif option == 2:
            decoded_password = decode(password)
        else:
            game = False


if __name__ == '__main__':
    main(game)
