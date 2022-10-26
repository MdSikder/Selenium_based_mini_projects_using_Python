from selenium.webdriver.common.by import By


class Locator(object):
    # home page locator

    # id
    UserNameBar = "inputUsername"
    # name
    PasswordBar = "inputPassword"

    # className
    signinButton = "signInBtn"

    # linkText
    ForgotYourPassword = "Forgot your password?"

    """************************************* Forgot password ****************************"""
    # By xpath
    NameBar = "//input[@placeholder='Name']"
    # By xpath
    EmailBar = "//input[@placeholder='Email']"

    # By CssSelector
    PhoneNumberBar = "input[placeholder='Phone Number']"

    # By CssSelector
    ResetButton = ".reset-pwd-btn"

    # By cssSelector
    PickPass = ".error"

    # CssSelector
    GoToLoginButton = ".go-to-login-btn"