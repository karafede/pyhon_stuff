
# read only
employee_file = open("employees.txt", "r")

# write
# open("employees.txt", "w")
# append information
# open("employees.txt", "a")
# read and write
# open("employees.txt", "r+")


# print(employee_file.readable())
# print(employee_file.read())

# print(employee_file.readlines())
# print(employee_file.readlines()[1])

for employee in employee_file.readlines():
    print(employee)

employee_file.close()