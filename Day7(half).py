##认识列表

def main():
    str1 = 'hello, world!'
    # 通过len函数计算字符串的长度
    print(len(str1))  # 13
    # 获得字符串首字母大写的拷贝
    print(str1.capitalize())  # Hello, world!
    # 获得字符串变大写后的拷贝
    print(str1.upper())  # HELLO, WORLD!
    # 从字符串中查找子串所在位置
    print(str1.find('or'))  # 8
    print(str1.find('shit'))  # -1
    # 与find类似但找不到子串时会引发异常
    # print(str1.index('or'))
    # print(str1.index('shit'))
    # 检查字符串是否以指定的字符串开头
    print(str1.startswith('He'))  # False
    print(str1.startswith('hel'))  # True
    # 检查字符串是否以指定的字符串结尾
    print(str1.endswith('!'))  # True
    # 将字符串以指定的宽度居中并在两侧填充指定的字符
    print(str1.center(50, '*'))
    # 将字符串以指定的宽度靠右放置左侧填充指定的字符
    print(str1.rjust(50, ' '))
    str2 = 'abc123456'
    # 从字符串中取出指定位置的字符(下标运算)
    print(str2[2])  # c
    # 字符串切片(从指定的开始索引到指定的结束索引)
    print(str2[2:5])  # c12
    print(str2[2:])  # c123456
    print(str2[2::2])  # c246
    print(str2[::2])  # ac246
    print(str2[::-1])  # 654321cba
    print(str2[-3:-1])  # 45
    # 检查字符串是否由数字构成
    print(str2.isdigit())  # False
    # 检查字符串是否以字母构成
    print(str2.isalpha())  # False
    # 检查字符串是否以数字和字母构成
    print(str2.isalnum())  # True
    str3 = '  jackfrued@126.com '
    print(str3)
    # 获得字符串修剪左右两侧空格的拷贝
    print(str3.strip())


if __name__ == '__main__':
    main()

def main():
    list1=[1, 3, 5, 7, 100]
    print(list1)
    list2 = ['hello'] * 5
    print(list2)
	# 计算列表长度(元素个数)
    print(len(list1))
	# 下标(索引)运算
    print(list1[0])
    print(list1[4])
	# print(list1[5])  # IndexError: list index out of range
    print(list1[-1])
    print(list1[-3])
    list1[2] = 300
    print(list1)
	# 添加元素
    list1.append(200)
    list1.insert(1, 400)
    list1 += [1000, 2000]
    print(list1)
    print(len(list1))
	# 删除元素
    list1.remove(3)
    if 1234 in list1:
        list1.remove(1234)
    del list1[0]
    print(list1)
	# 清空列表元素
    list1.clear()
    print(list1)
	
	
	
   

if __name__ == '__main__':
	main()

def main():
	fruits = ['grape', 'apple', 'strawberry', 'waxberry']
	fruits += ['pitaya', 'pear', 'mango']
	# 循环遍历列表元素
	for fruit in fruits:
		print(fruit.title(), end=' ')
	print()
	# 列表切片
	fruits2 = fruits[1:4]
	print(fruits2)
	# fruit3 = fruits  # 没有复制列表只创建了新的引用
    # 可以通过完整切片操作来复制列表
	fruits3 = fruits[:]
	print(fruits3)
	fruits4 = fruits[-2:-4:-1]
	print(fruits4)
    # 可以通过反向切片操作来获得倒转后的列表的拷贝
	fruits5 = fruits[::-1]
	print(fruits5)


if __name__ == '__main__':
	main()


def main():
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    list2 = sorted(list1)
    # sorted函数返回列表排序后的拷贝不会修改传入的列表
    # 函数的设计就应该像sorted函数一样尽可能不产生副作用
    list3 = sorted(list1, reverse=True)
    # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
    list4 = sorted(list1, key=len)
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    # 给列表对象发出排序消息直接在列表对象上进行排序
    list1.sort(reverse=True)
    print(list1)


if __name__ == '__main__':
    main()

##生成列表
import sys

def main():
    f = [x for x in range(1, 10)]
    print(f)
    f = [x + y for x in 'ABCDE' for y in '1234567']
    print(f)
    # 用列表的生成表达式语法创建列表容器
    # 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
    f = [x ** 2 for x in range(1, 1000)]
    print(sys.getsizeof(f))  # 查看对象占用内存的字节数
    print(f)
    # 请注意下面的代码创建的不是一个列表而是一个生成器对象
    # 通过生成器可以获取到数据但它不占用额外的空间存储数据
    # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
    f = (x ** 2 for x in range(1, 100))
    print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
    print(f)
    for val in f:
        print(val)


if __name__ == '__main__':
    main()

##使用元组
def main():
	# 定义元组
	t = ('骆昊', 38, True, '四川成都')
	print(t)
	# 获取元组中的元素
	print(t[0])
	print(t[3])
	# 遍历元组中的值
	for member in t:
		print(member)
	# 重新给元组赋值
	# t[0] = '王大锤'  # TypeError
	# 变量t重新引用了新的元组原来的元组将被垃圾回收
	t = ('王大锤', 20, True, '云南昆明')
	print(t)
	# 将元组转换成列表
	person = list(t)
	print(person)
    # 列表是可以修改它的元素的
	person[0] = '李小龙'
	person[1] = 25
	print(person)
    # 将列表转换成元组
	fruits_list = ['apple', 'banana', 'orange']
	fruits_tuple = tuple(fruits_list)
	print(fruits_tuple)


if __name__ == '__main__':
	main()

##使用集合

def main():
    set1 = {1, 2, 3, 3, 3, 2}
    print(set1)
    print('Length =', len(set1))
    set2 = set(range(1, 10))
    print(set2)
    set1.add(4)
    set1.add(5)
    set2.update([11, 12])
    print(set1)
    print(set2)
    set2.discard(5)
    # remove的元素如果不存在会引发KeyError
    if 4 in set2:
        set2.remove(4)
    print(set2)
    # 遍历集合容器
    for elem in set2:
        print(elem ** 2, end=' ')
    print()
    # 将元组转换成集合
    set3 = set((1, 2, 3, 3, 2, 1))
    print(set3.pop())
    print(set3)
    # 集合的交集、并集、差集、对称差运算
    print(set1 & set2)
    # print(set1.intersection(set2))
    print(set1 | set2)
    # print(set1.union(set2))
    print(set1 - set2)
    # print(set1.difference(set2))
    print(set1 ^ set2)
    # print(set1.symmetric_difference(set2))
    # 判断子集和超集
    print(set2 <= set1)
    # print(set2.issubset(set1))
    print(set3 <= set1)
    # print(set3.issubset(set1))
    print(set1 >= set2)
    # print(set1.issuperset(set2))
    print(set1 >= set3)
    # print(set1.issuperset(set3))


if __name__ == '__main__':
    main()


##字典
def main():
	scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
    # 通过键可以获取字典中对应的值
	print(scores['骆昊'])
	print(scores['狄仁杰'])
    # 对字典进行遍历(遍历的其实是键再通过键取对应的值)
	for elem in scores:
		print('%s\t--->\t%d' % (elem, scores[elem]))
    # 更新字典中的元素
	scores['白元芳'] = 65
	scores['诸葛王朗'] = 71
	scores.update(冷面=67, 方启鹤=85)
	print(scores)
	if '武则天' in scores:
		print(scores['武则天'])
	print(scores.get('武则天'))
    # get方法也是通过键获取对应的值但是可以设置默认值
	print(scores.get('武则天', 60))
    # 删除字典中的元素
	print(scores.popitem())
	print(scores.popitem())
	print(scores.pop('我', 120))
    # 清空字典

	print(scores)


if __name__ == '__main__':
	main()




#### 练习1：在屏幕上显示跑马灯文字
import os
import time


def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()

#### 练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
import random

def vertification_code(code_length=6):
    storage='1234567890qwertyuiopasdfghjklzxcvbnm'
    code=''
    for _ in range(code_length):
        index=random.randint(0,len(storage))
        code +=storage[index]
    return code

#### 练习3：设计一个函数给文件返回后缀名

def get_suffix(filename, has_dot=False):
    dot=filename.rfind('.')
    if 0 < dot < len(filename) - 1:
        if has_dot :
            index=dot
        else:
            index=dot+1
        return filename[index:]
    else:
        return ''

#### 练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。

def finding_max2(list1=[]):
    max_st=max(list1)
    list1.remove(max_st)
    max_nd=max(list1)
    return max_st,max_nd


def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2



#### 练习5：计算指定的年月日是这一年的第几天

def is_leap_year(year):
    return year%400==0 or year%100!=0 and year%4==0

def which_day(year,month,day):
    if is_leap_year(year)==True:
        day_calendar=[31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        day_calendar=[31,28,31,30,31,30,31,31,30,31,30,31]
    number=0
    for i in range(month-1):
        number+=day_calendar[i]
    number+=day
    return number

which_day(2022,11,27)

#### 练习6：打印[杨辉三角]。

