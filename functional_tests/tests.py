from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10


class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_for_one_user(self):
        # Billy heard about an awesome new online to-do app that's super handy.
        # He goes to check it out.
        self.browser.get(self.live_server_url)

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
        self.wait_for_row_in_list_table('1: Clean out the car')

        # There is still a text box inviting her to add another item. He enters
        # "Clean my computer" ( as it desperately needs a cleaning )
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Clean my computer')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on his list
        self.wait_for_row_in_list_table('1: Clean out the car')
        self.wait_for_row_in_list_table('2: Clean my computer')

        # Billy wonders whether the site will remember his list. Then he sees
        # that the site has generated a unique URL for her -- there is text explaining it


        # He visits that URL - and huzzah his list is still there

        # Now satisfied, he returns to finishing lunc

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Billy starts a new todo list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Clean out the car')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Clean out the car')

        # He notices that his list has a unique URL
        billy_list_url = self.browser.current_url
        self.assertRegex(billy_list_url, '/lists/.+')

        # Now a new user, Francine, visits the site.the

        ## We use a new browser session to make sure no information of
        ## Billy's is coming through from cookies etc.
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francine visits the home page. There is no sign of Billy's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Clean out the car', page_text)
        self.assertNotIn('Clean out my computer', page_text)

        # Francine starts a new list by entering a new item. He is more exciting than Billy
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Set up sky diving')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Set up sky diving')

        # Francine gets his own unique URL
        francine_list_url = self.browser.current_url
        self.assertRegex(francine_list_url, '/lists/.+')
        self.assertNotEqual(francine_list_url, billy_list_url)

        # Again, there is still no trace of Billy's boring list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Clean out the car', page_text)
        self.assertIn('Set up sky diving', page_text)

        # Satisfied they both go about their days

    def test_layout_and_styling(self):
        # Billy goes to the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # He notices the input box nicely centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )

        # He starts a new list and sees the input is nicely
        # centered there too
        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: testing')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] /2,
            512,
            delta=10
        )

