import random
def lty(ic):
    match ic:
        case 0:
            return random.randrange(48,58)
        case 1:
            return random.randrange(65,91) 
        case 2 | 3:
            return random.randrange(97,123)
password_length = int(input("How long do you want your password to be (Enter a number): "))
password = ""
while len(password) <= password_length - 1:
    password += chr(lty(random.randrange(0,3)))
print("Your password is: ", password)
