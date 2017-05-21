from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_tiems(self):
        # Billy goes to the home page and accidentally tries to submit
        # an empty list item. SHe hits Enter on the empty input box

        # The home page refreshes, and there is an eror message
        # saying that list items cannot be blank

        # She tries again with some text for the item, which works now

        # Perversely, she decides to submit a second blank list item

        # She recieves a similar warning on the list page

        # And she can correct it by filling some text in
        self.fail('write me!')
