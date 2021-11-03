from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from Library import ConfigReader

def startBrowser():
    global driver
    if ConfigReader.configreader('Details','Browser')=='Chrome':
        path = './Driver/chromedriver.exe'
        driver = Chrome(executable_path=path)
    elif ConfigReader.configreader('Details','Browser')=='Firefox':
        path = './Driver/geckodriver.exe'
        driver = Firefox(executable_path=path)

    print(ConfigReader.configreader('Details','App_Url'))
    Ul=ConfigReader.configreader('Details','App_Url')
    print(type(Ul))
    driver.get(Ul)
    # driver.get(ConfigReader.configreader('Details','App_Url'))
    driver.maximize_window()
    return driver

def closeBrowser():
    driver.close()