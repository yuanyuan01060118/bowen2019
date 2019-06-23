# -*- coding:utf-8  -*-
# print ("hello")
# # #join
# # a=[12,1,2]
# # b=[1,2,3,a,24]
# # c=b.copy()
# # b.append(100)
# # print(b)
# # print(c)
# a='use{}'
# b=a.format(1)
# print(b)
# a='use{sex}123{name}'
# b=a.format(name='zlq',sex='qwe')
# print(b)
# a='123'
# print(type(a))
# a=set(a)
# print(type(a))
# #fplskdfp
# a=input('>>>')
# a=int(a)
# if a > 3:
#      print('hello')
# elif a < 2:
#      print('123')
# elif a==3:
#      print('asd')
# else:
#      print(1000)
# a=input('>>>')
# a=int(a)
# if a>=90:
#      print("优秀")
# elif a>=80 and a<90:
#      print("良好")
# elif a >= 70 and a<80:
#      print('及格')
# a=input('>>>')
# a=int(a)
# if a%2==0:
#    if a%3==0:
#       print("helloworld")
#    else:
#         print("hello")
# elif a%3==0:
#  print("world")
# else:


# a=1
# sum=0
# for  i  in range(a,101):
#     sum=sum+i
# print(sum)


# sum=0
# sam=0
# for i in range (1,100,2):
#     sum= sum + i
# for n in range (2,100,2):
#        sam=sam+n
# s=sum-sam
# print(s)

# import random
# a = random.randrange(1,10)
# for  c in range(1,4,1):
#     b = input('>>>')
#     b = int(b)
#     if b ==a:
#         print('恭喜')
#         break
#     elif b<a:
#        print('小了还有{}次机会'.format(3-c))
#        continue
#     else:
#         print('大了还有{}次机会'.format(3-c))
# else:
#     print('菜')

# a =[1,2,3,4]
# for i in enumerate(a):
#     print(i)
#
# for i in range (1,10,1):
#     for j in  range (1,10):
#         if j <= i:
#             print("{}*{}={}".format(j,i,i*j),end='\t')
#             if i==j:
#                 print("{}*{}={}".format(i,j,i*j))


# s=0
# for a in range(2,101,1):
#     for b in range(2,101,1):
#         c=a%b
#         if c==0:
#             break
#     if a==b:
#      s=s+a
# print(s)

# 1000以内的水仙花数
# for a in range(100,1000,1):
#     b=a//100
#     c=a//10%10
#     d=a%10
#     if a==b**3+c**3+d**3:
#       print(a)


# 1000以内因数之和等于他本身
# for a in range (1,1001):
#     s = 0
#     for b in range (1,1000):
#         if b<a and a%b==0:
#             s=s+b
#     if a==s:
#          print(a)


# a=0
# for i in range (0,1000,7):
#     print(i)
#     a=a+1
#     if a==20:
#         break
#
# 乘法表：
# for i in  range(1,10):
#     for j in range(1,10):
#         if j<=i:
#             print('{}*{}={}'.format(j,i,j*i),end='\t')
#         if j==i:
#          print()
# sum=0
# for i in range(2,100):
#     for j in range(2,100):
#         if i % j==0:
#             break
#     if i==j:
#        sum=sum+i
# print(sum)
# 回文字符串
# a=input('字符串')
# a=str(a)
# if a==a[::-1]:
#     print('回文字符串')
# else:
#     print('不回文字符串')


# i = 1
# s=0
# i=int(i)
# s=int(s)
# while i <=100:
#    i=i+1
#    s=s+i
# print(s)
#
# while True:
#     a = input('>>>')
#     a = a.split(',')
#     for i,j in enumerate(a):
#        a[i]=int(j)
#     b=sum(a)//len(a)
#     print('平均数{}'.format(b))
#     for k in a:
#        if k < b:
#           print('低于平均数的有{}'.format(k))
#     if a[0] < 0:
#          break

# a = [i**2 for i in range(6) if i >2]
# print(a)
# 求出平均数，显示低于平均数的分数
# while True:
#    a = input('>>>')
#    a = a.split(',')
#    a=[int(i) for i in a ]
#    b=sum(a)//len(a)
#    if a[0]<0:
#        break
#    print('平均数{}'.format(b))
#    s=[ k for k in a if k < b]
#    print(s)
# 删除重复：
# a=input('一组数')
# a = a.split(',')
# a=[int(s) for s in a ]
# for i in a:
#     while a.count(i)>1:
#         a.remove(i)
#         print(a)

# a=[1,2,3,4,45,5,2,23,4]
# for i in a:
#     b=a.count(i)
#     if b > 1:
#         for j in range(b-1):
#             a.remove(i)
#     print(a)

# a=[12,12,13,4,5,6]
# for i in a:
#  i=[]
# if i not in a:
#     i.append(a)
#     print(i)


# f = open('a.txt','w',encoding='utf-8' )
# f.write('asadsf')
# f.close()
# 文件写入99乘法表
# f = open('c.txt','w',encoding='utf-8' )
# for i  in range(1,10):
#     for j in range(1,i+1):
#        if j<i:
#            f.write('{}*{}={}\t'.format(j,i,j*i))
#        if j==i:
#            f.write('{}*{}={}'.format(j, i, j *i))
#     f.write('\n')
# f.close()
# f = open(r'c.txt','r',encoding='utf-8' )
# b =f.readline()
# c=f.readline()
# print(b,c)
# f.close()
#
# 过滤出文件以abc开头的

# f = open(r'a.txt','r',encoding='utf-8' )
# i=f.readlines()
# for b in i:
#  if b[:3] == 'abc':
#    print(b)
# f.close()
# 过滤出文件15到20行的内容
# f = open(r'a.txt','r',encoding='utf-8' )
# for i in range(1,21):
#     b = f.readline()
#     if i>=15:
#         print(b)
# a=0
# b=1
# for s in range(1,4):
#     b=b*s
#     a=a+b
#     print(a)

# 三角形的判断
# a = input('第一个数')
# # a=int(a)
# # b =input('第二个数')
# # b=int(b)
# # c=input('第三个数')
# # c=int(c)
# # if a < b+c and b < a+c and c < a+b:
# #   print('为三角形')
# # else:
# #    print('不是三角形')

# 三角形的判断：
# a = input("边长")
# a = a.split(",")
# a = [int(i) for i in a]
# if a[0]<a[1]+a[2] and a[1]<a[0]+a[2] and a[2]<a[0]+a[1]:
#  print('为三角形')
# else:
#   print('不是三角形')

#
# a=int ( input ("一组数"))
# b=a.startswitch('123')
# print(b)
# a=input("一组数")
# a=a.split(",")
# a=int(a)
# b = []
# for b in a:
#     while a.count(b)>1:
#         a.remove(b)
#         print(a)
# 排序（选择、冒泡）
# a=input ("一组数")
# a=a.split(',')
# a = [int(i) for i in a]
# b=len(a)
# for i in range(1,b):
#  for j in range(b-1):
#     if a[j+1] < a[j]:
#       t=a[j]
#       a[j]=a[j+1]
#       a[j+1]=t
# print(a)

# a=input ("一组数")
# a=a.split(',')
# a = [int(x) for x in a]
# for b in range(0,len(a)-1):
#      if a[b+1] < a[b]:
#       t=a[b]
#       a[b]=a[b+1]
#       a[b+1]=t
#       print(a)

# 选择法
# a=input ("一组数")
# a=a.split(',')
# a = [int(i) for i in a]
# b=len(a)
# for i in range(1,b):
#   for j in range(b-1):
#      if a[j] > a[i]:
#       t=a[j]
#       a[j]=a[i]
#       a[i]=t
# print(a)
# 1000因数之和等于他本身
# for i in range(2,1001):
#     sum=0
#     for j in range(1,1000):
#         if j< i and i%j== 0:
#            sum=sum+j
#     if i==sum:
#       print(i)
# for a in range (2,1001):
#     s = 0
#     for b in range (1,1000):
#         if b<a and a%b==0:
#             s=s+b
#     if a==s:
#          print(a)


# f=open('123.jpg','rb')
# b=f.read()
# s=open('123.jpg','wb')
# s.write(b)
# f.close()


# with open('a.txt','r+',encoding='utf-8') as f:
#     f.write('qwe')
#     b=f.read()
#     print(b)
# def a():
#     b=0
#     for i in range(101):
#         b=b+i
#     print(b)
# a()
# 一组数最大放在第一
# a =input("一组数")
# a=a.split(',')
# a=(a)
# for b in range(0,len(a)-1):
#      x=max(a)
#      a[0]=x
# print(a)

# 一个数组第一大的数，第二大的数
# a=input ("一组数")
# a=a.split(',')
# a = [int(i) for i in a]
# b=a.startswitch('abc')
# # b=len(a)
# for i in range(1,b):
#   for j in range(b-1):
#      if a[j] < a[i]:
#       t=a[j]
#       a[j]=a[i]
#       a[i]=t
# print(a[:2])


# f = open('a.txt', 'r', encoding='utf=8')
# b = f.readlines()
# x=len(b)
# for i in range(x):
#    c=b[i].startswith('abc')
#    d=b[i].endswith('123\n')
#    if c==True and d==True:
#      print(b[i])


# a=[12,12,23,23,34]
# b=[]
# for b in a:
#     while a.count(b)>1:
#         a.remove(b)
#     print(a)

# i = 1
# sum = 0
# while (i < 101):
#     sum = sum + i
#     i = i + 1
# print(sum)


# b=1
# def a():
#     global b
#     b=0
#     print(b)
# a()
# print(b)

#
# def asd(x):
#     a=sum(range(x+1))
#     print('hello')
#     print(a)
# asd(100)
# for i in range:

# def a(b=100):
# #     c=0
# #     for i in range(b+1):
# #         c+=i
# #     print(c)
# # a(10)

# def asd( x=2,y=100):
#     a=0
#     for i in range(x,y+1):
#         for j in range(2,y+1):
#             if i%j==0:
#              break
#         if i==j:
#          a=a+i
#     print(a)
# asd(2,100)


# def asd(**kwargs):
#     print(kwargs)
# asd(name=12,age=23,sd='qwer')

# def asd():
#     for i in range(10):
#      print(i)
#     return
# asd()

# 1-10,1-20,1-30,1-40的和都加2
# def asd(y):
#     a = 0
#     for i in range(1,y+1):
#        a+=i
#     return a
# for i  in range(10,41,10):
#  c=asd(i)+2
#  print(c)


# 加减乘除
# def asd (x,y,z):
#   if z =='+':
#       a=x+y
#   if z  =='-':
#       a=x-y
#   if z =='*':
#       a=x*y
#   if z=='/':
#       a=x/y
#   return a
# c=asd(3,20,'-')
# print(c)


# def asd(x,y):
#         b=x-y
#         return b
# c=asd(15,10)
# print(c)

# def asd(x,y):
#     b=x*y
#     return b
# c=asd(3,3)
# print(c)

# def asd(x,y):
#     b=x/y
#     return b
# c=asd(22,2)
# print(c)


# a =lambda x,y : x + y
# b =lambda x,y : x - y
# c =lambda x,y : x * y
# d =lambda x,y : x / y
# while True:
#    s = input('数字')
#    if '-' in s:
#         z = s .split('-')
#         print(b(int(z[0]),int(z[1])))
#    elif '+' in s:
#         z = s.split('+')
#         print(a(int(z[0]), int(z[1])))
#    elif '*' in s:
#          z = s.split('*')
#          print(c(int(z[0]), int(z[1])))
#    elif '/' in s:
#         z = s.split('/')
#         print(d(int(z[0]), int(z[1])))
#    else:
#        break

# def a (x,y,z):
#     x=list(x)
#      d=y+z
#     if d >len(x):
#         d =len(x)
#      for i in range(y,d):
#         x.pop(y)
#     x=''.join(x)
#      print(x)
# a('asdfgasdf',2,20)

# def a (x,y,z):
#      x=list(x)
#      d=y+z
#      if  d >len(x):
#          d=len(x)
#      for i in range(y,d):
#         x.pop(y)
#      x ="".join(x)
#      print(x)
# a('qwertsdfysdf',2,3)
# 左移动
# a= [1,2,3,4,5]
# b=a.pop(0)
# a.append(b)
# print(a)
# 右移动
# a= [1,2,3,4,5]
# b=a.pop(len(a)-1)
# a.insert(0,b)
# print(a)


# 不用int将字符串变成整数
# a='123'
# b=len(a)
# c=0
# for i in range(b):
#     for j in range(10):
#         if  str(j)==a[i]:
#             c+=j*10**(b-i-1)
# print(c)
# print(type(c))


# a=input("一组数")
# a=a.split(',')
# a=[int(s) for s in a]
# b=len(a)
# for i in range(b):
#     for j in  range (b):
#          for x in range(b):
#              if a[i]!=a[j] and a[j]!=a[x] and a[i]!=a[x]:
#                c=a[i]*100+a[j]*10+a[x]
#                print(c)



# a=input('数字')
# a=a.split(',')
# a=[int(s) for s in a]
# b=max(a)
# a.remove(b)
# a.append(b)
# d=min(a)
# a.remove(d)
# a.insert(0,d)
# a=list(a)
# print(a)

# a=input("数字")
# a=int(a)
# b=[2,34,9,13]
# b.append(a)
# for i in range(1,len(b)):
#     for j in range(len(b)-1):
#         if b[j+1] < b[j]:
#             t=b[j]
#             b[j]=b[j+1]
#             b[j+1]=t
# print(b)


# a=100
# for i in range(100):
#     for j in range(50):
#         k=100-i-j
#         if i*1+j*2+k*0.5==100:
#             print(i,j,k)

# a=int(input("数字"))
# ff=[str(i) for i in range(10)]+['a','b','c','d','e','f']
# c=""
# while True:
#     b=a%16
#     c=c+ff[b]
#     a=a//16
#     if a==0:
#         break
# print(c[::-1])

# a=int(input("总资产"))
# b=[('电脑',1999),("鼠标",10),("游艇",20),("美女",998)]
# c=[]
# for i ,j in enumerate(b):
#     print(i+1,j)
# while True:
#  d=int(input("商品号"))
#  if d < len(b)+1 and d >=0:
#      if d ==1:
#        c.append(b[0])
#      if d ==2:
#        c.append(b[1])
#      if d==3:
#        c.append(b[2])
#      if d==4:
#        c.append(b[3])
#  print(c)
#  if






# def  wc(x,y,z):
#     x=list(x)
#     d=y+z
#     if  d > len(x):
#         d=len(x)
#     for  i in range(y,d):
#         x.pop(y)
#     b=''.join(x)
#     print(b)
# wc('hdjfehhjdcf',2,12)


# 购物车
# a = int(input("总资产"))
# b = [('摇篮', 1999), ("投影仪", 10), ("沙发", 20), ("茶具", 998)]
# c = []
# z = []
# for i, j in enumerate(b):
#     print(i + 1, j)
# while True:
#     d = int(input("商品号"))
#     if d == 1:
#         c.append(b[0])
#     elif d == 2:
#       c.append(b[1])
#     elif d == 3:
#          c.append(b[2])
#     elif d == 4:
#          c.append(b[3])
#     elif d==5:
#         break
#     print(c)
# # while True:
# #         # p=int(input("删除商品序号"))
# #         # c.pop(c[p])
# #         # print(c)
# #         # if p ==9:
# #         #  exit()
# for q in range(0,len(c)):
#     z.append(c[q][1])
# print(z)
# w=[int(k) for k in z]
# print(sum(w))
# if sum(w) > a:
#     print("金额不够")
#     chongzhi = int(input('输入充值金额'))
#     a = a + chongzhi
# if a >sum(w):
#     print('购买成功')


# def a (x,y):
#      # x=[int(e) for e in x]
#      for i in range(len(x)):
#         for j in range(len(x)):
#              if i !=j and y==x[i]+x[j]:
#               print(x[i],x[j])
# a((2,3,4,5),8)


# def asd(x,y):
#         b=x-y
#         return b
# c=asd(15,10)
# print(c)
# a=int(input("数字"))
# ff=[str(i) for i in range(10)]+['a','b','c','d','e','f']
# c=""
# while True:
#     b=a%16
#     c=c+ff[b]
#     a=a//16
#     if a==0:
#         break
# print(c[::-1])



# def asd(b):
#     a=0
#     for i in range(1,b+1):
#         a=a+i
#         return a
# c=asd(10)+2
# print(c)

# with open('a.txt','r',encoding='utf-8')as f:
#     a=f.readlines()
#     for i in range(len(a)-1):
#         b=a[i].startswith('#')
#         if b==True:
#             a.remove(a[i])
#     for j in range(len(a)-1):
#         if  a[j]=='\n':
#          a.remove(a[j])
#     print(a)



# def zz():
#     print("hello")
# if __name__=='__main__':
#     for i in range(10):
#         print(i)

#
# try:
#     a=123+'qwe'
#     print(a)
# except:              #默认能够预防所有类型的错误
#     print(123)
# else:
#     print(789)
# finally:
#     print('567')



# #九九乘法表写入表格中
# import xlwt
# f=xlwt.Workbook()      #创建一个空的excel文件
# sheet=f.add_sheet('python_test')#创建一个标签页，括号中是标签页的名称
# for i in range(1,10):
#      for j in range(1,i+1):
#          sheet.write(i-1,j-1,'{}*{}={}'.format(j,i,i*j))#写入数据时，需要固定单元格，x,y
# f.save('yy.xls')

# import xlrd
# f=xlrd.open_workbook('yy.xls')
# b=f.nsheets
# print(b)
# sheet=f.sheets()[0]

# import xlrd
# f=xlrd.open_workbook('yy.xls')
# # b=f.sheet_names()
# # print(b)  #获取所有标签页的名称
# sheet=f.sheet_by_name('python_test')
# b=sheet.nrows
# for i in range(b):        #获取所有行的内容
#     c=sheet.row_values(i)
#     print(c)


# import xlrd
# f=xlrd.open_workbook('yy.xls')

# # b=f.sheet_names()
# # print(b)  #获取所有标签页的名称
# sheet=f.sheet_by_name('python_test')
# # b=sheet.ncols  #获取所有列
# for i in range(0,5):        #获取所有行的内容
#   c=sheet.row_values(i)
# # b=sheet.cell(0,0).value
#   print(c)
#

# 把a.txt文件内容插入表中
# import xlwt
# ff=xlwt.Workbook()
# sheet=ff.add_sheet('python_test')
# c=[]
# f=open('a.txt','r',encoding='utf=8')
# a=f.readlines()
# print(a)
# for x in range(4):
#   q=a[x]
#   w=q.split(',')
#   c.append(w)
#   print(c)
# f.close()
# #print(len(c))
# for i in range(len(c)):
#       for j in range(len(c)):
#          sheet.write(i,j,c[i][j])
# ff.save('qq.xls')



#给excel表格中追加内容
# from xlutils.copy import copy
# import  xlrd
# f=xlrd.open_workbook('qq.xls')#打开追加的文件
# new_f=copy(f)  #复制文件
# sheet = new_f.get_sheet(0)  #获取要追加的标签页，通过索引
# sheet.write(0,0,'qwe')  #写入
# new_f.save('qq.xls')
#





#错误的qwertyusdfghjdfghjdxfghjbnm,.,mnbnm,.,mnm,nbvbnmnvbnmcvbvc
#from xlutils.copy import copy
# import  xlrd
# f=xlrd.open_workbook('qq.xls')#打开追加的文件
# sheet1=f.sheets()[]
# b=sheet1.nrows
# new_f=copy(f)  #复制文件
# sheet = new_f.get_sheet(0) #获取要追加的标签页，通过索引
# f=open('a.txt','r',encoding='utf=8')
# x=f.readlines()
# c=[]
# for i in range(len(x)):
#     q=x[i]
#     w=q.split(",")
#     c.append(w)
# sheet1=f.sheets()[]
# b=sheet1.nrows
# new_f=copy(f)
# sheet.write(0,0,'qwe')
# new_f.save('qq.xls')




# a=time.tim e()
# b=time.localtime(10000000000)
# print(b)
# a=time.strftime('%Y-%m-%d',b)
# print(a)
# import time
# a=time.strptime('2011-12-22 10:20:03','%Y-%m-%d %H:%M:%S')
# print(a)
# # time.sleep(30)
# # b=(2014,11,11,11,11,11,23,12,12)
# # a=time.mktime(b)
# print(a)

#判断一个日期是不是闰年，星期几，一年中的第几天
# import time
# a=input("日期")
# x=time.strptime(a,'%Y-%m-%d')
# print(x)
# c=x[0]
# if c%4==0:
#  print('是闰年')
# else:
#  print('不是闰年')
# d=x[6]+1
# print('星期{}'.format(d))
# c=x[7]
# print('今年第{}天'.format(c))

# import time
# a=input("日期")
# x=time.strptime(a,'%Y-%m-%d')
# y=time.mktime(x)
# z=int(y)
# q=z-86400
# w=time.localtime(q)
# print('前一天{}年{}月{}号'.format(w[0],w[1],w[2]))
# d=x[0]
# c=x[1]
# e=x[2]
# if e==1:
#     c=c-1
# yesterday= today + timedelta(days = -1)
# print(x[0], c, x[2] - 1)
#
#
# # 把表格中的内容插入a.txt文档中
# import xlrd
# f=xlrd.open_workbook('yy.xls')
# sheet=f.sheet_by_name('python_test')
# b=sheet.nrows
# ff = open('a.txt', 'w', encoding='utf=8')
# for i in range(b):
#  c = sheet.row_values(i)
#  d=str(c)
#  d = " ".join(c)
#  ff.write(d)
#  ff.write('\n')
# ff.close()



# import time
# sentence = "qqyy"
# for char in sentence.split():
#    allChar = []
#    for y in range(12, -12, -1):
#        lst = []
#        lst_con = ''
#        for x in range(-30, 30):
#             formula = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
#             if formula <= 0:
#                 lst_con += char[(x) % len(char)]
#             else:
#                 lst_con += ' '
#        lst.append(lst_con)
#        allChar += lst
#    print('\n'.join(allChar))
#    time.sleep(1)

# import xlrd
# from xlutils.copy import copy
# f=xlrd.open_workbook('qqq.xls')
# sh=f.sheets()[0]
# num=sh.nrows
# nun=sh.ncols
# new_f=copy(f)
# sheet=new_f.get_sheet(0)
# for i in range(10):
#     sheet.write(num,nun,'qwe')
# new_f.save('aaaa.xls')


# import pymysql
# conn=pymysql.connect(host='192.168.0.176',port=3306,user='root',passwd='123456')
#
# m=conn.cursor()
# # m.execute('create database python_learn;')
# m.execute('use python_learn;')
# m.execute('show databases;')
# print(m.fetchall())
# m.execute('create table biao(name char(20),age int);')
# m.execute('create table qq(name char(20),age int,sex char(20));')
# for i in range(10):
#    m.execute('insert into qq values("小红",{},"nan")'.format(i))
# m.execute('select * from qq')
# m.execute('show tables')
# c=m.fetchall()  #读取上一个sql语句的结果
# print(c)
# b=m.fetchmany(1)  #传入的参数的数字是几，就读取几条数据
# print(b)

# b=m.fetchone()  #每次只读取一条
# # c=m.fetchone()   # 读取的时候按照第一次读的顺序
# print(b)



#把表格中的内容如数据库
# import pymysql
# conn=pymysql.connect(host='192.168.0.176',port=3306,user='root',passwd='123456')
# m=conn.cursor()
# import xlrd
# f=xlrd.open_workbook('qq.xls')
# m.execute('use python_learn')
# sheet=f.sheets()[0]
# for i in range(sheet.nrows):
#     b=sheet.row_values(i)
#     if i==0:
#       m.execute('create table  dd({} char(255),{} char(255),{} char(255),{} char(255))'.format(b[0],b[1],b[2],b[3]))
#     else:
#         m.execute('insert into dd values("{}","{}","{}","{}")'.format(b[0],b[1],b[2],b[3]))
# m.execute('select * from dd;')
# c=m.fetchall()
# print(c)



# 把a.txt文件中的内容导入数据库
# import pymysql
# conn=pymysql.connect(host='192.168.0.99',port=3306,user='root',passwd='123456')
# m=conn.cursor()
# f=open('a.txt','r',encoding='utf-8')
# b=f.readlines()
# m.execute('use python_learn')
# for i in range(len(b)):
#      c=b[i].split(',')
#      if i==0:
#         m.execute('create table  ww({} char(255),{} char(255),{} char(255),{} char(255));'.format(c[0],c[1],c[2],c[3]))
#      else:
#        m.execute('insert into ww values("{}","{}","{}","{}");'.format(c[0],c[1],c[2],c[3]))
# m.execute('select * from ww;')
# c=m.fetchall()
# print(c)
#
# b=input("  ")
# c=b.split(',')
# for i in  c:
#     d=int(i)
# print(type(d))
# # print()
#


#把数据哭的内容写入a.txt
# import pymysql
# conn=pymysql.connect (host='192.168.0.47',port=3306,user='root',passwd='123456')
# m=conn.cursor()
# m.execute('use zlq;')
# m.execute('desc zhuzhu;')
# c=m.fetchall()
# print(c)
# q=[]
# for j in range(len(c)):
#      q.append(c[j][0])
#      p=' '.join(q)
# f = open('a.txt', 'w', encoding='utf-8')
# f.write('{}'.format(p))
# f.write('\n')
# m.execute('select * from ww;')
# c=m.fetchall()
# print(c)
# for z in range(len(c)):
#      f.write('{}'.format(c[z]))
#      f.write('\n')

#把数据哭的内容写入exce表格中
# import pymysql
# conn=pymysql.connect (host='192.168.0.176',port=3306,user='root',passwd='123456')
# m=conn.cursor()
# m.execute('use python_learn;')
# m.execute('desc ww;')
# c=m.fetchall()
# # print(len(c))
# m.execute('select * from ww')
# d=m.fetchall()
# print(d)
# ff=len(d)
# import xlwt
# f=xlwt.Workbook()
# sheet = f.add_sheet('qq')
# for i in range(len(c)):
#     sheet.write(0,i,c[i][0])
# for j in  range(1,ff+1):
#     for k in range(len(c)):
#         sheet.write(j,k,d[j-1][k])
# f.save('x.xls')
#








# def asd(x):
#     a=0
#     for i in range(101):
#         a+=i
#     return a
# c=asd(123)
# print(c)

#浅复制
# a=[212,23,[23,234,34],3]
# b=a.copy()
# print(b)
# a.append(100)
# print(b)  #不显示添加的
# a[2].append()
# print(b)   #显示添加的

# import copy
# b=copy.deepcopy(a) #深复制(先写 import copy 模块)
# print(b)


# import os
# print(os.getcwd())
# os.chdir(r'C:\zlq')
# print(os.getcwd())

# b=os.popen('route print')
# print(b.read())
# print(os.listdir(r'C:'))  #查看所有文件

# os.mkdir('aaa')  #创建目录
#os.rmdir('aaa') #删除空目录
# os.makedirs(r'aaa\bbb\ccc')  #创建递归目录
#os.removedirs(r'aaa\bbb\ccc')   #删除递归目录
# b=os.path.split(r'C:\Users\Public\Desktop\网易有道词典')
# print(b)     #把文件路径与文件分隔开
# b=os.path.splitext(r'‪C:\Users\Public\Desktop\网易有道词典.lnk')
# print(b)   #把后缀名与路径分隔开
# os.rename(r'x.xls',r'll.xls')  #重命名
# b=os.path.isfile(r'‪C:\Users\Public\Desktop\网易有道词典')
# print(b)     #判断是否为普通文件

#将本目录下的所有.py的文件打印出来

# b=os.listdir()
# for i in b:
#     c=str(i)
#     d=c.endswith('.py')
#     if d==True:
#         print(i)


# import paramiko
# #创建一个ssh客户端
# with paramiko.SSHClient() as ssh111:
# #跳过know-hosts文件中验证
#      ssh111.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# #连接主机
#      ssh111.connect(hostname='192.168.0.176',
#                port=22,
#                username='root',
#                password='123456')
# # #执行命令
#      while True:
#          x=input('>>>')
#          if  x=='exit':
#             break
#          else:
#             a,b,c=ssh111.exec_command(x)
#             print(b.read().decode())
#第一个变量：标准输入的命令(不能简写，必须是有结果的命令
#第二个变量：是命令的输出
#第三个变量是命令的报错

# # 断开连接
# ssh111.close()
# #上传和下载文件
# import paramiko
# #创建一个传输通道
# qq = paramiko.Transport(('192.168.0.176',22))
# #连接主机
# qq.connect(username='root',password='123456')
# #使用ssh协议创建一个传输功能
# sftp = paramiko.SFTPClient.from_transport(qq)
# #下载文件，从Linux上下载到window
# # sftp.get(r'/home/b.out','ss.sh')
# #上传文件，从window上传到Linux上
# sftp.put('zhu.py','/home/day3.py')
# #断开连接`--
# # qq.close()



# #发送邮件smtp， pop3  imap
# import smtplib     #封装smtp协议
# import email.mime.multipart as mul   #制作邮件
# import email.mime.text as textt   #  对邮件的正文进行处理
# message = mul.MIMEMultipart()  #建立一个空邮件
# message['Subject']='python_test'  #标题
# message['From']='zhaolq1998@163.com'#发件人
# ww=['973472897@qq.com','825069672@qq.com']
# # message['To']='17637839607@163.com'   #收件人
# message['To']='.'.join(ww)
# txt="""  #正文  多行数据
#  猩猩and狒狒！
#  """
# # 对正文进行处理
# tet=textt.MIMEText(txt)
# # # #将处理过后的正文添加到邮件里
# message.attach(tet)
# att1 = textt.MIMEText(open('ll.py', 'rb').read(), 'base64', 'utf-8')
# att1["Content-Type"] = 'application/octet-stream'  #附件的字段 固定
# att1["Content-Disposition"] = 'attachment; filename="xingxing.py"'  #filename可以改附件名，对方显示的是这个名字
# message.attach(att1)
# # # #定义邮件服务器 https=http+ssh
# smtp123=smtplib.SMTP_SSL('smtp.163.com',465)
# # # #登录服务器 用户名，密码(不死登录密码，是授权码)
# smtp123.login('zhaolq1998@163.com','wzz0106')
# smtp123.sendmail('zhaolq1998@163.com',ww,message.as_string())
# smtp123.close()



# socket  套接字，提供了通信双方最底层的功能(发送，接受)
# c/s结构 通过socket 实现基本的通信
#server端
# import socket  #创建一个套接字(具有发送和接受能力)
# SOCK_STREAM # 指的是tcp
# AF_INET  #指的是ipv4
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #括号里面值得是tcp
# s.bind(('192.168.0.131',3000))  #绑定ip和端口号
# s.listen(3)
# while True:
#     client,addr=s.accept()     #接受客户端建立的连接  接受的是建立连接
#     #接受客户端发送的数据
#     reg=client.recv(1024)   #第一个变量的结果:立连接的信息  第二个变量的结果:客户端的ip和端口号
#     print(reg.client.recv(1024))                       #1024是每次接受的最大数据（字节）
#     print(reg.decode('utf-8'))
#     msg='welcome'
#     #给客户端发送响应
#     client.send(msg.encode('utf-8'))

#
# f=open('a.txt','r',encoding='utf=8')
# a=f.readlines()
# # print(a)
# for i in a:
#    b=i.split(',')
#    print(b)





# import xlwt
# ff=xlwt.Workbook()
# sheet=ff.add_sheet('123')
# for j in range(len(a)):
#    for k in range(j+1):
#       sheet.write(j,k,b[j])
# ff.save('ww.xls')


# import time
# # a=time.time()
# # print(a)
# # b=time.localtime(100)
# b=time.strptime('2019-4-23','%Y-%m-%d')
# print(b)



#服务器
# import socket    #创建一个套接字
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  #SOCK_DGRAM为udp  AF_INET为ipv4
# s.bind(('192.168.0.22',3000))    #绑定IP地址     类型元组
# while True:
# #接受客户端的请求  第一个变量是客户端的请求数据  第二个变量是客户端的ip和端口号
#     client,addr=s.recvfrom(1024)
#     print(client.decode('utf-8'))
#     msg='welcome'
#     s.sendto(msg.encode('utf-8'),addr)



#正则表达式
# with open ('a.txt','r') as f:
#     a=f.read()
# 贪婪模式：尽可能多的去匹配符合条件的内容
# 非贪婪模式：尽可能少的去匹配符合条件的内容  (?)
# import re    #将字符串转换成正则表达式
# # a='wqr123qwNer23445sew789dfqwe'  #匹配a中的数字
# # b=re.compile('W(.*)W',re.I)   #  re.S :给拥有匹配换行符在内的功能
# # #将正则表达式编译成python能够识别的正则语言
# # #拿着编译后的正则到字符串中找   找所有符合条件的字符，结果是一个列表
# # c=b.findall(a)
# # print(c)
# #
# #
# # c=re.findall('123(.*)789',a)  #findall本身具有编译的能力
# # print(c)
# #
#
#
# # a=['qwertyt123q2324wertysdf234sdfg34']
# # for i in a:
# #     print(i)
#     # # 括号里面的第一个为正则过滤出被替换的字符
#     # # 第二个是替换成的字符
#     # #第三个是要被替换的字符范围
#     # c=re.sub('[0-9]+','abc',i)
#     # print(c)
#
# #python 的函数
# # print(hex(123))     #10进制转16进制
# # print(oct(123))     #10进制转8进制
# # print(bin(123))     #10进制转2进制
# # print(int(0b11))    #任何进制转10进制
#
# #chr将数字转换成asill表中对应的字符b
# # a=[chr(i) for i in range(97,103)]
# # print(a)
# #ord将asill表中的字符转换成对应的数字
# # print(ord('a'))
# #
# # a,b=divmod(100,6)   #整除求余
# # print(a,b)   #a为整除的结果  b为余数
# #shell属于面向过程 通过代码和逻辑一步一步实现要达到的目的 优点：性能好  缺点：不易维护
# #面向对象  优点：可扩展 ，易维护，可以重复使用
# #1：将函数进行分类和封装，使开发更高效
# #定义一个类  class+类名：默认首字母大写
# #2：属性，方法(函数)  属性：一个类中的所有的函数都具有的特点
# #self  不是函数的参数，self是类的实例 是方便在类的内部调用其他函数
# # class  ASD():
# #     def zhishu(self,x):
# #         a=0
# #         for i in  range(x+1):
# #             a=a+i
# #         print(a)
# #         # self.qwe()     #可以接着执行下一个函数
# #     def  yy(self):
# #         print('hello')
# # #将类名()赋值给了一个对象
# # #asd叫类的实例(对象) 是方便在类的外部调用其他函数
# # # asd=ASD()
# # # asd.zhishu(10)
# # #3：继承
# # class zzz():   #括号中是写要继承的类 新的类会继承旧的类中的所有函数
# #     def yy(self):  #继承多个类的时候用逗号隔开
# #                   #如果继承多个类的时候，类中有重复的函数名只调用最左面的函数
# #       print(123)
# #                                     # q=zzz()
# #                                     # q.qwe()
# #
# # class lll(ASD,zzz):   #class lll(zzz,ASD)
# #     pass
# # z=lll()
# # z.yy()
#
#
#
#
# #4：多态（方法重写）继承的类中不满足需求，
# #在本类中自定义一个跟继承的类中函数名相同的函数
# # from zhu import ASD
# # class  abc(ASD):
# #     def zhishu(self,x):
# #         a=0
# #         for i in  range(x+1):
# #             a=a+i
# #         print(a)
# #     def  yy(self):       可以写自己的目的和要求
# #         print('hello')
# #         print(123456)
# # q=abc()
# # q.yy()
#
# #5：私有方法（函数）
# #不可被继承的，不能在类的外部调用
# #只能在内部调用  在函数名左边加两个下划线
#
# # class  abc():
# #     def __zhishu(self,x):   #__私有方法
# #         a=0
# #         for i in  range(x+1):
# #             a=a+i
# #         print(a)
# #                         #  可以在内部用self调用
# #     def  yy(self):
# #         print('hello')
# # qq=abc()
#
# #6:类的专有方法
#     # 函数名左右两边都有两个下划线
#     #专有方法是python内部固定的
#     #只要是个类，具有所有的专有方法
# # from zhu import ASD
# # class  abc():
# #     def __init__(self,name,xueliang):   #    定义属性 初始化属性
# #         self.name=name
# #         self.xueliang=xueliang
# #     def  daguai(self,x):
# #         self.xueliang-=200
# #         print('{},还剩下{}{}'.format(self.name,self.xueliang,x))
# #     def  jiaxue(self):
# #         self.xueliang+=500
# #         print('{},还剩下{}'.format(self.name, self.xueliang))
# #         return 100
# # q=abc('安其拉',1000)
# # w=abc('李白',1000)
# # q.jiaxue()
#
#
# # import smtplib
# # import email.mime.multipart as mul
# # import email.mime.text as textt
# # message=mul.MIMEMultipart()
# # message['project']='python_test'
# # message['From']='zhaolq1998@163.com'
# # message['To']='973472897@qq.com'
# # txt="""
# #   中国
# #   河南
# #   """
# # tet=textt.MIMEText(txt)
# # message.attach(tet)
# # smtp123=smtplib.SMTP_SSL('smtp.163.com','465')
# # smtp123.login('zhaolq1998@163.com','wzz0106')
# # smtp123.sendmail('zhaolq1998@163.com','973472897@qq.com',message.as_string())
# # smtp123.close()
# #
# # import socket
# # sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #创建一个套接字
# # sock.connect(('192.168.0.84',3000))       #连接服务器
# # qq='hello'    #将qq当做请求发送给服务器
# # sock.send(qq.encode('utf-8'))
# # qq=sock.recv(1024) #接受响应
# # print(qq.decode('utf-8'))
#
#
#
#
#

#
#
#
#
#
# #http协议
#
# # import os
# # # print(os.getcwd())
# # print(os.listdir())
#
#
# # 爬虫：模仿浏览器，根据自己制定的规则，批量去下载指定的资源
# # 分类：聚焦爬虫，搜索爬虫
# # 聚焦爬虫：指针对某个网站进行爬取
# # 搜素爬虫：针对全网络进行爬取（搜索引擎）
# # 模仿浏览器：requests  urllib   urllib3   scrapy
# # 过滤网页资源：正则表达式   re， BeautifulSoup,xpath
#
#
# # 爬虫第一步：分析网址
# #爬虫第二步：找到想要的资源过滤
# ##爬虫第三步：保存
# #对服务器请求，将得到he的相应数据过滤并保存
# #服务器有压力
# #开发人员：反爬：防止爬虫程序，批量下载资源
# #常见的反爬机制：
#              # 1：通过请求headers判断
#              #2：ip地址被封  频繁的转换公网ip（西刺代理）
#              #3：验证码
#              #4：数据混淆
#              #5：行为分析
#  # 网页：静态网页：所有的资源都在html文件上
#  #      动态网页：资源不在html文件上  ajax(xhr)  javaScript(js)
#  #json:是一种轻量级的数据传输格式
#  # import json
#  # import  requests
#  # url=''
#  # res=requests.get(url)
#  # hhh=res.content.decode('utf-8')
#  # qqq=json.loads(hhh)  #将字符串转换为字典
#  # print(qqq['data'])
#  # uuu=json.dumps(qqq)   #将字典转换为字符串
#  #
#  #
#
#
#
#
# import requests
# import re
# class  FreeBuf():
#    def send_请求(self):
#      url='https://www.freebuf.com/page/{}.format(z)'
#      head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'}
#      res=requests.get(url,headers=head)                                    #发送请求
#      hh=res.content.decode('utf-8')      #读取结果1：text  以文本的方式接收 字符串
#      return hh

#    def guolv(self,x): #2:content  以字节方式接受
#        title=[]
#        patt=re.compile('<div class="news-info">(.*?)<dd>',re.S)
#        itesms=patt.findall(x)
#        for i in itesms:
#            aa=re.findall('title="(.*?)"',i)  #二次过滤
#            title.append(aa[0])
#        return title
#            # print(aa)
#
#    def  save(self,y):
#         with  open('a.txt','a',encoding='utf-8')as f:
#             for i in y:
#                 f.write(i+'\n')
# # #
# # #
# #
# # fr3=FreeBuf()
# # for i in range(1,5):
# #     hh=fr.send_请求(i)
# #     fr.guolv(hh)
# #     yy=(fr.guolv(hh))
# #     fr.save(yy)
#
#
#
# #保存图片





# import requests
# import re
# url = 'http://www.doutula.com/article/list/?page=2'
# head = {'User-Agent': 'Mozilla/5.0 (WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/70.0.3538.110Safari/537.36'
#         }
# res = requests.get(url,headers=head)
# html = res.content.decode('utf-8')
# patt = re.compile(r'<img src="//pic.qiushibaike.com/system/pictures/(.*?).jpg"')
# items = patt.findall(html)
# a=0
# # print(len(items))     打印出图片的个数
# for i in items:
#     j ='http://pic.qiushibaike.com/system/pictures/'+i+'.jpg'
#     msg=requests.get(j,headers=head)
#     hh=msg.content
#     with open('{}.jpg'.format(a),'wb')as f:
#         f.write(hh)
#         a+=1






# import requests
# import re
# aa='https://movie.douban.com/top250'
# head = {
#            'User-Agent': 'Mozilla/5.0 (WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/70.0.3538.110Safari/537.36'}
# b = requests.get(aa, headers=head)
# html =b.content.decode('utf-8')
# a = []
# pstt=re.compile('<img width="100" alt="(.*?)"')
# iteam=pstt.findall(html)
# a.extend(iteam)
# pst=re.compile(r'src="https://img(.).doubanio.com/view/photo/s_ratio_poster/public/(.*?).jpg" class="">')
# itea=pst.findall(html)
# print(itea)
# b=0
# for i in itea:
#     j = 'https://img{}.doubanio.com/view/photo/s_ratio_poster/public/{}.jpg'.format(i[0],i[1])
#     print(j)
# #     msg = requests.get(j,headers=head)
# #     hh = msg.content
# #     with open('{}.jpg'.format(a[b]), 'wb') as f:
# #         f.write(hh)
# #     b += 1



# import requests
# import re
# url='http://movie.douban.com/top250'
# head={'User-Agent':'Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
# res = requests.post(url,headers=head)
# html = res.content.decode('utf-8')
# a=[]
# bb = re.compile(' <img width="100" alt="(.*?)"')
# aa = bb.findall(html)
# a.extend(aa)
# cc = re.compile('src="https://img(.).doubanio.com/view/photo/s_ratio_poster/public/(.*?).jpg" class="">')
# dd = cc.findall(html)
# b=[]
# b.extend(dd)
# for i in dd:
#      j='https://img{}.doubanio.com/view/photo/s_ratio_poster/public/{}.jpg'.format(i[0],i[1])
#      msg = requests.get(j,headers=head)
#      hh = msg.content
#      with open('{}.jpg'.format(a[b]),'wb') as f:
#          f.write(hh)






# import os
# a = os.getcwd()
# aa = os.listdir(a)
# for i in aa:
#     c = str(i)
#     d = c.endswith('.jpg')
#     if d == True:
#         os.remove(i)
# def f(x):
#     y=x+1
#     return y
# f(1)




# import unittest
#写单元测试用的  写断言用的
#按预期结果与实际结果做对比的过程
# class demo(unittest.TestCase):
#     def test_1(self):
#         #假设预期结果是1
#         #实际结果是2
#         #判断预期结果是否等于实际结果
#         a=1#预期结果
#         #断言：
#         #实际结果与预期结果相等
#         self.assertEquals(a,2)
# if __name__=='__main__':
#     unittest.main()