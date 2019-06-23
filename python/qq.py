#！/usr/bin/python
# -*- coding:utf-8  -*-
# 九九成发表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(i,j,i*j),end='\t')
#     print()
#      字符串转换
# a='123'
# b=a[::-1]
# c=0
# for i in range(len(b)):
#     for j in range(10):
#         if str(j)==b[i]:
#             c+=j*10**i
# print(type(c))

# 3:
# import os
# import xlwt
# with open('a.txt','r',encoding='utf-8')as f:
#     a=f.readlines()
#     print(a)



# 4:

# import pymysql
# import xlwt
# import xlrd
# conn=pymysql.connect(host='192.168.0.98',port=3306,user='root',passwd='123456')
# m=conn.cursor()
# m.execute('use test')
# with open('b.txt','r',encoding='utf-8')as f:
#     b=f.readlines()
# print(b)
# for i in range(len(b)):
#        c=b[i].split(',')
#        if i==0:
#            m.execute('create table aa({} char(255),{} char(255),{} char(255),{} char(255));'.format(c[0],c[1],c[2],c[3]))
#        else:
#            m.execute('insert into aa values("{}","{}","{}","{}");'.format(c[0],c[1],c[2],c[3]))
#            m.execute('select * from aa;')
#            c=m.fetchall()
# print(c)
# conn.close

# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('192.168.0.98',3000))
# s.listen(3)
# while True:
#      client,addr=s.accept()
#      reg=client.recv(1024)
#      print(reg.decode('utf-8'))
#      msg=input('>>>')
#      client.send(msg.encode('utf-8'))



# import smtplib
# import email.mime.multipart as mul
# import email.mime.text as text
# message =mul.MIMEMultipart()
# message['Subject']='python_test'
# message['From']='zhaolq1998@163.com'
# message['To']='825069672@qq.com'
# txt="""
# 火箭总冠军
# """
# tet=text.MIMEText(txt)
# message.attach(tet)
# att1=text.MIMEText(open('ll.py','rb').read(),'base64','utf-8')
# att1["Content-Type"]='application/octet-stream'
# att1["Content-Disposition"] = 'attachment; filename="ll.py"'
# message.attach(att1)
# smtp123=smtplib.SMTP_SSL('smtp.163.com',465)
# smtp123.login('zhaolq1998@163.com','wzz0106')
# smtp123.sendmail('zhaolq1998@163.com','825069672@qq.com',message.as_string())
# smtp123.close()


#
# import pymysql
# import requests
# import json
# import xlwt
# url='https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=719&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E9%98%80%E9%97%A8&kt=3&=0&_v=0.76993069&x-zp-page-request-id=15bcdb0ebcb9429caa38f21c62074be9-1558592659420-447654'
# head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
# res=requests.get(url,headers=head)
# hh=res.content.decode('utf-8')
# a = json.loads(hh)
# with open('a.txt','w',encoding='utf-8')as f:
#  for i in range(22):
#       x=(a['data']['results'][i]['salary'])
#       x1=(a['data']['results'][i]['jobName'])
#       x2=(a['data']['results'][i]['welfare'])
#       x3=(a['data']['results'][i]['company']['name'])
#       f.write('{}   {}   {}   {}'.format(x3,x1,x,x2))
#       f.write('\n')
# f.close()
# f=open('b.txt','w+',encoding='utf-8')
# for  i in range(88):
#     b1=a['data']['results'][i]['company']['name']
#     b2=a['data']['results'][i]['jobName']
#     b3=a['data']['results'][i]['salary']
#     b4=a['data']['results'][i]['city']['display']
#     b5=a['data']['results'][i]['eduLevel']['name']
#     # b6=a['data']['results'][i]['welfare']
#     f.write("{},".format(b1))
#     f.write("{},".format(b2))
#     f.write("{},".format(b3))
#     f.write("{},".format(b4))
#     f.write("{}".format(b5))
#     # f.write("{}".format(b6))
#     f.write('\n')
# f=open('b.txt','r',encoding='utf-8')
# a=f.readlines()
# print(a)
# import pymysql
# import xlwt
# ww=xlwt.Workbook('aa.xls')
# sheet=ww.add_sheet('zhilian')
# c=["公司","岗位","工资","地点","学历"]
# for k in range(len(c)):
#     sheet.write(0,k,c[k])
# for l in range(0,len(a)):
#     bb=a[l].split(',')
#     for a1 in range(len(c)):
#         sheet.write(l+1,a1,bb[a1])
# ww.save('aa.xls')
# conn=pymysql.connect(host='192.168.0.200',port=3306,user='root',passwd='123456')
# m=conn.cursor()
# m.execute('use test')
# m.execute('create table zhilian2(公司  char(255),岗位 char(255),工资 char(255),地点 char(255),学历 char(255))')
# for j in range(0,len(a)):
#     bb=a[j].split(',')
#     m.execute('insert into zhilian2 values("{}","{}","{}","{}","{}");'.format(bb[0],bb[1],bb[2],bb[3],bb[4]))


# import requests
# import re
# url = 'http://www.doutula.com/article/list/?page=3'
# head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
# res = requests.get(url,headers=head)
# html = res.content.decode('utf-8')
# patt = re.compile(r'original="http://img.doutula.com/production/uploads/image//(.*?).jpg" ')
# items = patt.findall(html)
# b=0
# for i in items:
#     j = 'http://img.doutula.com/production/uploads/image//{}.jpg'.format(i)
#     print(j)
#     msg = requests.get(j,headers=head)
#     hh = msg.content
#     with open(r'C:\Users\zhuzhu\Desktop\新建文件夹//{}.jpg'.format(b), 'wb') as f:
#         f.write(hh)
#     b += 1
#表情包
# import requests
# import re
# url = 'http://www.doutula.com/article/list/?page=3'
# head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
# res = requests.get(url,headers=head)
# html = res.content.decode('utf-8')
# patt = re.compile(r'original="http://img.doutula.com/production/uploads/image//(.*?).jpg" ')
# items = patt.findall(html)
# b=0
# for i in items:
#     j = 'http://img.doutula.com/production/uploads/image//{}.jpg'.format(i)
#     print(j)
#     msg = requests.get(j,headers=head)
#     hh = msg.content
#     with open(r'C:\Users\zhuzhu\Desktop\新建文件夹//{}.jpg'.format(b), 'wb') as f:
#         f.write(hh)
#     b += 1
# print(len(items))     #打印出图片的个数
# for i in items:
#     j ='http://pic.qiushibaike.com/system/pictures/'+i+'.jpg'
#     msg=requests.get(j,headers=head)
#     hh=msg.content
#     with open('{}.jpg'.format(a),'wb')as f:
#         f.write(hh)
#         a+=1


# import os
# a = os.getcwd()
# aa = os.listdir(a)
# for i in aa:
#     c = str(i)
#     d = c.endswith('.jpg')
#     if d == True:
#         os.remove(i)
for i in range(1,10):
    for j in range(1,10):
       if j <=i:
            print('{}*{}={}'.format(j,i,j*i),end='\t')
       if j==i:
            print()
