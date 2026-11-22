from playwright.sync_api import expect,Page

class Screen:
    def __init__(self,page):
        self.page=page

    def search_product(self,enter_product):
        search_box=self.page.locator("//div[@class='py-2 border-bottom ml-3']//input[@placeholder='search']")
        search_box.fill(enter_product)
        #search_box.fill()
        search_box.press("Enter")


    def valid_product(self):
        return self.page.locator("//div[@class='card'] //b").all_text_contents()

    def no_product(self):
        return self.page.locator("//div[@aria-label='No Products Found']")

    def price_range(self,min_price,max_price):
        enter_price_1=self.page.locator("(//input[@placeholder='Min Price'])[2]")
        enter_price_1.fill(min_price)
        enter_price_1.press('Enter')
        enter_price_2=self.page.locator("(//input[@placeholder='Max Price'])[2]")
        enter_price_2.fill(max_price)
        enter_price_2.press('Enter')
