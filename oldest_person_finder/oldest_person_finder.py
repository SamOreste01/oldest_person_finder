#Define Name standards
#Define Age standards
#Define ask for more input
#Create dictionary for data entries
#Create an dictionary array for the inputted data
#Input name and age 
#Ask the user to input or not
#Find the oldest 

def valid_name(name):
    try:    
        if name == str(name): #name must be a text
            return name.isalpha() #name must be letters from a-z
        return False
    except ValueError:
        return False

def valid_age(age):
    try:
        age = int(age) #age must be integers
        if age <= 122: #age must be only up to 122 years old
            return True
        return False    
    except ValueError:
        return False

def ask_input():
    while True:
        another_input = input("Do you want to enter another entry? (Yes/No): ")
        if another_input.lower() == 'yes':
            return True
        elif another_input.lower() == 'no':
            return False
        else:
            print("Invalid input! Please type 'Yes' or 'No'.")

def oldest_person():
    pass

user_input = []

while True:
    name = input("Please enter a name: ")
    while not valid_name(name):
        print("Invalid name! Name should contain only alphabetic characters.")
        name = input("Please enter a name: ")

    age = input("Please enter age: ")
    while not valid_age(age):
        print("Invalid age! Age should be a number between 0 and 122.")
        age = input("Please enter age: ")

    user_input.append({"name": name, "age": int(age)})

    if not ask_input():
        break


   