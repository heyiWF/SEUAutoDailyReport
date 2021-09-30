from selenium import webdriver
import time
import random

def main():
    sleeping = random.randint(0,300)
    print("Sleeping for " + str(sleeping) + " seconds... ")
    time.sleep(sleeping)
    #driver = webdriver.Firefox()
    driver = webdriver.Chrome()
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
    
    try:
        driver.find_element_by_xpath('/html/body/main/article/section/div[2]/div[1]').click()
        time.sleep(5)
        driver.find_element_by_xpath('/html/body/div[11]/div/div[1]/section/div[2]/div/div[4]/div[2]/div[1]/div[1]/div/input').send_keys("36.7")
        driver.find_element_by_xpath('//*[@id="save"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('/html/body/div[62]/div[1]/div[1]/div[2]/div[2]/a[1]').click()
    except Exception:
        print("Operation failed. Please try again. ")
    
    #driver.quit()

if __name__ == '__main__':
   main()

