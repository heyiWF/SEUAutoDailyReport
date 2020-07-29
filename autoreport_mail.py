import time
import smtplib
import random
from email.mime.text import MIMEText
from email.header import Header
from selenium import webdriver
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-gpu')
#chrome_options.add_argument('--no-sandbox')

def main():
    time.sleep(random.randint(0,300))
    mail_host="smtp.qq.com"
    mail_user="YourEmail@qq.com"
    mail_pass="YourMailToken"
    sender = 'YourEmail@qq.com' # Must be the same as mail_user
    receivers = ['YourEmail@qq.com'] # The email address you want to receive the result
    driver = webdriver.Firefox()
    #driver = webdriver.Chrome(chrome_options=chrome_options)
    #driver = webdriver.Chrome()
    #driver.maximize_window()
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
        temp = round((36.4 + random.randint(0,4) / 10),1) # Generate a random number between 36.4 and 36.8
        driver.find_element_by_xpath('/html/body/div[11]/div/div[1]/section/div[2]/div/div[4]/div[2]/div[1]/div[1]/div/input').send_keys(str(temp))
        print("Input temperature. ")
        driver.find_element_by_xpath('//*[@id="save"]').click()
        print("Clicked \'save\'")
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[60]/div[1]/div[1]/div[2]/div[2]/a[1]').click()
        print("All done!!")
        message = MIMEText('Today\'s daily report has been successfully submitted. Temperature is: ' + str(temp), 'plain', 'utf-8')
        message['From'] = Header("AutoReportBot", 'utf-8')
        message['To'] =  Header("Master", 'utf-8')
        subject = 'Daily Report Succeeded'
        message['Subject'] = Header(subject, 'utf-8')
    except Exception as e:
        msg = 'Oops... Something went wrong. \n' + str(e)
        message = MIMEText(msg, 'plain', 'utf-8')
        message['From'] = Header("AutoReportBot", 'utf-8')
        message['To'] =  Header("Master", 'utf-8')
        subject = 'Daily Report Failed'
        message['Subject'] = Header(subject, 'utf-8')
        print("Operation failed. Please try again. ")
    
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 587)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    driver.quit()

if __name__ == '__main__':
   main()
