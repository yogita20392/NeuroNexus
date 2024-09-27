import random

uppercase_letter = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lowercase_letter = list("abcdefghijklmnopqrstuvwxyz")
digits = list("0123456789")
spec_chr = list("!@#$%^&*")

def pass_generator(pass_len):
    
    password = []
    available_chr = []

    print("Choose chr set for password ")
    print("1. UperrLetters")
    print("2. LowerLetters")
    print("3. Digits")
    print("4. SpecialCharachters")
    print("5. Exit")

    while (True):
        choice = int(input("Pick a number [1-5]"))

        if(choice == 1):
            available_chr.extend(uppercase_letter)
        
        elif(choice == 2):
            available_chr.extend(lowercase_letter)
        
        elif(choice == 3):
            available_chr.extend(digits)

        elif(choice == 4):
            available_chr.extend(spec_chr)

        elif(choice == 5):
            break

        else:
            print("Please pick valid option !!")
        
    if available_chr :
        password = random.choices(available_chr ,k=pass_len)
        random.shuffle(password)

    return ''.join(password)



if __name__ == "__main__":
    pass_len = int(input("Enter the length for the password."))

    result = pass_generator(pass_len)
    print("Suggested Password : ",result)