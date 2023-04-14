# 双色球选购程序
# 红球 1~36
# 篮1球 1~16

red_ball = []
blue_ball = []
red_count = 0
while True:
    if red_count < 6:
        selection = input(f'请输入你要选择的第{red_count+1}红球：').strip()
        if selection.isdigit():
            selection = int(selection)
            if (0 < selection < 36) and selection not in red_ball:
                red_ball.append(selection)
                red_count = red_count + 1
            else:
                print(f'第{red_count}个红球你输入错误 请重新输入')
                continue
        else:
            print('选择的数不合法')
            continue
    else:
        selections = input('请选择你的蓝球数：').strip()
        if not selections.isdigit():
            print('蓝色的球输入不合法')
        selections = int(selections)
        if 0 < selections <= 16:
            blue_ball.append(selections)
            print(red_ball, blue_ball)
            break
        else:
            print('蓝色的球输入不合法')


