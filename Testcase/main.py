from pip import main
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import page

class TestRegisterForm(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome("/Users/oyls/chromedriver")
        self.browser.get("http://localhost:3000/register")

    def test_register_page(self):
        
        mainPage = page.MainPage(self.browser)
        print("-------------------------------")
        print("|NO |       CASE       |RESULT|")
        print("-------------------------------")
        
        # 1
        try:
            assert mainPage.title_matches()
            assert mainPage.header_matches()
            assert mainPage.name_matches()
            assert mainPage.gender_matches()
            assert mainPage.age_matches()
            assert mainPage.dob_matches()
            assert mainPage.phone_matches()
            assert mainPage.email_matches()
            assert mainPage.submit_matches()
            print("|1  |Testcase_01       | PASS |")
            print("-------------------------------")
        except AssertionError:
            print("|1  |Testcase_01       | FAIL |")
            print("-------------------------------")

        # 2
        try:
            assert mainPage.option_matches()
            print("|2  |Testcase_02       | PASS |")
            print("-------------------------------")
        except AssertionError:
            print("|2  |Testcase_02       | FAIL |")
            print("-------------------------------")

        # 3
        try:
            mainPage.type_name()
            mainPage.type_age()
            mainPage.type_date()
            mainPage.type_phone()
            mainPage.type_mail()
            mainPage.click_submit()
            mainPage.error_matches()
            print("|3  |Testcase_03       | FAIL |")
            print("-------------------------------")
        except :
            print("|3  |Testcase_03       | PASS |")
            print("-------------------------------")

        # 4
        try:
            self.browser.find_element(By. NAME, "input_name").clear()
            mainPage.type_name_number()
            mainPage.click_submit()
            mainPage.error_matches()
            print("|4  |Testcase_04       | PASS |")
            print("-------------------------------")
        except :
            print("|4  |Testcase_04       | FAIL |")
            print("-------------------------------")

        # 5
        try:
            self.browser.find_element(By. NAME, "input_name").clear()
            mainPage.type_name_symbol()
            mainPage.click_submit()
            mainPage.error_matches()
            print("|5  |Testcase_05       | PASS |")
            print("-------------------------------")
        except :
            print("|5  |Testcase_05       | FAIL |")
            print("-------------------------------")

        self.browser.find_element(By. NAME, "input_name").clear()
        mainPage.type_name()

        # 6
        try:
            self.browser.find_element(By. NAME, "input_age").clear()
            mainPage.type_underage()
            mainPage.click_submit()
            mainPage.error_matches()
            print("|6  |Testcase_06       | PASS |")
            print("-------------------------------")
        except :
            print("|6  |Testcase_06       | FAIL |")
            print("-------------------------------")

        # 7
        try:
            self.browser.find_element(By. NAME, "input_age").clear()
            mainPage.type_overage()
            mainPage.click_submit()
            mainPage.error_matches()
            print("|7  |Testcase_07       | PASS |")
            print("-------------------------------")
        except :
            print("|7  |Testcase_07       | FAIL |")
            print("-------------------------------")

        # 8
        try:
            self.browser.find_element(By. NAME, "input_age").clear()
            mainPage.type_age_text()
            mainPage.click_submit()
            mainPage.error_matches()
            print("|8  |Testcase_08       | PASS |")
            print("-------------------------------")
        except :
            print("|8  |Testcase_08       | FAIL |")
            print("-------------------------------")

        self.browser.find_element(By. NAME, "input_age").clear()
        mainPage.type_age()

        # 9
        try:
            self.browser.find_element(By. NAME, "input_date").clear()
            mainPage.type_date_false()
            mainPage.click_submit()
            mainPage.error_matches()
            print("|9  |Testcase_09       | PASS |")
            print("-------------------------------")
        except :
            print("|9  |Testcase_09       | FAIL |")
            print("-------------------------------")

        self.browser.find_element(By. NAME, "input_date").clear()
        mainPage.type_date()

        # 10
        try:
            self.browser.find_element(By. NAME, "input_phone").clear()
            mainPage.type_phone_false()
            mainPage.click_submit()
            mainPage.error_matches()
            print("|10 |Testcase_10       | PASS |")
            print("-------------------------------")
        except :
            print("|10 |Testcase_10       | FAIL |")
            print("-------------------------------")
        
        # 11
        try:
            self.browser.find_element(By. NAME, "input_phone").clear()
            mainPage.type_phone_text()
            mainPage.click_submit()
            mainPage.error_matches()
            print("|11  |Testcase_11      | PASS |")
            print("-------------------------------")
        except :
            print("|11  |Testcase_11      | FAIL |")
            print("-------------------------------")
        
        self.browser.find_element(By. NAME, "input_phone").clear()
        mainPage.type_phone()

        # 12
        try:
            self.browser.find_element(By. NAME, "input_mail").clear()
            mainPage.type_mail_false()
            mainPage.click_submit()
            mainPage.error_matches()
            print("|12  |Testcase_12      | PASS |")
            print("-------------------------------")
        except :
            print("|12  |Testcase_12      | FAIL |")
            print("-------------------------------")

        self.browser.find_element(By. NAME, "input_mail").clear()
        mainPage.type_mail()

        # 13
        try :
            mainPage.dropdown()
            mainPage.click_submit()
            mainPage.alert_success()
            print("|13  |Testcase_13      | PASS |")
            print("-------------------------------")
        except :
            print("|13  |Testcase_13      | FAIL |")
            print("-------------------------------")

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()