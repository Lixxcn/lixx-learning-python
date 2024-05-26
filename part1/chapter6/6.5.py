people_nums = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 3,
    'e': 3,
}

for key, value in people_nums.items():
    print(f"key: {key}, value: {value}")

for key in people_nums.keys():
    print(f"key: {key}")

for value in people_nums.values():
    print(f"value: {value}")