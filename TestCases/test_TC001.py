from Base import InitiateDriver
from Pages import Registration
import pytest
from Data  import  Datagenerator


@pytest.mark.parametrize('data',Datagenerator.datagenrator())

def test_TC0001(data):
    driver= InitiateDriver.startBrowser()
    reg= Registration.registration(driver)
    reg.username(data[0])
    # driver.find_element_by_name(ConfigReader.elementreader('Registration','Username')).send_keys("Sourav")
    driver.implicitly_wait(10)
    reg.email(data[1])
    # driver.find_element_by_xpath(ConfigReader.elementreader('Registration','Email')).send_keys("writetosourabhz@gmail.com")

