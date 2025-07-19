print("Welcome, Agent")

first_name= input("Enter your first Name: ")
color=input("Pick your favorite Color: ")
animal=input("Pick your favorite animal: ")
number=input("Favorite number: ")

#Simple Check
if first_name.lower() == "james":
    print("Bond? is That you?!")


# Code name output
print("\nYour secret agent name is:")
print(f"Agent {color.capitalize()} {animal.capitalize()}-{number.zfill(2)}")

