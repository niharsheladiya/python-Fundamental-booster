print("Welcome to the Interactive Personal Data Collector!")

name = input("\nPlease enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
favno = int(input("Please enter your favourite number: "))

print("\nThank you! Here is the information we collected: ")

print(f"\nName: {name} (Type: {type(name)}, Menory Address: {id(name)})")
print(f"Age: {age} (Type: {type(age)}, Menory Address: {id(age)})")
print(f"Height: {height} (Type: {type(height)}, Menory Address: {id(height)})")
print(f"Favourite Number: {favno} (Type: {type(favno)}, Menory Address: {id(favno)})")
currentage = 2026
birthyear = currentage - age

print(f"\nYour birth is approximately: {birthyear} (based on your age of {age})")

print(f"\nThank you for using the Personal Data Collector. Goodbye!")
