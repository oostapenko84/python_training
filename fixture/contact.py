__author__ = 'olga.ostapenko'

from model.contact import Contact

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.First_Name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.Middle_Name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.Last_Name)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.Company_Name)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.Address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.Home_Phone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.Mobile_Phone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.Work_Phone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.Email)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.Homepage)
        wd.find_element_by_name("theform").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[32]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[32]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[13]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[13]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.Birthday)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[24]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[24]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[9]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[9]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.Anniversary)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.Secondary_Address)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.open_home_page()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # edit first contact
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.First_Name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.Middle_Name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.Last_Name)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.Company_Name)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.Address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.Home_Phone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.Mobile_Phone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.Work_Phone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.Email)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.Homepage)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[32]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[32]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[13]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[13]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.Birthday)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[24]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[24]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[9]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[9]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.Anniversary)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.Secondary_Address)
        # submit edition
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        # go to home page
        self.app.open_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.app.open_home_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            text = element.find_element_by_name
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(name=text, id=id))
        return contacts
        # return [Group(name=e.text, id=e.id) for e in wd.find_elements_by_css_selector('span.group') ]