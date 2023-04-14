# 循环
for i in range(10):
    print("我是.", i)
# 打印奇数
for i in range(10):
    if i % 2 != 0:
        print(i)

for name in ['aaa', 'bbb', 'ccc']:
    print(name)

# 嵌套循环
# continue  跳出当前循环
# break   结束本次循环
# 标志位？？？？？？

# 打印99乘法表
for i in range(1, 10):
    for k in range(1, i + 1):
        print(f"{i}*{i}={i * i}", end=' ')
    print()  # 打印空格 可以进行换行

# 求100以内的所有素数（质数）
for i in range(2, 101):
    is_num = True  # 标志位
    for j in range(2, i):
        if i % j == 0:  # 能被整除 证明这个数就不是素数
            is_num = False
    if is_num:
        print(f'这个数就是素数.{i}')

# 打印三角形
'''
*
**
***
****
*****
****
***
**
*
'''

for i in range(11):
    if i <= 5:
        print("* " * i)
    else:
        print("* " * (10 - i))
# while
# while True:
#     i += 1
#     print(f'这是第{i}次打印')

# 实现猜年龄小游
count = 0
while True:
    input_age = input('请输入你要猜的数字:')
    if input_age.isdigit():
        count += 1
        age = int(input_age)
        if count < 3:
            if age < 18:
                print('你菜太小了')
            if age > 18:
                print('你猜太大了')
            if age == 18:
                print('恭喜你 猜对了 ')
                break
        else:
            input_yes_no = input('是否继续继续游戏(yes?no)').strip()
            if input_yes_no in ['Y', 'y', 'YES', 'yes']:
                count = 0
                print('请继续游戏')
            elif input_yes_no in ['N', 'n', 'NO', 'no']:
                print('游戏已退出')
                break
    else:
        print('只能输入数字！！！！！')

#  for.....else...
for i in range(10):
    if i == 5:
        break
else:  # 当循环正常结束时（没有被break、exit....）的时候，则执行...
    print('rexx')
