import random

# 练习题1
# 存款多少年能翻倍？
#  1、10000本金，利息每年0.0325，问连本带息多少年能翻倍
principal = 10000
interest_rate = 0.0325
year = 0

while True:
    principal += principal * interest_rate
    year += 1
    if principal > 20000:
        print(f"总共存了{year}年,本金、利息一共:{round(principal,2)}")
        break

# 练习题2
# 计算小球坠落的长度
# 一个小球，从100米高空坠落，每次反弹会原来的一半高度，问第十次反弹完，小球经过多少米

height = 100
count = 0
num = 0
while True:
    num = num + height  # 计算掉下来的高度 第一次为100米
    height = height / 2  # 当小球掉下来后会反弹高度的一半
    num = num + height  # 掉下来的高度 + 上反弹回去的高度
    count += 1  # 每一次加1
    if count == 10:
        print(f'小球共掉了{count}次，共计{num}米')
        break

# 练习题3  猴子吃桃子
# 有一堆桃子  猴子每天吃总数的一半并多吃了一个，吃了10天，到第11天的只剩一个桃子，问猴子吃之前一共是多少个挑子
# 分析  先计算第10天有多少挑子  (1+1)*2 = 4    第9天 （4+1）* 2
pick = 1
day = 11
while day > 1:
    pick = (1 + pick) * 2
    day -= 1
    print(day, pick)

# 练习题4
# 计算 1-2+3—4+5-6......100的和
odd_number = 0
even_number = 0
sum_number = 0
for i in range(101):
    if i % 2 == 0:
        sum_number -= i
    else:
        sum_number += i
print(sum_number)

num = 0
for i in range(101):
    num = num + i
print(num)
# 求列表的最大值、最小值
num_list = [99, 231, 41, 5, 2352, 535, 235245, 2342, 99999999999999]
max_n = num_list[0]
for i in num_list:
    if i > max_n:
        max_n = i
print(max_n)

# 求两个列表中的数据总和加起来等于10，如果相等 就打印两个数
print('求两个列表中的数据总和加起来等于10，如果相等 就打印两个数')
data1 = [1, 23, 4, 5, 643, 645, 657, 7457, 8676, 86, 123, 1]
data2 = [9, -13, 6, 5]
for i in data1:
    for j in data2:
        if i + j == 10:
            print([i, j])

# 练习题
# 年会抽奖程序
# 员工有300名，年会抽奖奖项如下
# 一等奖 3名，iphone 12plus手机各一部
# 二等奖 6名，奖金1000块
# 三等奖 30名，京东卡200元
# 规则
# 共抽奖3次，第一次抽3等奖，第2次抽二等奖，第3次抽一等奖，每个员工共只限中奖一次，不能重复
# print('======================开始=========================')
# staff = range(1, 301)   # 员工的数量
# num_1 = random.sample(staff, 30)   # 中三等奖的员工
# num_2 = []       # 未中三等奖的人员
# for i in staff:
#     if i not in num_1:
#         num_2.append(i)
# num_3 = random.sample(num_2,6)     # 中二等奖的人员
# num_4 = []     # 未中奖的员工
# for i in num_2:
#     if i not in num_3:
#         num_4.append(i)
# num_one = random.sample(num_4, 3)
# print('中三等将的员工')
# print(num_1)
# print('中二等将的员工')
# print(num_3)
# print('中一等将的员工')
# print(num_one)
# not_num = []
# for i in num_4:
#     if i not in num_one:
#         not_num.append(i)
# print('未中奖的员工')
# print(not_num)
# print('======================抽奖结束=========================')

print('======================开始=========================')
luck_draw_num = 0  # 抽奖的次数
staff = list(range(1, 301))  # 员工的数量
num = 0
num_luck = 4
while True:
    if luck_draw_num < 3:
        luck_draw_num += 1
        num_luck -= 1
        if luck_draw_num == 1:
            num = 30
        elif luck_draw_num == 2:
            num = 6
        elif luck_draw_num == 3:
            num = 3
        luck_num = random.sample(staff, num)
        print(f'{num_luck}等奖:{luck_num}')
        for i in luck_num:
            staff.remove(i)
    else:
        break
print('======================抽奖结束=========================')


