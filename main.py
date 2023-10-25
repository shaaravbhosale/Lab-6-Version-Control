# Author: Shaarav Bhosale
def menu():
    print("\nMenu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encode(password):
    encoded_password = ''
    for value in password:
        encoded_value = str((int(value) + 3) % 10)
        encoded_password += encoded_value
    return encoded_password


def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        if int(digit) >= 3:
            decoded_password += str(int(digit) - 3)
        else:
            decoded_password += str(int(digit) + 7)

    print(f"The encoded password is: {encoded_password}, and the original password is {decoded_password}")


def main():
    encoded_password = ''
    while True:
        menu()
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            for i in range(0, len(password) - 1):
                while len(password) != 8 or not password[i].isdigit():
                    password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
        elif option == 2:
            decode(encoded_password)
        elif option == 3:
            break
        else:
            print("Invalid input")


if __name__ == '__main__':
    main()
