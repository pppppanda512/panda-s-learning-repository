##百钱百鸡
for i in range(1,20):
    for j in range(1,34):
        z=100 -i -j
        if 5*i+3*j+z/3==100:
            print('公鸡%i只，母鸡%i只，小鸡%i只' %(i,j,z))



'''Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束'''
'''import random as r
for i in (1,1001):
  x=r.randint(1,6)
  y=r.randint(1,6)
  k=x+y
  if k==7 or 11 :
      print('玩家胜')
  elif x+y==2 or 3 or 12:
      print('庄家胜')
  else:
      p=r.randint(1,6)
      q=r.randint(1,6)
      if p+q ==7:
        print('庄家胜')
      elif p+q==k:
        print('玩家胜')'''
#赌博需要下注
money =1000
while(money>0):
    print('你的总资产为：%i' %(money))
    bet=int(input('请下注：'))
    if bet>money:
        bet=int(input('请重新下注：'))
    import random as r
    x=r.randint(1,6)
    y=r.randint(1,6)
    k=x+y
    if k==7 or 11 :
      print('你掷到了%i和%i,你赢了' %(x,y))
      money+=bet
    elif x+y==2 or 3 or 12:
      print('你掷到了%i和%i,你输了' %(x,y))
      money-=bet
    else:
      p=r.randint(1,6)
      q=r.randint(1,6)
      if p+q ==7:
        print('你第一轮掷到了%i和%i,游戏继续；\n你第二轮掷到了%i和%i\n你输了' %(x,y,p,q))
        money-=bet
      elif p+q==k:
        print('你第一轮掷到了%i和%i,游戏继续；\n你第二轮掷到了%i和%i\n你赢了' %(x,y,p,q))
        money+=bet
print('你破产了，游戏结束')

    
"""

输出斐波那契数列的前20个数
1 1 2 3 5 8 13 21 ..."""

a=0
b=1
for i in range(1,20):
    print(b,end='  ')
    (a,b)=(b,a+b)

"""

猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了

Version: 0.1
Author: 骆昊
Date: 2018-03-02

"""

import random as r
target=r.randint(1,100)
guess=int(input('来猜一猜吧：'))
counter=0
while(guess!=target):
    counter+=1
    if guess>target:
        print('小一点')
        guess=int(input('再来猜一猜吧：'))
    elif guess<target:
        print('大一点')
        guess=int(input('再来猜一猜吧：'))
print('恭喜你猜对了')
print('你一共猜了%i次' %(counter))


    
"""

找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
如: 153 = 1**3 + 5**3 + 3**3

Version: 0.1
Author: 骆昊
Date: 2018-03-02

"""

for i in range(100,1000):
    a=i//100
    b=(i%100)//10
    c=i-100*a-10*b#c=i%10
    if i==a**3+b**3+c**3 :
      print(i)

"""

判断输入的正整数是不是回文数
回文数是指将一个正整数从左往右排列和从右往左排列值一样的数

Version: 0.1
Author: 骆昊
Date: 2018-03-02

"""



"""

找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14

Version: 0.1
Author: 骆昊
Date: 2018-03-02

"""

import math as m

for i in range(1,10000):
  c=0
  for j in range(1,int(m.sqrt(i)+1)):
    if i%j==0:
      c+=j
      if j>1 and i/j!=j:
        c+=i/j
  if c==i:
    print('%i是一个完美数' %(i))

"""

输出2~99之间的素数

Version: 0.1
Author: 骆昊
Date: 2018-03-02

"""

import math as m

for i in range(2,100):
  K=True 
  for j in range(2,int(m.sqrt(i)+1)):
    if i%j==0 and j!=i:
      K=False
      break
  if K==True:
    print(i)


"""

输出乘法口诀表(九九表)

Version: 0.1
Author: 骆昊
Date: 2018-03-02

"""

for i in range(1,10):
  for j in range(1,i+1):
    print('%i*%i=%i' %(i,j,i*j),end='   ')
  print()
