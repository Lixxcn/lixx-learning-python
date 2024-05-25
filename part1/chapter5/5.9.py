users = []

if users:
    for user in users:
        if user == 'admin':
            print("Hello admin!")
        else:
            print(f"Hello {user}")
else:
    print("no user")