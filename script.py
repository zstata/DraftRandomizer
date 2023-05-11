import random
import os

years = [1960,1965,1965,1969,1970,1974]

for x in range(1964,2023):
    years.append(x)


print("Options:")
print("\t1: Create a new draft class randomization")
print("\t2: Alter a past draft class randomization")

decision = int(input())

while(True):
    # Clear the screen
    os.system("cls")

    if decision == 1:
        random.shuffle(years)
        print("Your randomized class list is as follows:")
        print(years)

        print("This one look good? (yes/no)")

        d2 = input()
        os.system("cls")

        if d2.startswith('y'):
            print("Enter a file name: ")
            name = input()
            os.system("cls")

            name = "saves/" + name + ".txt"

            # Write the list to a file
            f = open(name, "w")
            f.write(years)
    elif decision  == 2:
        print(2)
    else:
        print("Invalid input")
