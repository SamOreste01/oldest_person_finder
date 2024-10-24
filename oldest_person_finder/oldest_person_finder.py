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
    except ValueError:
        return False

def valid_age(age):
    try:
        age = int(age) #age must be integers
        if age <= 122: #age must be only up to 122 years old
            return True
    except ValueError:
        return False

def ask_input(another_input):
    another_input = input("Do you want to Enter another entry? (Yes/No): ")
    if another_input == "Yes":
        name
        age
    elif another_input == "No":
        break
        
user_input = {}

while True:
    name = input("Please Enter a Name: ")
    while not valid_name(name):
        print("Invalid Name!")

    age = input("Please Enter Age: ")
    while not valid_age(age):
        print("Invalid Age!")

user_input.append((name, int(age))) #Add entries to the dictionary





