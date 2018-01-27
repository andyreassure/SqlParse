from selenium import webdriver

option = webdriver.ChromeOptions()
option.set_headless()
option.add_argument("--disable-gpu")
option.add_experimental_option("useAutomationExtension", False)
executable_path = r"D:\software\Codes\python codes\SqlParse\chromedriver"
