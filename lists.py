
lucky_numbers = [4, 8, 15, 16, 23, 42, 23, 34, 67, 100]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

friends[1] = "Mike"

print(friends[2])
print(friends[-2])

print(friends[1:4])

# append another lists
friends.extend(lucky_numbers)
print(friends)

# append another element
friends.append("Federico")
print(friends)

# insert another element in between
friends.insert(1, "Kelly")
print(friends)

# remove elements
friends.remove("Kelly")
print(friends)
friends.clear()
print(friends)

friends = ["Kevin", "Karen", "Jim", "Jim", "Jim", "Oscar", "Toby"]
print(friends.index("Karen"))
print(friends.count("Jim"))

# sort the list
friends.sort()
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(friends)
print(lucky_numbers)

# copy a list

friends2 = friends.copy()
print(friends2)