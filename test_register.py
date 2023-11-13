from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from PageObjects.RegisterPage import RegisterPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_register(self):
        log = self.getLogger()
        self.driver.implicitly_wait(5)
        registerPage = RegisterPage(self.driver)
        registerPage.Registering().click()
        log.info("Getting corporate types")
        registerPage.getType().click()
        log.info("Entering firstname")
        button1 = registerPage.getFirstName()
        ActionChains(self.driver).move_to_element(button1).click(button1).perform()
        ActionChains(self.driver).move_to_element(button1).send_keys("testing").perform()
        log.info("Entering lastname")
        button2 = registerPage.getLastName()
        ActionChains(self.driver).move_to_element(button2).click(button2).perform()
        ActionChains(self.driver).move_to_element(button2).send_keys("testing").perform()
        log.info("Entering email")
        button3 = registerPage.getEmail()
        ActionChains(self.driver).move_to_element(button3).click(button3).perform()
        ActionChains(self.driver).move_to_element(button3).send_keys("testing@gmail.com").perform()
        log.info("getCheckbox")
        registerPage.getCheckbox().click()
        log.info("submission")
        registerPage.getSubmit().click()
        log.info("Print text")
        textMatch = self.driver.find_element(By.XPATH, "//div[@class='_2ntGtJxR']").text
        assert ("We've sent you an email with the next steps." in textMatch)
        print(textMatch)