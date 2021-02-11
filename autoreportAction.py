import time
import random
import requests
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

from sys import argv
_, username, password, sckey = argv

def main():
    global subject, msg
    fail = False
    sleeping = random.randint(0,300)
    print("Sleeping for " + sleeping + " seconds... ")
    time.sleep(sleeping)
    driver = webdriver.Chrome(options=chrome_options)
    #driver = webdriver.Chrome()
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
        driver.find_element_by_xpath('//*[@id="username"]').send_keys(f"{username}")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(f"{password}")
        driver.find_element_by_xpath('//*[@id="casLoginForm"]/p[5]/button').click()
    time.sleep(30)
    
    checkUrl = driver.current_url
    if not checkUrl.startswith("http://ehall.seu.edu.cn/"):
        print("Login failed. ")
        driver.quit()
        return
   
    print("Successfully logged in. ") 
    try:
        driver.find_element_by_xpath('/html/body/main/article/section/div[2]/div[1]').click()
        print("Clicked \'add\'")
        time.sleep(30)
        temp = round((36.4 + random.randint(0,4) / 10),1)
        driver.find_element_by_xpath('/html/body/div[11]/div/div[1]/section/div[2]/div/div[4]/div[2]/div[1]/div[1]/div/input').send_keys(str(temp))
        print("Input temperature. ")
        driver.find_element_by_xpath('//*[@id="save"]').click()
        print("Clicked \'save\'")
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[60]/div[1]/div[1]/div[2]/div[2]/a[1]').click()
        print("All done!!")
        subject = 'Daily Report Succeeded'
        msg = 'Today\'s daily report has been successfully submitted. Temperature is: ' + str(temp)
    except Exception as e:
        fail = True
        msg = 'Oops... Something went wrong. \n' + str(e)
        subject = 'Daily Report Failed'
        print("Operation failed. Please try again. ")

    driver.quit()
    return fail

if __name__ == '__main__':
    # Try twice before reporting a failure
    if main():
        main()
    
    # Send notification to WeChat
    if not sckey == '':
        posturl = f'https://sc.ftqq.com/{sckey}.send'
        d = {'text':subject, 'desp':msg}
        r = requests.post(posturl,data=d)
        print(r.text)

