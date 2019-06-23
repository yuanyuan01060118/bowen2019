#！/usr/bin/python
# -*- coding:utf-8  -*-


from appium  import webdriver
from time import sleep
de={
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "emulator-5554",
  "appPackage": " com.alltuu.android",
  "appActivity": "android.alltuu.com.newalltuuapp.home.HomeActivity",
  "noReset": "true"
}
dr =webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=de)
sleep(10)
dr.find_elements_by_class_name('android.widget.EditText')[1].send_keys('13781160311')
dr.find_element_by_class_name('android.view.View')[-1].send_keys('13781160311')