master_pwd = input("what is the master password? ")


def view():
    pass

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

with open('passwords.txt', 'a') as f:
    f.write(name + "|" + pwd + "\n")


while True: 
    mode  = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit ?") .lower()
    if mode == "q":  
        break

    if mode == "view":
        add()
    elif mode == "add":
        pass
    else: 
        print("Invalid mode.")
