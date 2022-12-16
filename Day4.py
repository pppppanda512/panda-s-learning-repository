for i in range(1, 10):
	for j in range(1, i + 1):
		print('%d*%d=%d' % (i, j, i * j), end='\t')
	print(end='\n')

num=int(input('请输入需要判断的数'))
import math as m
result='恭喜你，这是一个素数'
for i in range(2,int(m.sqrt(num)+1)):
    if (num%i==0):
        result='它不是素数，其最小非1因数为%i' %(i)
        break
print(result)

p=int(input('请输入一个正整数'))
q=int(input('请再输入一个正整数'))
x=max(p,q)
y=min(p,q)
while x%y!=0 :
    r=x%y
    x=y
    y=r
print('%i和%i的最大公因数为%i，最小公倍数为%i' 
      %(p,q,y,p*q/y))

row = int(input('请输入行数: '))
for i in range(row):
    for j in range(row*2-1):
        if j < row-i-1 or j>row -1+i:
            print(' ', end='')
        else:
            print('*', end='')
    print()








