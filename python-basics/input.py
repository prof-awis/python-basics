name = input("What is your name? ")
print(f"Hello {name}")

birth_year = input("Enter your birth year: ")
age = 2020 - int(birth_year);  # convert the string birth_year to integer
print(f"{name}'s age is {age}")
