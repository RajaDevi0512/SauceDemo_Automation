"""
This file contains locator that are used in automation
"""

class SauceDemo_Locator:
    username_locator = "user-name" # ID
    password_locator = "password" # ID
    login_locator = 'login-button' #ID
    profile_icon_locator = 'react-burger-menu-btn' #ID
    logout_locator =  'logout_sidebar_link'  #ID

    dashboard_item_locator = "//div[@class='oxd-sidepanel-body']//li[a][1]"