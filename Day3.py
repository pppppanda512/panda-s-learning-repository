#### 练习1：英制单位与公制单位互换


a=float(input('请输入长度='))
b=input('请输入单位=')
if b=='英寸' or 'in':
    c=a*2.54
    print('%.2f英寸=%.2f厘米' %(a,c))
else:
    c=a/2.54
    print('%.2f厘米=%.2f英寸' %(a,c))  #有其他情况退回更好

    
a=float(input('请输入长度='))
b=input('请输入单位=')
if b=='英寸' or 'in':
    c=a*2.54
    print('%.2f英寸=%.2f厘米' %(a,c))
elif b=='厘米' or 'cm':
    c=a/2.54
    print('%.2f厘米=%.2f英寸' %(a,c))
else: 
    print('请输入有效单位') 

### 练习2：掷骰子决定做什么

from random import randint
value=randint(1,6)
if value==1:
    print('吃')# result='吃'
elif value==2:
    print('喝')
elif value==3:
    print('玩')
elif value==4:
    print('睡')
elif value==5:
    print('唱')
else:
    print('逛')
# print(result)

#### 练习4：输入三条边长如果能构成三角形就计算周长和面积

a=float(input('请分三次输入您想要用来构成三角形的三边长度'))
b=float(input('请继续输入您想要用来构成三角形的另一边长度'))
c=float(input('请继续输入您想要用来构成三角形的另一边长度'))
if a+b>c and a+c>b and b+c>a :
    cosA=(b**2+c**2-a**2)/(2*b*c)
    import math as m
    sinA=m.sqrt(1-cosA**2)
    area=1/2*b*c*sinA
    #	p = (a + b + c) / 2
	#area = math.sqrt(p * (p - a) * (p - b) * (p - c))海伦公式
    C=a+b+c
    print('可构成三角形，其面积=%.2f，周长=%.2f' %(area,C))
else:
    print('您输入的三边长不能构成三角形，请重新输入')


