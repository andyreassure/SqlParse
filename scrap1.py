import time

from selenium import webdriver

option = webdriver.ChromeOptions()
option.set_headless()
option.add_argument("--disable-gpu")
driver = webdriver.Chrome(executable_path=r"D:\software\Codes\python codes\SqlParse\chromedriver", options=option)
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3)
print(driver.find_element_by_id('content').text)
driver.close()
