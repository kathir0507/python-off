from inspect import stack
import os
import sys
import unittest

import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

import FunctionLibrary.CommonFunctions.Commonfunctions as common 
import FunctionLibrary.CustomFunctions.performCruxCxRestIntegration as custom


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



Root= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print Root

def test_Cron4_CruxCxRestIntegration_cron4(driver):

        
        value=custom.CustomTestFunctions(driver)
       
        if value:
            print stack()[0][3]+ " Test Case Passed "

        else:
            print("Assertion Error Occurred in following test case -> "+stack()[0][3])
            common.screenshotsOnFailure(stack()[0][3],driver,Root)
#             fail("Assertion Error Occurred in following test case -> "+stack()[0][3])

#     except NoSuchElementException as e:
#         common.screenshotsOnFailure(stack()[0][3], driver, Root)
# #         fail(stack()[0][3]+"TestCase Failed due to Element Not Found")
# 
#     except TimeoutException as e:
#         common.screenshotsOnFailure(stack()[0][3], driver, Root)
# #         fail(stack()[0][3]+"TestCase Failed due to Timeout")

#     except Exception as e:
#         common.screenshotsOnFailure(stack()[0][3], driver, Root)
# #         fail(stack()[0][3]+"TestCase Failed due to an Error or Exception")

