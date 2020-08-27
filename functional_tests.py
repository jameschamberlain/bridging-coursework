from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

from django.test import Client

import unittest
import time

class EditCVTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_update_cv(self):
        # James has decided to update his cv on his website. He goes
        # to the website admin page and then visits the homepage
        self.browser.get('http://127.0.0.1:8000/admin/')
        username_input_box = self.browser.find_element_by_name('username')
        username_input_box.send_keys('james')
        password_input_box = self.browser.find_element_by_name('password')
        password_input_box.send_keys('tottenham99')
        password_input_box.send_keys(Keys.ENTER)
        time.sleep(3)

        self.browser.get('http://127.0.0.1:8000')

        # He notices the page title and header mention his name
        self.assertIn('James', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('james', header_text)

        # He sees a button to go to the cv page and clicks it
        self.assertIn('CV', [btn.text for btn in self.browser.find_elements_by_class_name('btn')])
        cv_button = self.browser.find_element_by_link_text('CV')
        ActionChains(self.browser).click(cv_button).perform()
        time.sleep(2)
        self.assertEqual(self.browser.current_url, "http://127.0.0.1:8000/cv/")

        # He can see that cv is in the title of the page
        self.assertIn('CV', self.browser.title)

        # He notices the navigation bar at the top and that the cv heading is selected
        nav_buttons = self.browser.find_elements_by_class_name('nav')
        self.assertEqual(len(nav_buttons), 3)
        selected_nav_button = self.browser.find_element_by_class_name('selected')
        self.assertEqual(selected_nav_button.text, 'CV')

        # He can see all the sections of his cv including his work experience,
        # education, projects, and skills
        work_experience_header_text = self.browser.find_element_by_id('work-experience').text
        self.assertEqual(work_experience_header_text, "Work Experience")
        work_experience_header_text = self.browser.find_element_by_id('education').text
        self.assertEqual(work_experience_header_text, "Education")
        work_experience_header_text = self.browser.find_element_by_id('projects').text
        self.assertEqual(work_experience_header_text, "Projects")
        work_experience_header_text = self.browser.find_element_by_id('skills').text
        self.assertEqual(work_experience_header_text, "Skills")

        # He decides to add a new project and clicks the button next to the projects section
        add_work_experience_btn = self.browser.find_element_by_id('add-project')
        ActionChains(self.browser).click(add_work_experience_btn).perform()
        time.sleep(2)

        # He adds a project title: "Portfolio website"
        self.fail('Finish the test!')

        # He adds a description: "Portfolio website created using Django."

        # When he hits the 'add' button, the page updates, and now the new project can be seen
        # in the projects section

        # James is satisfied and closes his browser window

if __name__ == '__main__':
    unittest.main()