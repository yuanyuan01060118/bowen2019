# ！/usr/bin/python
# -*- coding:utf-8  -*-

# 登录模块
from selenium  import  webdriver
from time  import sleep
dr=webdriver.Chrome()
dr.get('https://www.alltuu.com')
# sleep(2)
# dr.switch_to.frame('login_frame') #iframe 内嵌框架（窗口） 切换到某个框架上去 id name 属性可以切换
sleep(2)
dr.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[2]/ul/li[2]/div/a[1]').click()
sleep(2)
# dr.switch_to.frame('login_frame')
sleep(2)
dr.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/section[2]/div/input').send_keys('13781160311')
dr.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/section[3]/div/input').send_keys('zhuzhuzhu')
dr.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/section[4]/div').click()
