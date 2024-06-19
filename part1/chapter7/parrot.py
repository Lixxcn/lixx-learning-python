prompt = "\n给我说什么，我就给你回复什么"
prompt += "（输入'q'退出这个程序）："

active = True
while active:
    message = input(prompt)

    if message == 'q':
        active = False
    else:
         print(f"你输入的内容为：{message}")

print("\n退出程序\n")
