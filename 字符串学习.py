# 字符串的定义
# 不可变、可遍历、可切片、有索引
name = 'xiaosong'
for i in name:
    print(i)

print(name[0])

# 一切字符串皆对象
# 字符串类型方法

# 1、格式化方法
s = 'xiaoqignshang'
# center(50,'-')
# '------------------xiaoqingshang-------------------'
s.strip()  
# s.format()  引用外部变量   #  msg = 'my name is {name}'.format(name = 'xiao')

# 2、判断方法
s.isalnum()  # 是不是数字or字母
s.isalpha()  # 是不是全是字母
s.isdigit()  # 是不是全是数字  只能判断整数 不能判断小数  建议使用
s.isnumeric() # 是不是数字
s.islower()   # 是不是小写

# 3、查、改、计数、替换
s.find('x')  # 查询字符  返回字符的索引  找不到会返回-1
s.index('i')  # 查询字符  找不到会报错
s.count('i')  # 计数  计算i在字符串出现的次数   可切片
s.split('.')   # 通过'.'来进行切分  默认为空格
s.replace('i','s')  # 替换 将字符串中的'i' 替换成's'


# 4、特殊的方法
# 将列表拼接成字符串
names = ['xiaoming','xiaohua','black girl']
"-".join(names)
#  输出结果为: 'xiaoming-xiaohua-black girl'
# 生成密码本
# .....
# 练习
# 统计输入的字符有多少数字、字母、特殊字符
msg = 'xiao12345 6@#$'
str_msg = 0     # 特殊字符
str_num = 0     # 数字
str_zm = 0      # 字母
str_kg = 0      # 空格
for i in msg:
    if i.isdigit():
        str_num += 1
    elif i.isalpha():
        str_zm += 1
    elif i.isspace():  # 空格
        str_kg += 1
    else:    #  特殊字符
        str_msg += 1
print(f"特殊字符{str_msg},数字{str_num},字母{str_zm},空格{str_kg}")