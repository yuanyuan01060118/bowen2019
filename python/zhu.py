#！/usr/bin/python
# -*- coding:utf-8  -*-7
# while语句100以内的和
# i = 1
# sum = 0
# while i < 101:
#     sum = sum + i
#     i = i + 1
# print(sum)



#1：乘法表：
# for i in  range(1,10):
#     for j in range(1,10):
#         if j<=i:
#             print('{}*{}={}'.format(j,i,j*i),end='\t')
#         if j==i:
#     print()



#2：质数之和（任意范围的）
# s=0
# for a in range(2,101,1):
#
#         c=a%b
#         if c==0:
#             break
#     if a==b:
#      s=s+a
# print(s)



#3.	阶乘之和（任意数的）
#a=0
# b=1
# for s in range(1,4):
#     b=b*s
#     a=a+b
#     print(a)




# 4：三角形的判断
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




#5:判断以什么开头，以什么结束
# f = open('a.txt', 'r', encoding='utf=8')
# b = f.readlines()
# x=len(b)
# for i in range(x):
#    c=b[i].startswith('abc')
#    d=b[i].endswith('123\n')
#    if c==True and d==True:
#      print(b[i])




#6：： 删除重复：
# a=input('一组数')
# a = a.split(',')
# a=[int(s) for s in a ]
# for i in a:
#     while a.count(i)>1:
#         a.remove(i)
#         print(a)



# 7：回文字符串
# a=input('字符串')
# a=str(a)
# if a==a[::-1]:
#     print('回文字符串')
# else:
#     print('不回文字符串')




# 8：排序（选择、冒泡）
# a=input ("一组数")
# a=a.split(',')
# a = [int(i) for i in a]
# b=len(a)
# for i in range(1,b):
#   for j in range(b-1):
#      if a[j+1] < a[j]:
#       t=a[j]
#       a[j]=a[j+1]
#       a[j+1]=t
# print(a)




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



#9.	三次猜数字
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




# 10：：1000以内的水仙花数
# for a in range(100,1000,1):
#     b=a//100
#     c=a//10%10
#     d=a%10
#     if a==b**3+c**3+d**3:
#       print(a)




# 11:一个数组第一大的数，第二大的数
# a=input('请输入')
# b = a.split(',')
# b = [int(i) for i in b]
# b.sort()
# o = []
# f=b.count(b[-1])
# for k in range(1,f+1):
#     o.append(b[-1])
#     b.remove(b[-1])
# d=b.count(b[-1])
# for j in range(1,d+1):
#     o.append(b[-1])
# print(o)





# 12.	不用int将字符串变成整数
# a='234'
# b=len(a)
# c=0
# for i in range(b):
#     for j in range(10):
#         if  str(j)==a[i]:
#             c+=j*10**(b-i-1)
# print(c)
# print(type(c))





# 13.任意4个数字，组成不相同的三位数
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





# 14：# 左移动
# a= [1,2,3,4,5]
# b=a.pop(0)
# a.append(b)
# print(a)
# 右移动
# a= [1,2,3,4,5]
# b=a.pop(len(a)-1)
# a.insert(0,b)
# print(a)




# 15.	十进制转换成十六进制
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




#16：：：1000以内因数之和等于他本身
# for a in range (2,1001):
#     s = 0
#     for b in range (1,1000):
#         if b<a and a%b==0:
#             s=s+b
#     if a==s:
#          print(a)





#17.	将列表中最大的放在最后一位，最小的放在第一位
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



#18.	一个有顺序的列表，随机加入一个数，加入的数在正确的位置
# a=input("数字")
# a=int(a)
# b=[2,34,9,13]、
# b.append(a)
# for i in range(1,len(b)):
#     for j in range(len(b)-1):
#         if b[j+1] < b[j]:
#             t=b[j]
#             b[j]=b[j+1]
#             b[j+1]=t
# print(b)





# 19：用100元买100只鸡，公鸡2元一只，母鸡1元一只，小鸡0.5元一只，问买公鸡、母鸡、小鸡各几只
# a=100
# for i in range(100):
#     for j in range(50):
#         k=100-i-j
#         if i*1+j*2+k*0.5==100:
#             print(i,j,k)




# 20:一个函数，传两个参数a,b，a是数组，b是一个数字，找出a数组中两数只和等于b，打印出来这两个数

# def a(x, y):
#     for i in range(len(x)):
#         for j in range(len(x)):
#             if i != j and y == x[i] + x[j]:
#              print(x[i], x[j])
# a((2, 3, 1, 5), 3)

# def ad ():
#     print('hello')
# ad()
# def qwe():
#     print(123)
# qwe()

# def  wc(x,y,z):
#     x=list(x)
#     d=y+z if  d > len(x):
#         d=len(x)
#     for  i in range(y,d):
#         x.pop(y)
#     b=''.join(x)
#     print(b)
# wc('hdjfehhjdcf',2,12)






#
# import zhuzhu1
# zhuzhu1.asd().zhishu(10)

# import  zlq
# zlq.zz()

# from zhuzhu1 import*
# zz()



#客户端
# while True:
#   import socket
#   sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #创建一个套接字
#   sock.connect(('192.168.0.121',3000))       #连接服务器
#   qq=input('  ')    #将qq当做请求发送给服务器
#   sock.send(qq.encode('utf-8'))
#   ww=sock.recv(1024) #接受响应
#   print(ww.decode('utf-8'))



# import xlwt
# ff=xlwt.Workbook()
# sheet=ff.add_sheet('python_test')
# c=[]
# f=open('a.txt','r',encoding='utf=8')
# a=f.readlines()
# print(a)
# for x in ra:
#   q=a[x]
#   w=q.split(',')
#   c.append(w)
#   print(x)
# f.close()
#print(len(c))
# for i in range(len(c)):
#       for j in range(len(c)):
#          sheet.write(i,j,c[i][j])
# ff.save('qq.xls')



#客户端
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# host=('192.168.0.98',3000)
# while True:
#     msg=input(">>>")
#     s.sendto(msg.encode('utf-8'),host)
#     reg=s.recv(1024)
#     print(reg.decode('utf-8'))






#
# import smtplib     #封装smtp协议
# import email.mime.multipart as mul   #制作邮件
# import email.mime.text as textt   #  对邮件的正文进行处理
# message = mul.MIMEMultipart()  #建立一个空邮件
# message['Subject']='python_test'  #标题
# tt='zhaolq1998@163.com'
# message['From']=tt#发件人
# ww=['973472897@qq.com','17637839607@163.com']
# # message['To']='17637839607@163.com'   #收件人
# message['To']='.'.join(ww)
# txt="""             #正文  多行数据
#   猩猩and狒狒！
#   sfdgdgg
#   """
# tet=textt.MIMEText(txt)
# message.attach(tet)
# smtp123=smtplib.SMTP_SSL('smtp.163.com',465)
# smtp123.login('zhaolq1998@163.com','wzz0106')
# smtp123.sendmail(tt,ww,message.as_string())
# smtp123.close()


#重写
# class  ASD():
#     def zhi(self,x):
#         a=0
#         for i in  range(x+1):
#             a=a+i
#         print(a)
#     def yy(self):
#         print('hello')
#
# import smtplib
# import email.mime.multipart as mul
# import email.mime.text as textt
# message=mul.MIMEMultipart()
# message['project']='python_test'
# tt='zhaolq1998@163.com'
# message['From']= tt
# ff='973472897@qq.com'
# message['To']=ff
# txt="""
#   中国
#   河南
#   """
# tet=textt.MIMEText(txt)
# message.attach(tet)
# smtp123=smtplib.SMTP_SSL('smtp.163.com','465')
# smtp123.login('zhaolq1998@163.com','wzz0106')
# smtp123.sendmail(tt,ff,message.as_string())
# smtp123.close()

# import smtplib
# import email.mime.multipart as map
# message = map.MIMEMultipart()
# import email.mime.text as py
# message['subject'] = 'python_tset1'
# tt = 'zhaolq1998@163.com'
# message['From'] = tt
# ff = '15226018652@163.com'
# message['To']   = ff
# pop = """
# 猪猪最好
# 王猪猪最美
# """
# tet = py.MIMEText(pop)
# message.attach(pop)
# att1 = py.MIMEText(open('a.txt', 'rb').read(), 'base64', 'utf-8')
# att1["Content-Type"] = 'application/octet-stream'
# # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
# att1["Content-Disposition"] = 'attachment; filename="a.txt"'
# message.attach(att1)
#
# amp111 = smtplib.SMTP_SSL('smtp.163.com',465)
# amp111.login('zhaolq1998@163.com','wzz0106')
# amp111.sendmail(tt,ff,message.as_string())
# amp111.close()


# import  socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('192.168.0.84',3000))
# s.listen(3)
# while True:
#     client,addr=s.accept()
#     reg=client.recv(1204)
#     print(reg.decode('utf-8'))
#     msg='wellcome'
#     client.send(msg.encode('utf-8'))




# import os
# os.chdir(r'C:\user')
# print(os.listdir())



# aa=b'\xe4\xbd\xa0\xe5\xa5\xbd'
# a=aa.decode('utf-8')
# print(a)