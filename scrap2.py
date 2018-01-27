from selenium import webdriver
import scrap0


scrap0.option.set_headless(False)
driver = webdriver.Chrome(executable_path=scrap0.executable_path, options=scrap0.option)
url = r'https://kyfw.12306.cn/otn/index/initMy12306'
driver.get(url)
print(driver.page_source)
# driver.close()