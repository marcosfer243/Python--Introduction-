friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends[1] = "Mike"
print(friends[1:])

# List Functions

lucky_numbers = [4, 8, 15, 16, 23, 42]
myfriends = ["Kevin", "Karen", "Jim", "Jim", "Jim", "Jim", "Oscar", "Toby"]

myfriends.extend(lucky_numbers)

myfriends.append("Creed")

myfriends.insert(2, "Kelly")

myfriends.remove("Oscar")

myfriends.pop()

print(myfriends.index("Toby"))

# myfriends.clear()

print(myfriends.count("Jim"))

lucky_numbers.sort()

print(lucky_numbers)

myfriends2 = myfriends.copy()

print(myfriends)

print(myfriends2)