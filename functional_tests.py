from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Billy heard about an awesome new online to-do app that's super handy.
        # He goes to check it out.
        self.browser.get('http://localhost:8000')

        # Billy notices the page title and the header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # He types "Clean out the car" into the text box
        # ( He's been dreading it for days )
        inputbox.send_keys('Clean out the car')

        # When he hits enter, the page updates, and now the page lists
        # "1: Clean out the car" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Clean out the car', [row.text for row in rows])

        # There is still a text box inviting her to add another item. He enters
        # "Clean my computer" ( as it desperately needs a cleaning )
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Clean my computer')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows both items on his list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Clean out the car', [row.text for row in rows])
        self.assertIn('2: Clean my computer', [row.text for row in rows])

        # Billy wonders whether the site will remember his list. Then he sees
        # that the site has generated a unique URL for her -- there is text explaining it
        self.fail('Finish the test!')

        # He visits that URL - and huzzah his list is still there

        # Now satisfied, he returns to finishing lunc

if __name__ == '__main__':
    unittest.main(warnings='ignore')