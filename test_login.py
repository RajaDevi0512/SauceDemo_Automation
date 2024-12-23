from Utilities.SauceDemo_automation import Saucedemo

import os

#To test the whether webpage URL is coorrect or not
def test_urlCheck(): #test 1
    assert Saucedemo().url_check() == 'https://www.saucedemo.com/'
    print("Test Passed, Url Verified")

# To test the login using cookie
def test_loginCheck_cookie(): #test 2
    assert Saucedemo().login_check_with_cookie() == 'www.saucedemo.com'
    print("Test Passed! Cookie verified")

#To test the visibility og the logout icon
def test_logoutVisibility():  #test 3
    assert Saucedemo().logoutButton_visibility() == "Logout"
    print("Test Passed, Logout visibility checked")

#To test the visibility of the cart icon
def test_cart_visibility(): #test 4
    assert Saucedemo().cart_visibility() == True
    print("Test Passed, cart visibility checked")

#To test whether 4 products are added to the cart. 
def test_adding_product(): #test 5
    assert Saucedemo().Adding_products() == 4
    print("Test passed, 4 products added to the cart successfully")
    
# Fetching the product name and comapring it with the dashboard list 
def test_check_products_in_cart(): #test 6
    All_products = Saucedemo().fetching_product_Name()
    product_in_cart = Saucedemo().fetching_product_Name_from_cart()

    is_subset = all(item in All_products for item in product_in_cart) # Checks whether products in the cart is the sub set of main product list

    if is_subset is True: print("Test Passed, products in cart is checked")
    else: print("TEst Failed, no items in cart")
    # Saucedemo().checkout()

# To test whether screenshot is present in the folder or not 
def test_checkout_screenshot(): #test 7
       
    # Call the checkout method and get the screenshot file path
    screenshot_path = Saucedemo().checkout()
    
    # Assert if the screenshot file exists at the specified path
    assert os.path.exists(screenshot_path), "Test Failed, No screenshot saved"
    
    # Optionally, print the screenshot path for verification
    print("Test Passed, Screenshot saved")

#To test whether logout functionality is working or not 

def test_logout_functionality(): #test 8
    assert Saucedemo().Logout_Functionality() == "https://www.saucedemo.com/"
    print("Test Passed, logout Functionality checked")
    

# To test whether login with credentials in excel using DDT framework
def test_LoginwithExcel(): #test 9
    assert Saucedemo().loginExcel() == 'Printed'
    print("Test Passed, Login Verified")

# Finally shutdown
def test_shutdown(): #test 10
    assert Saucedemo().shutdown() == True
    print("Test Passed! Automation completed")

