from selenium import webdriver
from selenium.webdriver import ActionChains

import unittest
import time

class CVTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_update_cv(self):
        # James has decided to update his cv on his website. He goes
        # to the website homepage
        self.browser.get('http://127.0.0.1:8000')

        # He notices the page title and header mention his name
        self.assertIn('James', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('james', header_text)

        # He sees a button to go to the cv page and clicks it
        self.assertIn('CV', [btn.text for btn in self.browser.find_elements_by_class_name('btn')])
        cv_button = self.browser.find_element_by_link_text('CV')
        ActionChains(self.browser).click(cv_button).perform()
        time.sleep(1)
        self.assertEqual(self.browser.current_url, "http://127.0.0.1:8000/cv")

        # He can see all the sections of his cv including his work experience,
        # education, projects, and skills
        self.fail('Finish the test!')

        # He decides to add a new project and clicks the edit button next to the projects section

        # He adds a project title: "Portfolio website"

        # He adds a description: "Portfolio website created using Django."

        # When he hits the 'add' button, the page updates, and now the new project can be seen
        # in the projects section

        # James is satisfied and closes his browser window

if __name__ == '__main__':
    unittest.main()