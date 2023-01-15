from nturl2path import url2pathname
from selenium import webdriver

# for finding elements with By.ID, ...
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

import time

# for the dropdown
from selenium.webdriver.support.ui import Select


def SetUp():
    global driver, url, uname, pw

    driver = webdriver.Chrome()

    uname = "henryvangard"
    pw = "xxxxxxx"

    url = 'https://www.cdw.com/accountcenter/LogOn?target=%2F'

    # This is very important to allow for certain features to finish loading.
    driver.implicitly_wait(30)


def LogIn():
    driver.get(url)
    driver.find_element(By.ID, 'UserName').send_keys(uname)
    driver.find_element('id', 'UserPassword').send_keys(pw)
    driver.find_element('id', 'LogOnButton').click()
    driver.maximize_window()


# clear the cart first
def ClearCart():
    pass


def SearchItem(item):
    # clear the search field first
    searchField = driver.find_element(By.ID, 'search-input')
    searchField.clear()
    # search for hp products
    searchField.send_keys(item)
    # press Enter to search
    driver.find_element(By.ID, 'gh-header-button-search').send_keys(Keys.ENTER)


def AddToCart():
    # add to cart
    driver.find_element('id', 'AddItemToCartStickyHeader').click()


def Checkout():
    # click on Checkout button
    driver.find_element('id', 'expressCheckout').click()

    # fill out the New shipping address
    fn = 'Bob'
    ln = 'Yang'
    co = None
    address = '123 4th St'
    city = 'Minneapolis'
    state = 'MN'
    zipcode = 55106
    phone = '651-333-4455'

    co = 'Bob\'s, Inc.'

    driver.find_element(
        By.ID, 'ShippingAddressEditor_AttentionFirstName').send_keys(fn)

    driver.find_element(
        By.ID, 'ShippingAddressEditor_AttentionLastName').send_keys(ln)
    if co is not None:  # co for company is NOT None
        driver.find_element(
            By.ID, 'ShippingAddressEditor_CompanyName').send_keys(co)
    driver.find_element(
        By.ID, 'ShippingAddressEditor_Address1').send_keys(address)
    driver.find_element(By.ID, 'ShippingAddressEditor_City').send_keys(city)
    driver.find_element(
        By.ID, 'ShippingAddressEditor_ZipOrPostalCode').send_keys(zipcode)
    driver.find_element(
        By.ID, 'ShippingAddressEditor_Phone').send_keys(phone)

    # drop select the state
    dropState = Select(driver.find_element_by_id(
        'ShippingAddressEditor_StateOrProvince'))
    dropState.select_by_value('MN')


def Continue():
    # click Continue
    driver.find_element(
        # By.XPATH, '/html/body/main/div/div/form/div/section[2]/div/input').click()
        By.XPATH, '//*[@id="shipping-address-form"]/div/section[2]/div/input').click()


def VerifyAddress():
    driver.implicitly_wait(5)

    # click Continue to verify address
    driver.find_element(By.XPATH, '//*[@id=\"continueWithAddress\"]').click()


def ConfirmAddress():
    driver.implicitly_wait(5)

    # click Continue to confirm address then provide payment information
    driver.find_element(
        By.XPATH, '//*[@id="shipping-address-form"]/div/section[2]/div/input').click()


def SendEmail():
    pass


# close the browser
def Exit():
    driver.close()


########################################################################
# Main
########################################################################


SetUp()
LogIn()
ClearCart()

item1 = 6914736
SearchItem(item1)
AddToCart()

item2 = 7015784
SearchItem(item2)
AddToCart()

item3 = 7193191
SearchItem(item3)
AddToCart()

# click on Checkout button
Checkout()

# click on the Continue button
Continue()

# verify shipping address
VerifyAddress()

# final Continue after verifying the shipping address
ConfirmAddress()

# send an email notification to the customer
SendEmail()

# exit the application by closing the browser
Close()
