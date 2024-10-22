#Define Name standards
#Define Age standards
#Create tuple for data entries
#Create an dictionary array for the inputted data
#Input name and age 
#Ask the user to input or not
#Find the oldest 

def valid_name(name):
    pass

def valid_age(age):
    try:
        age = int(age) #age must be integers
        age <= 122
    except:
        print("Invalid Age")

user_input = []

name = input("Please Enter a Name: ")

age = int(input("Please Enter Age: "))
