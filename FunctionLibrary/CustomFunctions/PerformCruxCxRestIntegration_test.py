import ConfigParser
from datetime import date, timedelta
import datetime
import os
import sys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
import FunctionLibrary.CommonFunctions.Commonfunctions as common 

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


Config = ConfigParser.ConfigParser()
Root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

Config.read(Root + "/../ObjectLibrary/HomepageObjects.ini")
Config.read(Root+ "/../ObjectLibrary/LoginpageObjects.ini")
Config.read(Root+ "/../DataBank/Datavalue.ini")
Config.read(Root + "/../ObjectLibrary/HomepageObjects.ini")
Config.read(Root +  "/../ObjectLibrary/PerformCruxCxRestIntegrationObject.ini")
Config.read(Root +  "/../ObjectLibrary/time.ini")

url=Config.get('LoginpageObjects', 'URL')
userName=Config.get('LoginpageObjects', 'username')
passWord=Config.get('LoginpageObjects', 'passsword')
usname_Value=Config.get('Datavalue', 'usname_value')
password_Value=Config.get('Datavalue', 'pssword_value')
aup_shd_lnk=Config.get('PerformCruxCxRestIntegration', 'menu_id')
home_lnk=Config.get('HomepageObjects', 'img_home_schedulerLink')
check_box=Config.get('PerformCruxCxRestIntegration', 'check_box')
change_button=Config.get('PerformCruxCxRestIntegration', 'change_date_button')
site_forecast_date=Config.get('PerformCruxCxRestIntegration','site_forecast_date')
change_button_submit=Config.get('PerformCruxCxRestIntegration','change_button_submit')
home_lnk_page=Config.get('PerformCruxCxRestIntegration', 'home_lnk_page')
Admin_lnk=Config.get('PerformCruxCxRestIntegration', 'Admin_lnk')
view_lnk=Config.get('PerformCruxCxRestIntegration', 'view_lnk')
cron4_lnk=Config.get('PerformCruxCxRestIntegration', 'cron4_lnk')
run=Config.get('PerformCruxCxRestIntegration', 'run')
  
def customTestFunctions(driver):
    try:
        common.loginToCrux(userName,passWord,usname_Value,password_Value,driver)
             
    except AssertionError :
        print (" Tese Case Failed ")
        raise AssertionError
        return False
