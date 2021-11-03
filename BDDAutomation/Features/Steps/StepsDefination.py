from selenium.webdriver import Chrome
from behave import *

@given(u'user is on registration page')
def step_impl(context):
    path = '../Driver/chromedriver.exe'
    context.driver = Chrome(executable_path=path)
    context.driver.get('http://www.theTestingWorld.com/testings')

@when(u'user enters user name')
def step_impl(context):
    context.driver.find_element_by_name('fld_username').send_keys('Sourav')


@when(u'user enters password')
def step_impl(context):
    print ('ok')


@when(u'user enters email id')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@placeholder='myusername@gmail.com']").send_keys('email@gmail.com')

@when(u'user click on signup')
def step_impl(context):
    print ('ok')


@then(u'user should be registered successfully')
def step_impl(context):
    print ('ok')

@when(u'user enters duplicate user name')
def step_impl(context):
    print ('ok')

