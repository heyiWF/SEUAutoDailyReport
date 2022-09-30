import time
import random
import requests
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--incognito')

def sendMsg():
    global subject, msg
    # Send notification to WeChat
    posturl = 'https://sctapi.ftqq.com/SendKey.send'
    d = {'title':subject, 'desp':msg}
    r = requests.post(posturl,data=d)
    print(r.text)

def main():
    global subject, msg
    fail = False
    sleeping = random.randint(0,300)
    print("Sleeping for " + str(sleeping) + " seconds... ")
    time.sleep(sleeping)
    try:
        driver = webdriver.Chrome(options=chrome_options)
    except Exception as e:
        msg = "The version of webdriver installed doesn't match your browser. \n\n" + str(e)
        subject = "Daily Report ❌"
        print("Operation failed. The version of webdriver doesn't match. ")
        print(str(e))
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
    url="http://ehall.seu.edu.cn/qljfwapp2/sys/lwReportEpidemicSeu/index.do#/dailyReport"
    try:
        driver.get(url)
    except WebDriverException:
        msg = "Webdriver exception occurred: " + str(e)
        subject = "Daily Report ❌"
        print("Unknown WebDriverException!")
        driver.quit()
        return
    
    checkUrl = driver.current_url
    # Check if you are already logged in
    # If not, then try login using your username and password
    if not checkUrl.startswith("http://ehall.seu.edu.cn/"):
        # Please specify your own username and password!
        driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("YourUsername")
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("YourPassword")
        driver.find_element(By.XPATH, '//*[@id="casLoginForm"]/p[5]/button').click()
    print("Loading webpage... ")
    time.sleep(10)
    
    checkUrl = driver.current_url
    if not checkUrl.startswith("http://ehall.seu.edu.cn/"):
        print("Login failed. ")
        msg = "Failed to sign in. "
        subject = "Daily Report ❌"
        driver.quit()
        return

    print("Successfully logged in. ") 
    try:
        driver.find_element(By.XPATH, '/html/body/main/article/section/div[2]/div[1]').click()
        print("Clicked \'add\', waiting for input... ")
        time.sleep(10)
        temp = round((36.4 + random.randint(0,4) / 10),1)
        driver.find_element(By.NAME, "DZ_JSDTCJTW").send_keys(str(temp))
        print("Input temperature. ")
        driver.find_element(By.ID, "save").click()
        print("Clicked \'save\'")
        time.sleep(3)
        driver.find_element(By.LINK_TEXT, "确认").click()
        print("All done!!")
        msg = 'Today\'s daily report has been successfully submitted. \n\nTemperature is: ' + str(temp)
        subject = 'Daily Report ✅'
    except Exception as e:
        fail = True
        msg = "Oops... Something went wrong. \n\n" + str(e)
        subject = "Daily Report ❌"
        print("Operation failed. Please try again. ")
    
    print(msg)
    driver.quit()
    return fail

if __name__ == '__main__':
   if main():
       main()
   sendMsg()
