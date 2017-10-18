'''
The first test using selenium
'''
import time, datetime
from selenium import webdriver
def main2():
    chrome_driver = r'C:\Users\Frank.Wang\chromedriver.exe'
    driver = webdriver.Chrome(chrome_driver)
    site = 'https://onecard.network/client/en_AU/charlessturt/search/'
    
    driver.get(site)
    time.sleep(3)
    tlogin = driver.find_element_by_class_name('loginLink')
    tlogin.click()
    time.sleep(3)
    tt = driver.find_element_by_xpath('//*[@id="loginModal"]/iframe')
    driver.switch_to_frame(tt)
    t_username = driver.find_element_by_xpath('//*[@id="j_username"]')
    t_username.send_keys('X0201701885')
    t_password = driver.find_element_by_xpath('//*[@id="j_password"]')
    t_password.send_keys('100726')
    t_submit = driver.find_element_by_xpath('//*[@id="submit_0"]')
    time.sleep(3)
    t_submit.click()
    time.sleep(5)
    site2 = 'https://onecard.network/client/en_AU/charlessturt/search/account?dt=list'
    driver.get(site2)
    time.sleep(5)
    t_over = driver.find_element_by_xpath('//*[@id="checkoutsSummary"]/h3/div[2]/span')
    print(t_over.text)
    

if __name__ == '__main__':
    start = datetime.datetime.now()
    print('Start:', start)
    main2()
    end = datetime.datetime.now()
    print('End:', end)
    print('Duration:', end - start)