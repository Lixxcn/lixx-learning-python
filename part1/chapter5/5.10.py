current_users = ['A','b','c','d','e']
new_users = ['a','B','f','g','h']

current_users_lower = []

for user in current_users:
    current_users_lower.append(user.lower())
print(current_users_lower)


for user in new_users:
    if user.lower() in current_users_lower:
        print(f"{user} 用户名已存在!")
    else:
        print(f"{user} 用户名未被使用。")
    
