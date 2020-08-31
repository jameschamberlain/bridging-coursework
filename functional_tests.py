from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

from django.test import Client

import unittest
import time

class CVTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def login(self):
        self.browser.get('http://127.0.0.1:8000/admin/')
        username_input_box = self.browser.find_element_by_name('username')
        username_input_box.send_keys('james')
        password_input_box = self.browser.find_element_by_name('password')
        password_input_box.send_keys('tottenham99')
        password_input_box.send_keys(Keys.ENTER)
        time.sleep(3)

    def test_cv_layout_and_styling(self):
        # James has decided to view his cv on his website. He goes
        # to the website admin page and then visits the homepage
        self.login()
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
        nav_buttons = self.browser.find_elements_by_class_name('nav-bar')
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


    def test_can_update_work_experience_on_cv(self):
        # James has decided to update his work experiences on his cv on his website. He goes
        # to the website admin page and then visits his cv
        self.login()
        self.browser.get('http://127.0.0.1:8000/cv/')
        self.assertEqual(self.browser.current_url, "http://127.0.0.1:8000/cv/")

        # He decides to add a new work experience and clicks the button next to the work experience section
        add_work_experience_button = self.browser.find_element_by_id('add-work-experience')
        self.browser.execute_script("arguments[0].scrollIntoView();", add_work_experience_button)
        time.sleep(1)
        ActionChains(self.browser).click(add_work_experience_button).perform()
        time.sleep(2)
        self.assertEqual(self.browser.current_url, "http://127.0.0.1:8000/cv/new-work-experience")

        # He adds a company role: "Test developer"
        role_inputbox = self.browser.find_element_by_id('id_role')
        role_inputbox.send_keys('Test developer')

        # He adds a company name: "Tests R Us"
        name_inputbox = self.browser.find_element_by_id('id_company')
        name_inputbox.send_keys('Tests R Us')
        
        # He adds a description: "Test description for my test work at Tests R Us."
        description_inputbox = self.browser.find_element_by_id('id_description')
        description_inputbox.send_keys('Test description for my test work at Tests R Us.')

        # When he hits the 'add' button, the page updates, and now the new project can be seen
        # in the projects section
        save_button = self.browser.find_element_by_class_name('save')
        ActionChains(self.browser).click(save_button).perform()
        time.sleep(2)

        # He can see his new project on his CV
        heading_elements = self.browser.find_elements_by_tag_name('h5')
        self.assertIn('Test developer', [element.text for element in heading_elements])
        
        small_heading_elements = self.browser.find_elements_by_tag_name('h6')
        self.assertIn('Tests R Us', [element.text for element in small_heading_elements])

        text_elements = self.browser.find_elements_by_tag_name('p')
        self.assertIn('Test description for my test work at Tests R Us.', [element.text for element in text_elements])


    def test_can_update_education_on_cv(self):
        # James has decided to update his education on his cv on his website. He goes
        # to the website admin page and then visits his cv
        self.login()
        self.browser.get('http://127.0.0.1:8000/cv/')
        self.assertEqual(self.browser.current_url, "http://127.0.0.1:8000/cv/")

        # He decides to add a new education and clicks the button next to the education section
        add_education_button = self.browser.find_element_by_id('add-education')
        self.browser.execute_script("arguments[0].scrollIntoView();", add_education_button)
        time.sleep(1)
        ActionChains(self.browser).click(add_education_button).perform()
        time.sleep(2)
        self.assertEqual(self.browser.current_url, "http://127.0.0.1:8000/cv/new-education")

        # He adds an institution name: "Test University"
        institution_inputbox = self.browser.find_element_by_id('id_institution')
        institution_inputbox.send_keys('Test University')

        # He adds a description: "Testing is fun at Test University."
        description_inputbox = self.browser.find_element_by_id('id_description')
        description_inputbox.send_keys('Testing is fun at Test University.')

        # When he hits the 'add' button, the page updates, and now the new education can be seen
        # in the education section
        save_button = self.browser.find_element_by_class_name('save')
        ActionChains(self.browser).click(save_button).perform()
        time.sleep(2)

        # He can see his new education on his CV
        heading_elements = self.browser.find_elements_by_tag_name('h5')
        self.assertIn('Test University', [element.text for element in heading_elements])

        text_elements = self.browser.find_elements_by_tag_name('p')
        self.assertIn('Testing is fun at Test University.', [element.text for element in text_elements])


    def test_can_update_projects_on_cv(self):
        # James has decided to update his projects on his cv on his website. He goes
        # to the website admin page and then visits his cv
        self.login()
        self.browser.get('http://127.0.0.1:8000/cv/')
        self.assertEqual(self.browser.current_url, "http://127.0.0.1:8000/cv/")

        # He decides to add a new project and clicks the button next to the projects section
        add_project_button = self.browser.find_element_by_id('add-project')
        self.browser.execute_script("arguments[0].scrollIntoView();", add_project_button)
        time.sleep(1)
        ActionChains(self.browser).click(add_project_button).perform()
        time.sleep(2)
        self.assertEqual(self.browser.current_url, "http://127.0.0.1:8000/cv/new-project")

        # He adds a project name: "Portfolio website"
        name_inputbox = self.browser.find_element_by_id('id_name')
        name_inputbox.send_keys('Test project')

        # He adds a description: "Portfolio website created using Django."
        description_inputbox = self.browser.find_element_by_id('id_description')
        description_inputbox.send_keys('Test description for the test project.')

        # When he hits the 'add' button, the page updates, and now the new project can be seen
        # in the projects section
        save_button = self.browser.find_element_by_class_name('save')
        ActionChains(self.browser).click(save_button).perform()
        time.sleep(2)

        # He can see his new project on his CV
        heading_elements = self.browser.find_elements_by_tag_name('h5')
        self.assertIn('Test project', [element.text for element in heading_elements])

        text_elements = self.browser.find_elements_by_tag_name('p')
        self.assertIn('Test description for the test project.', [element.text for element in text_elements])


    def test_can_update_skills_on_cv(self):
        # James has decided to update his skills on his cv on his website. He goes
        # to the website admin page and then visits his cv
        self.login()
        self.browser.get('http://127.0.0.1:8000/cv/')
        self.assertEqual(self.browser.current_url, "http://127.0.0.1:8000/cv/")

        # He decides to add a new skill and clicks the button next to the skills section
        add_skill_button = self.browser.find_element_by_id('add-skill')
        self.browser.execute_script("arguments[0].scrollIntoView();", add_skill_button)
        time.sleep(1)
        ActionChains(self.browser).click(add_skill_button).perform()
        time.sleep(2)
        self.assertEqual(self.browser.current_url, "http://127.0.0.1:8000/cv/new-skill")

        # He adds a skill name: "Testing"
        name_inputbox = self.browser.find_element_by_id('id_name')
        name_inputbox.send_keys('Testing')

        # When he hits the 'add' button, the page updates, and now the new skill can be seen
        # in the skills section
        save_button = self.browser.find_element_by_class_name('save')
        ActionChains(self.browser).click(save_button).perform()
        time.sleep(2)

        # He can see his new skill on his CV
        heading_elements = self.browser.find_elements_by_tag_name('h5')
        self.assertIn('Testing', [element.text for element in heading_elements])


if __name__ == '__main__':
    unittest.main()