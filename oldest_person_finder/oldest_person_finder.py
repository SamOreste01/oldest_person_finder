# Function to validate name (only alphabetic characters and non-empty)
def is_valid_name(name):
    return name.isalpha()

# Function to validate age (integer and between 1 and 120)
def is_valid_age(age):
    try:
        age = int(age)
        if 1 <= age <= 120:
            return True
        return False
    except ValueError:
        return False

# Main program
entries = []  # Array to store entries

while True:
    # Input name and validate
    name = input("Enter a name: ")
    while not is_valid_name(name):
        print("Invalid name. Please enter a valid name (only alphabetic characters).")
        name = input("Enter a name: ")

    # Input age and validate
    age = input("Enter an age: ")
    while not is_valid_age(age):
        print("Invalid age. Please enter a valid age between 1 and 120.")
        age = input("Enter an age: ")

    # Store valid name and age in entries array
    entries.append((name, int(age)))

    # Ask if the user wants to input another entry
    another_entry = input("Do you want to input another entry? (Yes/No): ").lower()
    if another_entry == 'no':
        break

# Check for the oldest person if there are any entries
if entries:
    # Find the oldest person
    oldest_person = max(entries, key=lambda person: person[1])
    print(f"The oldest person is: {oldest_person[0]} with age {oldest_person[1]}")
else:
    print("No entries available.")


