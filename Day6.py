#### 练习1：实现计算求最大公约数和最小公倍数的函数。

def gcd(x,y):
    m=min(x,y)
    result=0
    for i in range(int(m),1,-1):
        if x%i==0 and y%i==0:
            result=i
            break
        else:
           result=1
    return result

if __name__=='__main__':
    print(gcd(997,689))

def lcm(x,y):
    g=gcd(x,y)
    return int(x*y/g)#x*y//g

if __name__=='__main__':
    print(lcm(12,18))

#### 练习2：实现判断一个数是不是回文数的函数。

def palindrome(x):
    new_x=0
    mid=x
    while mid>0:
        new_x*=10
        new_x+=mid%10
        mid//=10
    if new_x==x:
        return True
    else:
        return False

if __name__=='__main__':
    palindrome(76567)

#### 练习3：实现判断一个数是不是素数的函数。
def if_prime(i) :   
    import math as m

    c=True
    if i==1:
        c=False
    else:
       for j in range(2,int(m.sqrt(i))+1):
        if i%j==0:
            c=False
            break

    return c

if __name__=='__main__':
    if_prime(76567)

#### 练习4：写一个程序判断输入的正整数是不是回文素数。

x=int(input('请输入需要判断的正整数'))
if if_prime(x)==True and palindrome(x)==True:
    print('%i是回文素数'%(x))
elif if_prime(x)==True and palindrome(x)==False:
    print('%i是素数，但不回文'%(x))
elif if_prime(x)==False and palindrome(x)==True:
    print('%i是回文数，但不是素数'%(x))
else:
    print('%i既不是回文数，也不是素数' %(x))


def foo():
    global a
    a=200
    b = 'hello'
    c=False
    def bar():  # Python中可以在函数内部再定义函数
        nonlocal b
        c = True
        b='hi'
        print(a)
        print(b)
        print(c)
        
    bar()
    print(c)  # NameError: name 'c' is not defined

if __name__=='__main__':
    a=100
    foo()