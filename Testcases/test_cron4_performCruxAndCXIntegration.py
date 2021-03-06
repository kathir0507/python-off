from inspect import stack
import os

import pytest
import FunctionLibrary.CommonFunctions.Commonfunctions as common 
import FunctionLibrary.CustomFunctions.performCruxCxRestIntegration as custom

Root= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@pytest.mark.Regression
def test_Cron4_CruxCxRestIntegration_cron4(driver):
    
    value=custom.customTestFunctions(driver)
       
    if value:
        print stack()[0][3]+ " Test Case Passed "

    else:
        print("Assertion Error Occurred in following test case -> "+stack()[0][3])
        common.screenshotsOnFailure(stack()[0][3],driver,Root)
#             fail("Assertion Error Occurred in following test case -> "+stack()[0][3])