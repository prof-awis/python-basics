# properties name, number, balance
# ops withdraw, deposit, check

class Person:  # classes are created with uppercasses- good practice
    def __init__(self, name, age, gender):  # this is a constructor
        self.name = name
        self.age = age
        self.gender = gender

    def print_details(self):  # function
        print(self.name)
        print(self.age)
        print(self.gender)
        print("--------------")

    def save(self):
        details = f"Name: {self.name} Age: {self.age} Gender: {self.gender}\n"
        file = open("details.txt",
                    "a")  # Can save also in "w" mode.
        # The file is opened in append "a" mode. If the file ain't there it will be created for you
        file.write(details)
        file.close()  # close your file always. If you don't it might corrupt it

    def print_saved_details(self):
        # pass // used when you don't know what to do
        file = open("details.txt", "r")  # opening the file in read mode "r"
        for line in file:
            if self.name in line:
                print(line)
                break  # we stop the loop from running when we find what we needed
        file.close()


# creating objects = store data //funct manipulate data
p1 = Person("Jerry Jane", 21, "Female")  # instantiating classes
p2 = Person("Tom Juma", 24, "Male")
p3 = Person("Ling Liu", 23, "Male")

p1.print_details()  # calling an object
p2.print_details()
p3.print_details()

p1.save()
p2.save()
p3.save()

# Trying to print the saved details
p1.print_saved_details()
