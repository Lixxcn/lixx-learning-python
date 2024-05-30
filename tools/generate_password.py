import string
import random

def generate_password(length=12):
    # 定义密码字符集
    characters = string.ascii_letters + string.digits + string.punctuation
    # 随机选择字符
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# 设置密码长度
password_length = 12
# 生成密码
password = generate_password(password_length)
print("随机生成的密码是:", password)
