class login:
    def __init__(self, page):
        self.page=page

    def navigation(self):
        self.page.goto("https://rahulshettyacademy.com/client/#/auth/login")

    def enter_username(self,username,password):
        self.page.locator("#userEmail").fill(username)
        self.page.locator("#userPassword").fill(password)
        #karthi1412@gmail.com
        #KARTHIKAEYANr@14
    def login_click(self):
        self.page.locator("#login").click()
    
    def error(self):
        return self.page.locator("div[aria-label='Incorrect email or password.']")

    def email_requried(self):
        return self.page.locator("//div[text()='*Email is required']")

    def password_required(self):
        return self.page.locator("//div[text()='*Password is required']")

    def valid_email(self):
        return self.page.locator("//div[text()='*Enter Valid Email']")