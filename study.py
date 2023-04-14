# 测试打印变量
name = '张三'
age = 60
hobby = "吃饭、睡觉、打豆豆"

print(f'''
-----------{name} info---------
name: {name}
age: {age}
hobby: {hobby}
--------------end--------------
'''
      )

# print(f'''我的名字是：{name},年龄是：{age},爱好是：{hobby}''')

# 布尔值
f = 100
if f >= 100:
    print('成绩大于等于100')
else:
    print('成绩小于100')
print('我的姓名:' + name)

# 列表
girl = ["xiaosong", 'xiaoyun', 'backgril']
girl.insert(1, 'dd')
# del girl[2]
girl.remove('dd')  # 删除元素

girl[0:3]  # 取0~3个元素
girl[-1]  # 取最后一个
girl[0:4:2]  # 步长为:2
girl.append(["lisi", "180", '168'])  # 向列表中追加一个列表

# 常用运算符
num = range(10)
for i in num:
    print(i)

'''
+  加
-  减
*  
/  除
** 求次方
==
!=
a += b  就等同于 a = a + b

and  和
or   或者
not  取反

成员运算
in
'xiaoming' in girl  #'xiaoming' 在girl集合里面的
not in
'xiaoming' not in girl  #'xiaoming' 不在girl集合里面的
'''

# 接收用户的输入
msg = str(input('请输入你的内容:')).strip()  # strip()  去除两端空格
num = int(input('输入数字:'))

# 流程控制
if 3 > 5:
    print('yes')
elif 3 == 4:
    print("yes or no")
else:
    print('no')
'''
 if 表达式 1: 
	语句块 1 
elif表达式 2: 
	语句块 2 
elif表达式 3: 
	语句块 3
else: 
	语句块 n 
'''
