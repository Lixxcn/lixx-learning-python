prompt = "请输入你的年龄，我来告诉你如何收费（“q”退出）："

while(True):
    age = input(prompt)
    if age == 'q':
        break
    
    age = int(age)

    if age < 3:
        print("不收费")
    elif 3 <= age < 12:
        print("收费10元")
    else:
        print('收费15元')