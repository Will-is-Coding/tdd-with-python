from selenium import webdriver
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
        self.fail('Finish the test!')

        # He is invited to enter a to-do item straight away

        # He types "Clean out the car" into the text box
        # ( He's been dreading it for days )

        # When he hits enter, the page updates, and now the page lists
        # "1: Clean out the car" as an item in a to-do list

        # There is still a text box inviting her to add another item. He enters
        # "Clean my computer" ( as it desperately needs a cleaning )

        # The page updates again, and now shows both items on his list

        # Billy wonders whether the site will remember his list. Then he sees
        # that the site has generated a unique URL for her -- there is text explaining it

        # He visits that URL - and huzzah his list is still there

        # Now satisfied, he returns to finishing lunc

if __name__ == '__main__':
    unittest.main(warnings='ignore')