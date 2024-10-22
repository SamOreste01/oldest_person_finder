#Define Name standards
#Define Age standards
#Create an dictionary array for the inputted data
#Input name and age 
#Ask the user to input or not
#Find the oldest 

def valid_name(name):
    pass

def valid_age(age):
    pass

# Create an empty list to store user input dictionaries
user_input = []

# Loop to get multiple entries from the user
while True:
    # Get user input for name and age
    name = input("Please Enter Name (or 'quit' to stop): ")
    if name.lower() == 'quit':
        break  # Exit the loop if the user types 'quit'
    
    age = int(input("Please Enter Age: "))  # Convert age input to an integer
    
    # Create a dictionary for the current user
    user_entry = {"name": name, "age": age}
    
    # Append the user entry dictionary to the user_input list
    user_input.append(user_entry)

# Print the final list of user inputs
print(user_input)


