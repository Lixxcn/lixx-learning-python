import random

def get_user_choice():
    choice = input("请输入你的选择（剪刀/石头/布）：")
    while choice not in ["剪刀", "石头", "布"]:
        choice = input("无效选择，请重新输入（剪刀/石头/布）：")
    return choice

def get_computer_choice():
    return random.choice(["剪刀", "石头", "布"])

def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "平局"
    elif (user_choice == "剪刀" and comp_choice == "布") or \
         (user_choice == "石头" and comp_choice == "剪刀") or \
         (user_choice == "布" and comp_choice == "石头"):
        return "你赢了！"
    else:
        return "你输了！"

def play():
    user_choice = get_user_choice()
    comp_choice = get_computer_choice()
    print(f"你选择了：{user_choice}")
    print(f"计算机选择了：{comp_choice}")
    result = determine_winner(user_choice, comp_choice)
    print(f"结果：{result}")

if __name__ == "__main__":
    play()
