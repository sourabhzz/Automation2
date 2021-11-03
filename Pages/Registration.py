from Library import ConfigReader


class registration():
    def __init__(self,Driver):
        global driver
        driver=Driver


    def username(self,username):
        driver.find_element_by_name(ConfigReader.elementreader('Registration', 'Username')).send_keys(username)

    def email(self, email):
        driver.find_element_by_xpath(ConfigReader.elementreader('Registration', 'Email')).send_keys(email)
