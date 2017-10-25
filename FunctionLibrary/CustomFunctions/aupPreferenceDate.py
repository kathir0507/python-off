import ConfigParser
import os
import sys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import FunctionLibrary.CommonFunctions.Commonfunctions as common


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


Config = ConfigParser.ConfigParser()
Root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print Root
Config.read(Root + "/../ObjectLibrary/HomepageObjects.ini")
Config.read(Root+ "/../ObjectLibrary/LoginpageObjects.ini")
Config.read(Root+ "/../DataBank/Datavalue.ini")
Config.read(Root + "/../ObjectLibrary/HomepageObjects.ini")
Config.read(Root + "/../ObjectLibrary/AupPreferencesObject.ini")
Config.read(Root +  "/../ObjectLibrary/AupSchedulerObject.ini")
Config.read(Root +  "/../ObjectLibrary/time.ini")



userName=Config.get('LoginpageObjects', 'username')
passWord=Config.get('LoginpageObjects', 'passsword')
usname_Value=Config.get('Datavalue', 'usname_value')
password_Value=Config.get('Datavalue', 'pssword_value')
firstSiteName = Config.get('AupPreferencesObject', 'td_preferences_id')
siteDeleteBtn = Config.get('AupPreferencesObject', 'btn_preferences_id')
siteConfirmDeleteBtn = Config.get('AupPreferencesObject', 'btn_preferences_confirm')
siteSearchText = Config.get('AupPreferencesObject', 'txt_preferences_gsearch')
actualMessage = Config.get('AupPreferencesObject', 'lbl_prefernces_actual')
expectedMessage = Config.get('AupPreferencesObject', 'Expected_message')
norecordMessage=Config.get('AupPreferencesObject', 'Norecord_messge')
logout=Config.get('AupPreferencesObject', 'lnk_preferences_logout')
check_button=Config.get('AupPreferencesObject', 'Check_new_aup')
confirm_button=Config.get('AupPreferencesObject', 'Check_new_add')
site_count=Config.get('AupPreferencesObject','count_site')
expectedMessage_addsite=Config.get('AupPreferencesObject','Expected_site_message')
home_lnk=Config.get('HomepageObjects', 'img_home_schedulerLink')
aup_shd_lnk=Config.get('AupSchedulerObject', 'lnk_scheduler_PreferenceMenuLink')


def customTestFunctions(driver):

    #         print func_name
    """This function will create the object for AUP preferences view controller and triggers the required
     UI test cases via the class methods"""
    try:
        #             print os.path.abspath(os.curdir)  
        common.loginToCrux(userName,passWord,usname_Value,password_Value,driver)
        # Navigate to AUP preferences page from Home page.
        gotoPreferencesview(common,home_lnk,aup_shd_lnk,driver)
        message =common.find_element(By.XPATH,norecordMessage,driver).text
        time.sleep(10)
        count =message_split(common,driver)
         
        if(message=="No data available in table"):
            populatesite(common,driver)
            return True
#             count =self.populatesite(common,self.actualMessage,self.norecordMessage,driver)
        elif(count>0):
#             //table/tbody/tr[1]/td[16]/button[2]
            common.find_element(By.XPATH,"//table/tbody/tr[1]/td[16]/button[2]",driver).click()
            driver.set_page_load_timeout(10)
            common.find_element(By.XPATH,"//div[11]/div/button[1]",driver).click()
            driver.set_page_load_timeout(10)
            deletePreference(common,firstSiteName,siteDeleteBtn,siteConfirmDeleteBtn,driver)
            time.sleep(10) 
            less_count=message_split(common,driver)
            print less_count
            time.sleep(10)
            populatesite(common,driver)
            actual_count=message_split(common, driver)
            print actual_count
            if(actual_count>less_count):
                return  True
                        
    except AssertionError :
        print (" Tese Case Failed ")
        raise AssertionError
        return False
    
def deletePreference(common, firstSiteName, delete, confirm_del,driver):
    """Delete the table Content"""
     
 
    print "Click on Delete button"
    delButton =common.find_element(By.XPATH, delete,driver)
    delButton.click()
    # Confirm the delete operation
    print "Confirm the delete operation"
    common.find_element(By.XPATH, confirm_del, driver).click()
    driver.set_page_load_timeout(10)
    # Searching for the deleted site
 
 
def gotoPreferencesview(common, schedulerLink, preferenceLink,driver):
    """This function opens the AUP Preferences view"""
    print "On Home page, Clicking on Scheduler Link"
    # You are now on home page. Search scheduler link and click
     
    common.gotoPage(schedulerLink,driver)
     
    print "On Schedueler page, Clicking on AUP Preferences Link"
    # You are on AUP Scheduler main view. find Preference link and Click
    common.gotoPage(preferenceLink,driver)
    driver.set_page_load_timeout(10)
 
def populatesite(common,driver):
    """Populating the site"""
    common.find_element(By.XPATH,"//*[@id='new_aup_preferences_info']",driver).click()
    common.find_element(By.XPATH,"//span[text()='Add']",driver).click()
 
def message_split(common,driver):
    """Spliting the Messages"""
    message_detail=common.find_element(By.XPATH,"//*[@id='aup_pref_info']",driver).text
      
    data = message_detail.split() #split string into a list
 
    count=int(data[5])
    return count    
#                   