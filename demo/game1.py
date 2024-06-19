import tkinter as tk
from tkinter import messagebox
import random

# 创建主窗口
window = tk.Tk()
window.title("剪刀石头布游戏")
window.geometry("400x400")

# 设置emoji表示
scissors_emoji = "✂️"
rock_emoji = "🪨"
paper_emoji = "📄"

# 显示选择结果的标签
user_choice_label = tk.Label(window, text="你选择了：", font=("Arial", 16))
user_choice_label.pack(pady=10)

comp_choice_label = tk.Label(window, text="计算机选择了：", font=("Arial", 16))
comp_choice_label.pack(pady=10)

result_label = tk.Label(window, text="结果：", font=("Arial", 16))
result_label.pack(pady=10)

# 定义游戏逻辑
def play(user_choice):
    choices = ["剪刀", "石头", "布"]
    comp_choice = random.choice(choices)
    user_choice_label.config(text=f"你选择了：{user_choice}")
    comp_choice_label.config(text=f"计算机选择了：{comp_choice}")
    
    if user_choice == comp_choice:
        result = "平局"
    elif (user_choice == "剪刀" and comp_choice == "布") or \
         (user_choice == "石头" and comp_choice == "剪刀") or \
         (user_choice == "布" and comp_choice == "石头"):
        result = "你赢了！"
    else:
        result = "你输了！"
    
    result_label.config(text=f"结果：{result}")

# 创建按钮
scissors_button = tk.Button(window, text=scissors_emoji, font=("Arial", 40), command=lambda: play("剪刀"))
scissors_button.pack(side=tk.LEFT, padx=20)

rock_button = tk.Button(window, text=rock_emoji, font=("Arial", 40), command=lambda: play("石头"))
rock_button.pack(side=tk.LEFT, padx=20)

paper_button = tk.Button(window, text=paper_emoji, font=("Arial", 40), command=lambda: play("布"))
paper_button.pack(side=tk.LEFT, padx=20)

# 运行主循环
window.mainloop()
