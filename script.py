import random
import os

years = [1960,1965,1965,1969,1970,1974]

for x in range(1974,2023):
    years.append(x)


print("Options:")
print("\t1: Create a new draft class randomization")
print("\t2: Alter a past draft class randomization")

decision = int(input())

# Clear the screen
os.system("cls")

while(True):

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
            f = open(name, "w+")
            f.write(str(years))
            f.close()
            break
    elif decision  == 2:
        os.system("cls")
        print("What is the save name?")
        name = input(x)
        os.system("cls")

        name = "saves/" + name + ".txt"

        f = open(name, "r")

        print(f.read())

        f.close()
        break
    else:
        print("Invalid input")
        break
