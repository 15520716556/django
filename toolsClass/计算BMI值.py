import os

tz = int(input('请输入体重(KG):'))
sg = float(input('请输入身高(M):'))
bmi = round(float(tz / (sg * sg)), 2)
if bmi <= 18.5:
    print('你的体重为%s过轻' % bmi)
    os.system('pause')
elif 25 > bmi > 18.5:
    print('你的体重为%s正常' % bmi)
    os.system('pause')
elif 32 > bmi >= 25:
    print('肥胖')
    os.system('pause')
else:
    print('你的体重为%s严重肥胖' % bmi)
    os.system('pause')
