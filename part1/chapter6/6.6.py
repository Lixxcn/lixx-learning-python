people_nums = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 3,
    'e': 3,
}

people = ['a', 'e']

for key, value in people_nums.items():
    print(f"key: {key}, value: {value}")
    if(key not in people):
        print(f"邀请{key}")
    elif(key in people):
        print(f"感谢{key}")

