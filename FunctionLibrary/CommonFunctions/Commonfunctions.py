from _elementtree import iselement
from datetime import timedelta
import datetime
import os
import string
from telnetlib import EC
import time

import moment
import pytest
from pytz import timezone
import pytz
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, \
    NoAlertPresentException, TimeoutException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


now = moment.now().strftime("%d-%m-%Y")
path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
screen_dir = os.path.join(path, "screenshot", str(now))
        
def loginToCrux(obj_username,obj_password, username_value, pwd_value,driver):
    """Login to CRUX"""
    
    print "Login to CRUX"

    username_field= find_element(By.NAME,obj_username,driver)
    username_field.clear()
    username_field.send_keys(username_value)

    Password_field =find_element(By.NAME,obj_password,driver)
    Password_field.clear()
    Password_field.send_keys(pwd_value)
    #Press Enterkey
    Password_field.send_keys(Keys.ENTER)
   
    time.sleep(10)
    
def logoutFromCrux( logoutlink,driver):
    """Logout Function"""
    
    print "Logout from CRUX and Kill the browser object"
    find_element(By.CSS_SELECTOR,logoutlink,driver).click()
#         
    driver.set_page_load_timeout(20)
    
    print "Test Completed"
#    
def gotoPage(Aup_id,driver):
    """This function is used to navigate to specific page given
    as a parameter"""
    
    find_element(By.XPATH,Aup_id,driver).click()
    

def alert_present(driver):
    """To handle alert"""
    try:
        driver.switch_to_alert().accept()
        return True
    except NoAlertPresentException: 
        return False
    

def find_element(by_type,locator,driver):
    
    delay = 45  # seconds
    try:
        return WebDriverWait(driver, delay).until(EC.presence_of_element_located((by_type, locator)))
    except TimeoutException:
        print "Following element is not found "+locator


def is_elementsPresent( how, what, driver):
    """
    Helper method to confirm the presence of an element on page
    :params how: By locator type
    :params what: locator value
    """
    try:
        elements = driver.find_elements(by=how, value=what)
       
        return elements
    except NoSuchElementException as e:
        e.message
        print("Following element not found " + what)
        raise NoSuchElementException
    
def timestamp():
    """To get the current time"""
    date_format='%Y-%m-%d %H'
    date = datetime.datetime.now(tz=pytz.utc)
#         print 'Current date & time is:', date.strftime(date_format)
    
    date = date.astimezone(timezone('US/Pacific'))
    
    return date.strftime(date_format)

def timestampMonth():
    """To get the current month"""
    date_format='%Y-%m-%d %H'
    date = datetime.datetime.now()
    return date.strftime("%B")

def timestampYear():
    """To get the current year"""
    date_format='%Y-%m-%d %H'
    date = datetime.datetime.now()
    return date.strftime("%Y")

def currentdate():
    """To get the current date"""
    format='%d-%B-%Y'
    date=datetime.datetime.now()
    return date.strftime(format)

def nextdate():
    """To get the nextdate"""
    format='%d-%B-%Y'
    today=datetime.datetime.now()
    nextday=(today + timedelta(days=3)).strftime("%d-%b-%Y")
    return nextday

def is_present( how, what, driver):
    """
    Helper method to confirm the presence of an element on page
    :params how: By locator type
    :params what: locator value
    """
    try:
        element = driver.find_element(by=how, value=what)
        return True
    except NoSuchElementException as e:
        e.message
        return False

def is_exists( how, what, driver):
    """
    Helper method to confirm the presence of an element on page
    :params how: By locator type
    :params what: locator value
    """
    try:
        element = driver.find_element(by=how, value=what)
        return True
    except NoSuchElementException as e:
        e.message
        print("Following element not found " + what)
        raise NoSuchElementException
    
    
def pageLoadTime(timesec,driver):
    """To get the PageLoadtime"""
    try:
        driver.set_page_load_timeout(timesec)
       
    except NoSuchElementException as e:
        e.message
        print("Timeout Error " +timesec)
        
        
def string_split(content,spliter,driver):
    """To get the String split"""
    try:
        message=find_element(By.XPATH,content,driver).text
        mes = []
#            membersL = [memb.split("\n")[1] for memb in message]
        for i in message.split("\n"):
            mes.append(i)
        return mes
    except NoSuchElementException as e:
        e.message
        print("Error"+e.message )

def select_by_text(driver,dropdown_name,form_string):
    """To select the item by text"""
    try:
        select=find_element(By.XPATH,dropdown_name,driver)
        sel = Select(select)
        sel.select_by_visible_text(form_string)
        return True
    except NoSuchElementException as e:
        e.message
        print("Error"+e.message )

def screenshotsOnFailure(testName,driver,Root):
        """This function is used to navigate to specific page given
        as a parameter"""
        print Root+"\\Screenshots\\"+testName+".png"
        driver.save_screenshot(Root+"\\Screenshots\\"+testName+".png")
        
def delete_table(driver):
    """ Delete the table content by clicking delete Button"""
    count=0
    trElement = driver.find_elements_by_xpath("//span[text()='Delete']")
    buttoncount=len(trElement)
    for x in range(0, buttoncount):     
        if(is_present(By.XPATH, "//span[text()='Delete']", driver)):
            find_element(By.XPATH, "//span[text()='Delete']", driver).click()
            find_element(By.XPATH, "//span[text()='Confirm']", driver).click()
            count=count+1
           
        else:
            count=0    
    if(count>0):
        return True
    else:
        return False
    
    
def is_exists_condition( how, what, driver):
    """
    Helper method to confirm the presence of an element on page
    :params how: By locator type
    :params what: locator value
    """
    try:
        element = driver.find_element(by=how, value=what)
        return True
    except NoSuchElementException as e:
        return False   
    
def screen_path():
    global screen_dir
    if not os.path.exists(screen_dir):
        os.makedirs(screen_dir)
        os.chmod(screen_dir, 0755)
    return screen_dir


def remove_special_characters(text):
    return text.translate(string.maketrans('', ''), '\ / : * ? " < > |')


def save_screenshot(driver, name):
    _name = remove_special_characters(name)
    driver.get_screenshot_as_file(os.path.join(screen_path(), _name + '-' + now + ".png"))

 