prompt = "\n输入调料（结束时输入“退出”）："

while True:
    tl = input(prompt)

    if tl == '退出':
        break

    print(f"加入调料：{tl}")

