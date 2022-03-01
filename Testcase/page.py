from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class BasePage(object):

    def __init__(self, driver):
        self.browser = driver

class MainPage(BasePage):

#  verify

    def title_matches(self):
        return "Register" == self.browser.title

    def header_matches(self):
        register = self.browser.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/legend').text
        return register == "Register"
        
    def name_matches(self):
        fullname = self.browser.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/label').text
        return fullname == "Full name :"

    def gender_matches(self):
        gender = self.browser.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/label').text
        return gender == "Gender :"

    def option_matches(self):
        gender = ["Choose Gender", "Female", "Male", "Other"]
        i = self.browser.find_elements(By.CLASS_NAME, 'gender_list')
        match = 0
        for j in i:
            p = j.text
            split = p.split("\n")
        for list in split:
            for option in gender:
                if list == option:
                    match+=1
                    if match == 4:
                        return True

    def age_matches(self):
        age = self.browser.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/label').text
        return age == "Age :"

    def dob_matches(self):
        dob = self.browser.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/label').text
        return dob == "Date of Birth :"

    def phone_matches(self):
        phone = self.browser.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[5]/label').text
        return phone == "Phone No. :"

    def email_matches(self):
        email = self.browser.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[6]/label').text
        return email == "Email :"

    def submit_matches(self):
        submit = self.browser.find_element(By.XPATH, '//*[@id="submit"]').text
        return submit == "Submit"

# True

    def type_name(self): 
        self.browser.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/input').send_keys("John John")

    def type_age(self):
        self.browser.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/input').send_keys("23")

    def type_phone(self):
        self.browser.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[5]/input').send_keys("012-3456789")

    def type_mail(self):
        self.browser.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[6]/input').send_keys("john@gmail.com")

    def type_date(self):
        date = self.browser.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/input')
        date.send_keys("20/04/1998")

# False

    # name
    def type_name_number(self): 
        self.browser.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/input').send_keys("John 345")

    def type_name_symbol(self): 
        self.browser.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/input').send_keys("John *=/")

    # age
    def type_underage(self): 
        self.browser.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/input').send_keys("5")

    def type_overage(self): 
        self.browser.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/input').send_keys("51")

    def type_age_text(self): 
        self.browser.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/input').send_keys("ab")

    # phone
    def type_phone_false(self): 
        self.browser.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[5]/input').send_keys("0123456789")

    def type_phone_text(self): 
        self.browser.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[5]/input').send_keys("abcdefg")

    #  mail
    def type_mail_false(self): 
        self.browser.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[6]/input').send_keys("john==@gmail.com")

    # date
    def type_date_false(self): 
        date = self.browser.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/input')
        date.send_keys("20/04/1999")

    def dropdown(self):
        dropdown = Select(self.browser.find_element(By.CLASS_NAME, "gender_list"))
        dropdown.select_by_visible_text('Female')
        dropdown.select_by_visible_text('Male')
        dropdown.select_by_visible_text('Other')

    def alert_success(self):
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        alert.accept()
        if alert_text == "Register Successfully":
            return True

    def alert_fail(self):
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        alert.accept()
        if alert_text == "Failed Register":
            return True

    def error_matches(self):
        error = self.browser.find_element(By.CLASS_NAME, 'error')
        error_text = error
        if (error_text == "*Wrong Name" or error_text == "*Enter fullname" 
        or error_text == "*Wrong Age" or error_text == "*Overage" or error_text == "*Underage" 
        or error_text == "*Enter age" or error_text == "*Date of Birth not related to age" 
        or error_text == "*Enter Date of Birth" or error_text == "*Wrong Phone no." 
        or error_text == "*Enter Phone no." or error_text == "*Enter your email address in format email@xxx.xxx" 
        or error_text == "*Enter Email") :
            return True

    def click_submit(self):
        element = self.browser.find_element(By.XPATH, '//*[@id="submit"]')
        element.click()
