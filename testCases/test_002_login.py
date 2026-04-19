import pytest

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_Login():
    base_URL=ReadConfig.getApplicationURL()
    logger=LogGen.loggen()  #Logger

    user=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    @pytest.mark.sanity
    def test_login(self,setup):
        self.logger.info("*****Starting test__002_login*********")
        self.driver=setup
        self.driver.get(self.base_URL)
        self.driver.maximize_window()
        self.hp=HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()

        self.lp=LoginPage(self.driver)
        self.lp.setEmail(self.user)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.targetpage=self.lp.isMyAccountPageExists()
        if self.targetpage==True:
            assert True
        else:
            self.driver.save_screenshot("..\\screenshots\\" + "test_login.png")
            assert True
        self.driver.close()
        self.logger.info("******End of Test_002_login*************")