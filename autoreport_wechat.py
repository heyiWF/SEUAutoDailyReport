import time
import smtplib
import random
import requests
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

def sendMsg():
    global subject, msg
    # Send notification to WeChat
    posturl = 'https://sctapi.ftqq.com/SCKEY.send'
    d = {'title':subject, 'desp':msg}
    r = requests.post(posturl,data=d)
    print(r.text)

def main():
    global subject, msg
    sleeping = random.randint(0,300)
    print("Sleeping for " + str(sleeping) + " seconds... ")
    time.sleep(sleeping)
    try:
        #driver = webdriver.Firefox()
        driver = webdriver.Chrome(options=chrome_options)
        #driver = webdriver.Chrome()
        #driver.maximize_window()
    except Exception as e:
        msg = "The version of webdriver installed doesn't match your browser. \n\n" + str(e)
        subject = 'Daily Report Failed'
        print("Operation failed. The version of webdriver doesn't match. ")
        sendMsg()
        return
    driver.implicitly_wait("3")
    
    '''
    *********************************
    *                               *
    * Start opening URL here.       *
    * Try it on your browser first! *
    *                               *
    *********************************
    '''
    url="http://ehall.seu.edu.cn/qljfwapp2/sys/lwReportEpidemicSeu/index.do?t_s=1583641506865#/dailyReport"
    driver.get(url)
    
    checkUrl = driver.current_url
    # Check if you are already logged in
    # If not, then try login using your username and password
    if not checkUrl.startswith("http://ehall.seu.edu.cn/"):
        # Please specify your own username and password!
        driver.find_element_by_xpath('//*[@id="username"]').send_keys("YourUsername")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("YourPassword")
        driver.find_element_by_xpath('//*[@id="casLoginForm"]/p[5]/button').click()
    time.sleep(5)
    
    checkUrl = driver.current_url
    if not checkUrl.startswith("http://ehall.seu.edu.cn/"):
        print("Login failed. ")
        driver.quit()
        return
   
    print("Successfully logged in. ") 
    try:
        driver.find_element_by_xpath('/html/body/main/article/section/div[2]/div[1]').click()
        print("Clicked \'add\'")
        time.sleep(5)
        temp = round((36.4 + random.randint(0,4) / 10),1)
        driver.find_element_by_xpath('/html/body/div[11]/div/div[1]/section/div[2]/div/div[4]/div[2]/div[1]/div[1]/div/input').send_keys(str(temp))
        print("Input temperature. ")
        driver.find_element_by_xpath('//*[@id="save"]').click()
        print("Clicked \'save\'")
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[60]/div[1]/div[1]/div[2]/div[2]/a[1]').click()
        print("All done!!")
        msg = 'Today\'s daily report has been successfully submitted. \n\nTemperature is: ' + str(temp)
        subject = 'Daily Report Succeeded'
    except Exception as e:
        msg = 'Oops... Something went wrong. \n\n' + str(e)
        subject = 'Daily Report Failed'
        print("Operation failed. Please try again. ")
    
    sendMsg()
    driver.quit()

if __name__ == '__main__':
   main()

