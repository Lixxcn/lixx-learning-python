from pathlib import Path

path = Path("part1/chapter10/编程.txt")

# win
# path.write_text("我喜欢编程。",encoding="utf-8")

# linux
contents = "我喜欢编程。\n"
contents += "我喜欢创建"
path.write_text("我喜欢编程。")
