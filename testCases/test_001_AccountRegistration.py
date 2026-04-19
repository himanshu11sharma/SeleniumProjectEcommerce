import os
import time

import pytest

from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomString
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_001_AccountReg:
    baseURL = ReadConfig.getApplicationURL()    #or https://tutorialsninja.com/demo/
    logger=LogGen.loggen()  # for logging
    @pytest.mark.sanity
    def test_account_reg(self, setup):
        self.logger.info("*******test_001_AccountRegistration started*****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Launching application")
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.logger.info("clicking on MyAccount--> register")
        self.hp.clickMyAccount()
        self.hp.clickRegister()
        self.logger.info("Proving customer details for registration")
        self.regpage = AccountRegistrationPage(self.driver)

        self.regpage.setFirstName("John")
        self.regpage.setLastName("Canedy")
        self.email = randomString.random_string_generator() + '@gmail.com'
        # self.regpage.setEmail("abcxyz76iii810@gmail.com")
        self.regpage.setEmail(self.email)
        time.sleep(4)
        self.regpage.setTelephone("65656565")
        self.regpage.setPassword("abcxyz")
        self.regpage.setConfirmPassword("abcxyz")
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        self.confmsg = self.regpage.getconfirmationmsg()

        if self.confmsg == "Your Account Has Been Created!":
            self.logger.info("Account registration is passed..")
            assert True

        else:
            # self.driver.save_screenshot("C:\\Users\\LENOVO\\PycharmProjects\\OpencartV1\\screenshots\\test_account_reg.png")
            self.driver.save_screenshot("..\\screenshots\\" + "test_account_reg1.png")
            self.logger.error("Account registration is failed.")
            assert False
        self.logger.info("****** test_001_AccountRegistration finished*******")



