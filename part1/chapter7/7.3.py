number = input("请输⼊⼀个数，我会指出这个数是否是 10的整数倍：")
number = int(number)

if number % 10 == 0:
    print(f"\n{number}是10的整数倍。")
else:
    print(f"\n{number}不是10的整数倍。")