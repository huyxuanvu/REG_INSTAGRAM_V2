from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import time, random,json,re
import threading
from info import name,matkhau,username
from tempmail import getcode,getmail
import requests




with open("./data/settup.json","r") as f:
    settup = json.load(f)



class Reg(threading.Thread):
    def __init__(self,settup,luong,name,matkhau,username):
        super().__init__()
        self.settup = settup
        self.luong =luong
        self.name = name
        self.matkhau = matkhau
        self.username = username        
        
        pass       
    def getDriver(self):      # settup chrome
        x= int(self.luong)*400
        y =10   
        option = webdriver.ChromeOptions()
        option.add_argument('--incognito')
        option.add_argument("--disable-blink-features=AutomationControlled")
        
        service = Service("chromedriver.exe")
        driver = webdriver.Chrome(service=service,options=option)
        driver.set_window_rect(x,y,400,600)
        

        return driver
   
    def getmail():
        rep = requests.session()

        request = rep.get("https://10minutemail.net/address.api.php?new=1")
        result = request.json()['mail_get_mail']
        return result

    def getcode():
        rep = requests.session()

        count = 0 
        while True :          
            request000 = rep.get("https://10minutemail.net/address.api.php")       
            mail_list = request000.json()["mail_list"]
            for mail in mail_list :         
                if mail["from"] == '"Instagram" <no-reply@mail.instagram.com>' :
                    sub = mail['subject']           
            if count == 30:
                break
            time.sleep(0.8)
            count += 1          
        regex  = re.findall(r'\d{1}',sub)
        code = ""
        for i in regex:
            code += str(i)
        return code

    def run(self):
        
        driver = self.getDriver()
        driver.get("https://www.instagram.com/accounts/emailsignup/")
        driver.implicitly_wait(5) #chờ 5s đến khi element hiện
        driver.find_element(By.NAME, "emailOrPhone").send_keys(getmail())
        driver.find_element(By.NAME, "fullName").send_keys(self.name)
        try:
            for i in range(2):
                driver.find_element(By.XPATH, '//span[text()="Refresh suggestion"]').click() # chọn tên  
                time.sleep(1)
        except:
            driver.find_element(By.NAME,"username").send_keys(self.username)

        driver.find_element(By.NAME, "password").send_keys(self.matkhau)

        driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[7]/div/button').click() 
        #  driver.find_element(By.XPATH, '//button[text()="Sign up"]').click() 

        driver.implicitly_wait(5)
        
        
        #thang
        Select( driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select")).select_by_index(random.randrange(1,12))
        time.sleep(1)
        #ngay
        Select(driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select")).select_by_index(random.randrange(1,30))
        time.sleep(1)
        #nam
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select").send_keys(random.randrange(1990,2005))
        driver.find_element(By.XPATH, '//button[text()="Next"]').click()
        time.sleep(20)
        driver.find_element(By.NAME,"email_confirmation_code").send_keys(getcode())
        time.sleep(2)
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/button').click()
        time.sleep(15)
        time.sleep(settup["delay1"])
        with open("./data/output.txt","a") as f:
            f.write(getmail()+'|'+self.matkhau +"\n")
           

       


luong = int(input("nhap vao so luong : "))
for i in range(luong):

    t= Reg(settup,luong,name(),matkhau(),username())
    t.start()