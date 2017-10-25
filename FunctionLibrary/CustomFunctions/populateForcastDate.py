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

from string import lstrip
from selenium.common.exceptions import NoSuchElementException


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


Config = ConfigParser.ConfigParser()
Root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

Config.read(Root + "/../ObjectLibrary/HomepageObjects.ini")
Config.read(Root+ "/../ObjectLibrary/LoginpageObjects.ini")
Config.read(Root+ "/../DataBank/Datavalue.ini")
Config.read(Root + "/../ObjectLibrary/HomepageObjects.ini")
Config.read(Root + "/../ObjectLibrary/ProductreleaseinfoObject.ini")
Config.read(Root +  "/../ObjectLibrary/AupSchedulerObject.ini")
Config.read(Root +  "/../ObjectLibrary/AupPreferencesObject.ini")
Config.read(Root +  "/../ObjectLibrary/time.ini")

url=Config.get('LoginpageObjects', 'URL')
userName=Config.get('LoginpageObjects', 'username')
passWord=Config.get('LoginpageObjects', 'passsword')
usname_Value=Config.get('Datavalue', 'usname_value')
password_Value=Config.get('Datavalue', 'pssword_value')
home_lnk=Config.get('HomepageObjects', 'img_home_schedulerLink')
product_release_info=Config.get('ProductreleaseinfoObject', 'menu_product_release_id')
product_release_Addnew=Config.get('ProductreleaseinfoObject', 'new_product_release_info_id')
dropdown=Config.get('ProductreleaseinfoObject','dropdown')
prod_release_date=Config.get('ProductreleaseinfoObject','prod_release_date')
patch_date=Config.get('ProductreleaseinfoObject','patch_date')
addbutton=Config.get('ProductreleaseinfoObject','Addbutton')
siteSearchText = Config.get('ProductreleaseinfoObject', 'txt_preferences_gsearch')
home_lnk_page=Config.get('ProductreleaseinfoObject', 'home_lnk_page')
Admin_lnk=Config.get('ProductreleaseinfoObject', 'Admin_lnk')
view_lnk=Config.get('ProductreleaseinfoObject', 'view_lnk')
cron2_lnk=Config.get('ProductreleaseinfoObject', 'cron2_lnk')
run=Config.get('ProductreleaseinfoObject', 'run')
  
def customTestFunctions(driver):
    """To Run the Cron2 Job"""
  
    try:
        common.loginToCrux(userName,passWord,usname_Value,password_Value,driver)
#             gotoPreferencesview(common,home_lnk,product_release_info,driver)
        print "Clicking scheduler menu in the home page "
        common.gotoPage(home_lnk,driver)
        common.pageLoadTime(10,driver)
        print "Clicking Product Release Information menu Scheduler Page "
        common.gotoPage(product_release_info,driver)
        print "Deleting entire Product release Details"
        bool_Delete=common.delete_table(driver)
        print"If the Forecast date exists Delete"
        if(bool_Delete):
            form_string=add_details(driver, product_release_Addnew)
            bool_value=common.select_by_text(driver,dropdown,form_string)
            common.pageLoadTime(10, driver)
            if(bool_value):
                actual_info=prodcut_release_info(driver,common,prod_release_date,patch_date,addbutton,siteSearchText,form_string)
                alert_mes=cronjob2_run(common,driver,home_lnk_page,Admin_lnk,cron2_lnk,view_lnk,run)
                assert alert_mes=="Finished"
                return True
         
        else:
            print"If Forecast date Not exists Create New one" 
            form_string=add_details(driver, product_release_Addnew)
            common.pageLoadTime(10, driver)
            bool_value=common.select_by_text(driver,dropdown,form_string)
            prodcut_release_info(driver,common,prod_release_date,patch_date,addbutton,siteSearchText,form_string)
            alert_mes=cronjob2_run(common,driver,home_lnk_page,Admin_lnk,cron2_lnk,view_lnk,run)
            assert alert_mes=="Finished"
            return True
    
    except NoSuchElementException:
        print (" Tese Case Failed ")
        raise NoSuchElementException
        return False
        
    except AssertionError :
        print (" Tese Case Failed ")
        raise AssertionError
        return False

    
def add_details(driver,product_addnew):
    """To Add details in the Site"""
    common.gotoPage(product_addnew,driver)
    common.pageLoadTime(10,driver)
    print "Current month"      
    currentmonth=common.timestampMonth()
    print currentmonth  
    print "Current Year"    
    currentyear=common.timestampYear()
    print "Release date"
    release=datecalculation(driver,common,currentmonth)
    print release  
    print"Form String"
    form_string=formstring(driver,release,currentyear)
    print form_string
    return form_string


def datecalculation(driver,common,curmonth):
    """To Caculate the date"""
    first_term_release=['February','March','April']
    second_term_release=['May','June','July']
    third_term_release=['August','September','October']
    fourth_term_release=['November','December','January']
    
    if curmonth in first_term_release:
        return "February"
    elif curmonth in second_term_release:
        return "May"
    elif curmonth in third_term_release:
        return "August"
    else:
        return "November" 
    
def cronjob2_run(common,driver,home_lnk_page,Admin_lnk,cron2_lnk,view_lnk,run):
    
    print "Returning Home page"
    common.gotoPage(home_lnk_page,driver)
    common.pageLoadTime(10,driver)
    print "Clicking on Admin page"
    common.gotoPage(Admin_lnk,driver)
    common.pageLoadTime(10,driver)
    print "Clicking on View page"
    common.gotoPage(view_lnk,driver)
    common.pageLoadTime(10,driver)
    print "Clicking on Cron2 Tab"
    common.gotoPage(cron2_lnk,driver)   
    time.sleep(10)

    print "Running Cron"
    job_id=int(common.find_element(By.XPATH,"//tr[1]/td[1]",driver).text)
    common.gotoPage(run,driver)
    time.sleep(10)
    alert_msg=common.alert_present(driver)
    time.sleep(10)

    print "JoB Id"
    job_id_new=job_id+1
    time.sleep(10)
    print job_id_new
    print "After Running cron looks for the text"
    time.sleep(10)
    cron2_txt=common.find_element(By.XPATH,"//tr[1]/td[2]",driver).text
    print cron2_txt
    print "After CronRun looks for the message"
    afterrun_message_txt=common.find_element(By.XPATH,"//tr[1]/td[5]",driver).text
#         print afterrun_message_txt
#         print cron2_txt
    time.sleep(10)
    
    if(job_id!=job_id_new and cron2_txt=="AUP Forecast Date Generation('Job 2')" and "Forecast Date generated for sites:" in afterrun_message_txt):
        return "Finished"
    
    else:
        return "Failed"
    
    
def prodcut_release_info(driver,common,prod_release_date,patch_date,addbutton,siteSearchText,form_string):
    print "Select Current Date"
    cdate=common.currentdate()
    time.sleep(10)
    print cdate
    common.find_element(By.XPATH,prod_release_date, driver).send_keys(cdate)
    common.pageLoadTime(10, driver)
    common.find_element(By.XPATH,prod_release_date, driver).send_keys(Keys.ENTER)
    time.sleep(10)
    print "Select Next Date"
    patchdate=common.nextdate()
    time.sleep(10)
    print patchdate
#         patch_xpath="//a[text()='"+patch+"']"
#         print patch_xpath     
    common.pageLoadTime(10, driver)
    common.find_element(By.XPATH,patch_date, driver).send_keys(patchdate)
#         common.find_element(By.XPATH,patch_date, driver).send_keys(Keys.ENTER)
    common.pageLoadTime(10, driver)
    print "Clicking on the Add Date"
    common.find_element(By.XPATH,addbutton,driver).click()
    print "searching for the Product release Version"
    common.find_element(By.XPATH,siteSearchText,driver).send_keys(form_string)
    common.find_element(By.XPATH,siteSearchText, driver).send_keys(Keys.ENTER)
    text_td="//td[text()='"+form_string+"']"
    Actual_prod=common.find_element(By.XPATH,text_td,driver).text
    return Actual_prod
    
def formstring(driver,release,year):
    str="Oracle Service Cloud "+release+" "+year
    return str