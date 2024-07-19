# Define the function to find the youngest age
def find_youngest(jack_age, alex_age, lana_age):
    return min(jack_age, alex_age, lana_age)

# Read the ago of each person
jack_age = int(input("Enter Jack's age: "))
alex_age = int(input("Enter Alex's age: "))
lana_age = int(input("Enter Lana's age: "))

# Find and print the youngest age
youngest = find_youngest(jack_age, alex_age, lana_age)
print("The youngest age is:", youngest)