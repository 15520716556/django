# 列表的特性
# 有序 有索引、可切片、可遍历、可修改


# 列表的增删改查
s = 'xiaoqingshang'
li = list(s)
# 添加
li.append('song')
# li.insert('xia')
# 删除
# li.pop()   # 默认删除最后一个 可加参数 li.pop(1)  根据索引删除
# li.remove('x')   # 根据内容删除li.remove('x')
# del li['x']   # 删除变量
# 列表的切片
# li[0:5]  # 从0开始 切5个
# li[0:]   # 全部切
# 步长  默认步长为1
li[0:9:2]  # 从0开始切9个,步长设置为2 ，就相当于没隔两个切一次，全部切也可以：li[::2]

# 反转
li[::-1]  # li[1,2,3,4] 反转后 li[4,3,2,1]

# 查
# 特殊方法
li.reverse()  # 反转列表 会生成一个新的列表
li.sort()   # 列表排序
li2 = [1, 2, 'ww']
li.extend(li2)  # 合并列表  会生成一个新的列表  也可以使用 li + li2


# 复制copy 列表
li.copy()  # 浅复制  如果有嵌套列表 只是负责引用的地址 修改其中的一个嵌套列表 另一个也会变
# import  copy
# copy.deepcopy()   # 深复制  完全的复制一个列表 修改后不会影响另一个

# 列表的生成式
emp = []
for i in range(11):
    emp.append(f'str->{i}')

print(emp)

# 高级列表生成式
[f'str->{i}' for i in range(11)]


# 列表的练习题
'''
1、列表的去重  不能使用set
2、找到列表中第2大的值
3、统计列表中每个字符出现的次数 不能使用dict
4、判断一个列表是不是另一个列表的子列表
5、求出列表中，离最大值 和最小值 的平均 值 最近的值
'''


# 练习题1 列表的去重1
li_list = [1, 2, 555, 2, 666, 999, 45, 888, 555, 666, 2]
li_list1 = []     # 去重后的列表
for i in li_list:
    if i not in li_list1:
        li_list1.append(i)
print(li_list1)

# 练习题1 列表的去重2
li_list = [1, 2, 555, 2, 666, 999, 45, 888, 555, 666, 2, 555,9999]
li_nums = []

for i in li_list:
    if li_list.count(i) > 1 and [i, li_list.count(i)] not in li_nums:
        li_nums.append([i, li_list.count(i)])
for j in li_nums:
    num, times = j
    for k in range(times-1):
        li_list.remove(num)
print('去重后的list:',li_list1)


# 求列表的最大值
li_list = [1, 2, 555, 2, 666, 999, 45, 888, 555, 666, 2, 555, 8888, 9999]
max_n = li_list[0]
for i in li_list:
    if i > max_n:
        max_n = i
print(max_n)
# 练习题2  找到列表中第2大的值        ---------------已完成
# 思路 先将列表排序 然后取倒数第二个
# li_list.sort()
# li_list[-2]

# 练习题 3  统计列表中每个字符出现的次数   -----------算半完成 有点小bug
li_str = list('Adair')
str_num = 0
for i in li_str:
    str_num = li_str.count(i)
    print(f"{i}出现的次数是{str_num}")

# 练习题 4 判断一个列表是不是另一个列表的子列表
# 解题思路   li列表的值全部在li_list里面才算子列表
li_list = [1, 2, 555, 2, 666, 999, 45, 888, 555, 666, 2, 555, 9999, 4998]
li = [1, 666, 555, 7777]
is_list = True
for i in li:
    if i not in li_list:is_list = False
if is_list:
    print('是子列表')
else:
    print('不是子列表')

# 练习题 5 求出列表中，离 最大值和最小值的平均值 最近的值
# 分析 用平均值去减去列表中的所有值,最小的那个就是离平均值最近的一个
li_list = [1, 2, 555, 2, 666, 999, 45, 888, 555, 666, 2, 4998 , 555, 9999]
li_list.sort()
li_max = li_list[-1]
li_min = li_list[0]
li_avg = (li_min+li_max)/2
print('平均值是：', li_avg)
current_n = li[0] # 默认为第一最近
for i in li_list:
    # 平均值减当前列表的值  小于 平局值减去current_n  如果条件成立 就将i的值赋给current_n
    if abs(li_avg - i) < (li_avg - current_n):
        current_n = i
print('离 最大值和最小值的平均值 最近的值是:', current_n)
