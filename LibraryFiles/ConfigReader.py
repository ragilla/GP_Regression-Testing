import configparser

def readConfigData(section, key):
    config = configparser.ConfigParser()
    config.read("../ConfigurationFiles/Config.cfg")
    return config.get(section,key)

def fetchElementLocators(section_1, key_1):
    config = configparser.ConfigParser()
    config.read("../ConfigurationFiles/Config.cfg")
    return config.get(section_1,key_1)
