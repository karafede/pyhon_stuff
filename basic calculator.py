
#########################################
# build a basic calculator

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
# result = int(num1) + int(num2)
result2 = float(num1) + float(num2)
# print(result)
print(result2)

##########################################
# Mad libs

color = input("enter a colour: ")
plural_noun = input("enter a plural noun: ")
celebrity = input("enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)

##########################################
### building a better calculator

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else:
    print("invalid operator")