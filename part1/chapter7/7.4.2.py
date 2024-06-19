active = True

while active:
    prompt = "\n输入调料（结束时输入“退出”）："
    tl = input(prompt)
    if tl == '退出':
        active = False
        continue
    print(f"加入调料：{tl}")

