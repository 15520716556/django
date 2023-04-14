count = 0
black_girl_age = 22
while count < 3:
    guess = input("猜黑姑娘的年龄>:")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("不识别指令，重新输入")
        continue
    if guess > black_girl_age:
        print("请往小猜")
    elif guess < black_girl_age:
        print("请往大猜")
    elif guess == black_girl_age:
        print("睡一晚")
        break
    count += 1
    if count == 3:
        cmd = input("要不要再试一把？（y/n)").strip()
        if cmd in ["y", "Y", "yes"]:
            count = 0
        else:
            print("bye bye")


