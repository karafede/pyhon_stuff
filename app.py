
print("Hello World")
print("/___|")
print("   /|")
print("  / |")
print(" /  |")

# create variable
character_name = "George"
character_age = "50"
is_male = False
print("There was once a guy named " + character_name + ",")
print("he was" + character_age + " years old,")
character_name = "Tom"
print("he liked the name " + character_name + ",")
print("but he didn't like being " + character_age + ".")

phrase = "Giraffe\nAcademy"
phrase = "Giraffe Academy"
print(phrase + " is cool")

# functions with strings
print(phrase.lower() + "\n")
print(phrase.upper() + "\n")

print(phrase.isupper())
print(phrase.upper().isupper())

print(len(phrase))

print(phrase[0])
print(phrase.index("G"))
# find where the word Adademy starts..position 8
print(phrase.index("Academy"))

# print(phrase.index("z"))

print(phrase.replace("Giraffe", "Elephant"))


# functions with numbers
print(-2.567)
print(3 * 4 + 7)

# give you what is left from the division
print(10%3)

my_num = -5
print(my_num)

print(str(my_num) + " my favourite number")

print(abs(my_num))
print(pow(3, 2))   # 3^2
print(max(4, 2))
print(round(3.2))

# import all math functions
from math import *

print(floor(3.6))
print(ceil(3.6))
print(sqrt(3))

##########################################

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "!, you are " + age)

