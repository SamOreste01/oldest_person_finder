#Define Name standards
#Define Age standards
#Create tuple for data entries
#Create an dictionary array for the inputted data
#Input name and age 
#Ask the user to input or not
#Find the oldest 

def valid_name(name):
    try:
        name = str(name) #name must be strings
    except:
        print("Invalid Name")

def valid_age(age):
    try:
        age = int(age) #age must be integers
        age <= 122 #age must be only up to 122 years old
    except:
        print("Invalid Age")

user_input = []

name = input("Please Enter a Name: ")

age = int(input("Please Enter Age: "))
