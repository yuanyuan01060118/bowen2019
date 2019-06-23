#！/usr/bin/python
# -*- coding:utf-8  -*-



from appium  import webdriver
from time import sleep
#建立与appium服务器需要的参数，以字典的形式
# de= {
#   "platformName": "Android",
#   "platformVersion": "6.0.1",
#   "deviceName": "3493f5137d54",
#   "appPackage": "com.tencent.tim",
#   "appActivity": "com.tencent.mobileqq.activity.SplashActivity",
#   "noReset": "true"
# }
# #http:127.0.0.1:4723/wdd/hub 固定的，写死localhost=127.0.0.1
# #测试脚本与appium
# dr =webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=de)
# #层级定位
# sleep(5)
#
# # dr.find_element_by_accessibility_id('清除帐号').click()
# dr.find_element_by_class_name('android.widget.Button').click()
# dr.find_element_by_id('请输入QQ号码或手机或邮箱').clear()
# dr.find_element_by_accessibility_id('请输入QQ号码或手机或邮箱').send_keys('983472897')
# dr.find_element_by_id('com.tencent.tim:id/password').send_keys('wzz01060118..')
# a=dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')
# dr.find_element_by_id('com.tencent.tim:id/login').click()
# print(a)
# for i in a :
#     sleep(0.5)
#     i.click()
#     sleep(2)


#滑动 ：  第一步：获取手机屏幕大小
# s=dr.get_window_size()
# # 第二步：放缩x.y轴
# print(s)
# x1=s['width']*0.5
# y1=s['height']*0.25
# y2=s['height']*0.75
# #第三步：使用swipe方法，进行滑动操作
# dr.swipe(x1,y1,x1,y2)
# sleep(5)
# dr.quit()


#点击办公
#dr.find_element_by_id('android:id/tabs').find_element_by_class_name('android.widget.FrameLayout')[2].click()
# dr.find_element_by_accessibility_id('好友动态').click()


from appium import webdriver
from time import sleep


#面向对象
# class Tim(object):

  # 初始化属性
  # def __init__(self):
  #   # 建立与appium服务器需要的参数，以字典的形式
  #   self.des = {
  #     "device": "android",
  #     "platformName": "Android",
  #     "platformVersion": "6.0.1",
  #     "deviceName": "3493f5137d54",
  #     "appPackage": "com.tencent.tim",
  #     "appActivity": "com.tencent.mobileqq.activity.SplashActivity",
  #     "noReset": "true",
  #   }
  #   # http://127.0.0.1:4723/wd/hub 固定的，写死localhost==127.0.0.1
  #   # 测试脚本与appium服务器建立一个session连接
  #   self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.des)
  #   sleep(5)

  # def dian_zan(self):
  #   # 第一步，点击办公
  #   self.dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')[
  #     -1].click()
  #   # 第二步，点击好友动态
  #   t = self.dr.find_element_by_id('com.tencent.tim:id/lebasv').find_elements_by_class_name(
  #     'android.widget.RelativeLayout')
  #   t[-1].click()
  #   sleep(0.5)
  #   # 第三步 点赞
  #   x = self.dr.find_elements_by_class_name('android.widget.ImageView')
  #   print(x)
  #   x[1].click()
  #   sleep(2)
  #   x[2].click()
#获取文字
  # def get_wenzi(self):
  #     a = self.dr.find_element_by_id('com.tencent.tim:id/ivTitleName').text
  #     print(a)
  #     return a
#按键操作
  # def anjian(self):
  #模拟人点击物理按键
    #self.dr.keyevent(3)
    # sleep(10)
  #照相机拍照
    # self.dr.keyevent(27)
# 调用类
# if __name__ == '__main__':
#   yasuo = Tim()
  # yasuo.get_wenzi()
  # yasuo.anjian()

#生成html测试报告
import HTMLTestReportCN
#用于单元测试，验证预期与实际结果是否一致，一致通过，不一致失败
import unittest
# class T(unittest.TestCase):
 #测试用例方法，必须以test
  # def test_1(self):
         #预期结果
        # x="宝马"
        #实际结果
        # y="劳斯莱斯"
         #第一个断言方法，判断预期结果与实际结果是否相等
         #x，y位置是可以互换的
        # self.assertEquals(x,y,msg="msg的作用就是填写备注信息")
# if __name__=='__main__':
  #使用unittest类的main
  # unittest.main()
  ##############生成测试报告##########
  #第一步：创一个测试套件，理解成玩具枪的弹夹
  # suite=unittest.TestSuite()
  #第二步：向测试套件里面添加测试用例，理解往玩具枪里加子弹
  # suite.addTest(T('test_1'))
  # suite.addTest(T('test_2'))
  #第三步：将形成的测试结果写入html文件里，理解成玩具枪上膛

  # with open('a.html','wb',) as fb:
  #    runner=HTMLTestReportCN.HTMLTestRunner(
  #      stream=fb,
  #      title='报告名称',
  #      description='报告描述',
  #      verbosity=2 ,#输出内容的详细等级，默认是0，2代表最详细
  #    runner.run(suite)