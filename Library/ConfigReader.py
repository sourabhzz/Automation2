import configparser

def configreader(section,key):
    config= configparser.ConfigParser()
    config.read('./ConfigurationFiles/config.cfg')
    return config.get(section,key)

def elementreader(section,key):
    config= configparser.ConfigParser()
    config.read('./ConfigurationFiles/element.cfg')
    return config.get(section,key)



