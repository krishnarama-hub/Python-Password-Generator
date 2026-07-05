import random
print("""
╔═══════════════════════════════════════════════════╗
║ ____                                            _ ║
║|  _ \  __ _  ___  ___ __      __ ___   _ __  __| |║
║| |_) |/ _` |/ __|/ __|\ \ /\ / // _ \ | '__|/ _` |║
║|  __/| (_| |\__ \\__ \ \ V  V /| (_) || |  | (_| |║
║|_|    \__,_||___/|___/  \_/\_/  \___/ |_|   \__,_|║
║                                                   ║
║  ____                           _                 ║
║ / ___|  ___  _ __   _ __  __ _ | |_  ___   _ __   ║
║| |  _  / _ \| '_ \ | '__|/ _` || __|/ _ \ | '__|  ║
║| |_| ||  __/| | | || |  | (_| || |_| (_) || |     ║
║ \____| \___||_| |_||_|   \__,_| \__|\___/ |_|     ║
╚═══════════════════════════════════════════════════╝

""")
print("-----THE AUTOMATIC PASSWORD GENRATOR-----")
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z',

    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = [
    '0', '1', '2', '3', '4','5', '6', '7', '8', '9'
]

symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*','(', ')', '-', '_', '=', '+','[', ']', '{', '}', '\\',
      '|',';', ':', "'", '"', ',', '.','<', '>', '/', '?', '`', '~']
print("-"*100)
dicuss=False
while dicuss!=True:
    def choice():
            global choices
            choices=input("Enter your choice that you want a squence random genrated passowrd(s) or randowm genrated password(r): \n 's' for the squence and 'r' for the random").lower()
            print("-"*100)
    def squence_password_genrator():
        password=[]
        for i in range(letter):
            letter_random=random.choice(alphabet)
            password.append(letter_random)
        for i in range(sign):
            letter_random=random.choice(symbols)
            password.append(letter_random)
        for i in range(numericals):
            letter_random=random.choice(numbers)
            password.append(letter_random)
        print("-"*100)
        print("Thanks for genrating the password !!!!")
        print("-"*100)
        string=""
        for i in password:
            string+=i
        print("-"*100)
        print(f"Here's your password :{string}")
        print("-"*100)
        return
    def random_password_genrator():
        password=[]
        for i in range(letter):
            letter_random=random.choice(alphabet)
            password.append(letter_random)
        for i in range(sign):
            letter_random=random.choice(symbols)
            password.append(letter_random)
        for i in range(numericals):
            letter_random=random.choice(numbers)
            password.append(letter_random)
        print("-"*100)
        print("Thanks for genrating the password !!!!")
        print("-"*100)
        random.shuffle(password)
        string=""
        for i in password:
            string+=i
        print("-"*100)
        print(f"Here's your password : {string}")
        print("-"*100)
        return
    def connection():
        global letter
        global sign
        global numericals
        if choices=="s":
            print("-"*100)
            letter=int(input("Enter how many letters you want in the password:"))
            print("-"*100)
            sign=int(input("Enter how many symbols you want in the password:"))
            print("-"*100)
            numericals=int(input("Enter how numbers  you want in the password:"))
            print("-"*100)
            squence_password_genrator()
            return
        else:
            print("-"*100)
            letter=int(input("Enter how many letters you want in the password:"))
            print("-"*100)
            sign=int(input("Enter how many symbols you want in the password:"))
            print("-"*100)
            numericals=int(input("Enter how numbers  letters you want in the password:"))
            print("-"*100)
            random_password_genrator()
            return
    choice()
    connection()
    print("-"*100)
    choose= input("Do you want to change the password or password type\n(for changing the password write 'change' and for the type wirte the 'type') \n or no for the left the password  :")
    print("-"*100)
    if choose =="change":
        connection()
        print("-"*100)
        continues=input("Do you want to continue or not :").lower()
        print("-"*100)
        if continues=="not":
            dicuss=True
            print("The password genrator has been completed!!!----")



    elif choose=="type":
        choice()
        connection()
        print("-"*100)
        continues=input("Do you want to continue or not :").lower()
        print("-"*100)
        if continues=="not":
            dicuss=True
            print("-"*100)
            print("The password genrator has been completed!!!----")
            print("-"*100)
    else:
        dicuss=True
        print("-"*100)
        print("The password genrator has been completed!!!----")
        print("-"*100)










