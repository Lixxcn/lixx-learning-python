people = ['aa', 'bb', 'cc']
print(people)
print(people.pop(1))
people.insert(1, "dd")
print(people)

people.insert(0, "ee")
people.insert(2, "ff")
people.append("gg")

print(people)

print("sorry,", people.pop())
print("sorry,", people.pop())
print("sorry,", people.pop())
print("sorry,", people.pop())

print("hello,", people[0])
print("hello,", people[1])

del people[0]
del people[0]

print(people)

