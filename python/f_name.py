def hello():
    name = input("Please enter your name: ")
    print("Hello", name)

def get_firstname():
    firstname = input("Please enter your first name: ")
    return firstname

def get_surname():
    surname = input("Please enter your surname: ")
    return surname

if __name__=="__main__":
    firstname = get_firstname()
    surname = get_surname()
    print("Hello", firstname, surname)
    

          
