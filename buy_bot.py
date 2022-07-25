#Note, this bot requires selenium, beautifulsoup4, and pandas to be installed
#Also requires proper chromedriver for compatibility

from selenium import webdriver as wd
import chromedriver_binary  
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement

import time
import random

###################################################################
#This section is where user fills out their information 

email = "throw9554@gmail.com"
first_name = "firstname"
last_name = "lastname"
phone = "778 123 4567"
address = "random"
city = "vancouver"
province = "BC"  
#province has to be one of (AB,BC,MB,NB,NL,NS,NT,NU,ON,PE,QC,SK,YT) 
postal_code = "V4A 6N7"

#Note: won't work without a real credit card
card_num = "1234567891234567"
#expire month has to be in range of 1-12
expire_month = "1"
#expire year has to be of current or next years
expire_year = "2024"
cvv = "123"

###################################################################
#This section allows the bot to be compatible with current versions of chrome

#Note, the current version of chromedriver that this bot uses is 103, please update
#PATH based on the newer versions to be compatible.
PATH = 'please put the pathway for the needed version of chromedriver'
options = wd.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')

wd = wd.Chrome(PATH, options=options,);

###################################################################
#function adds time intervals between bot clicks
def randomWait():
    wait_time = random.randrange(4,10)
    time.sleep(wait_time)

#This section goes to the product page
#change the product page to user's desire 
wd.get('https://www.bestbuy.ca/en-ca/product/sony-wh-1000xm5-over-ear-noise-cancelling-bluetooth-headphones-silver/16162186?source=search&asSlot=1')
wd.maximize_window()
wd.implicitly_wait(10)

add_to_cart_button = wd.find_element_by_xpath('//*[@id="test"]/button/span/div')
add_to_cart_button.click()
randomWait()

go_to_cart_button =  wd.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[2]/div/div[3]/div/div/a[1]/span')
go_to_cart_button.click()
randomWait()

checkout_button = wd.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[2]/div/section/div/main/section/section[2]/div[3]/div/a')
checkout_button.click()
randomWait()

continue_button = wd.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div/div/div[1]/div/div[2]/a')
continue_button.click()
randomWait()

###################################################################
#This section fills out the shipping information

email_bar = wd.find_element_by_xpath('//*[@id="email"]')
email_bar.send_keys(email)
randomWait()

fname_bar = wd.find_element_by_xpath('//*[@id="firstName"]')
fname_bar.send_keys(first_name)
randomWait()

lname_bar = wd.find_element_by_xpath('//*[@id="lastName"]')
lname_bar.send_keys(last_name)
randomWait()

phone_bar = wd.find_element_by_xpath('//*[@id="phoneNumber"]')
phone_bar.send_keys(phone)
randomWait()

address_bar = wd.find_element_by_xpath('//*[@id="addressLine1"]')
address_bar.send_keys(address)
randomWait()

city_bar = wd.find_element_by_xpath('//*[@id="city"]')
city_bar.send_keys(city)
randomWait()

province_button = wd.find_element_by_xpath('//*[@id="regionCode"]')
Select(province_button).select_by_value(province)
randomWait()

postal_code_bar = wd.find_element_by_xpath('//*[@id="postalCode"]')
postal_code_bar.send_keys(postal_code)
randomWait()

###################################################################
#This section fills out the payment information

continue_to_payment = wd.find_element_by_xpath('//*[@id="posElement"]/section/section[1]/button')
continue_to_payment.click()
randomWait()

card_number_bar = wd.find_element_by_xpath('//*[@id="shownCardNumber"]')
card_number_bar.send_keys(card_num)
randomWait()

expire_month_bar = wd.find_element_by_xpath('//*[@id="expirationMonth"]')
Select(expire_month_bar).select_by_value(expire_month)
randomWait()

expire_year_bar = wd.find_element_by_xpath('//*[@id="expirationYear"]')
Select(expire_year_bar).select_by_value(expire_year)
randomWait()

cvv_bar = wd.find_element_by_xpath('//*[@id="cvv"]')
cvv_bar.send_keys(cvv)
randomWait()

#I commented out the confirm buy button so it wont automatically purchase for testing purposes
# confirm_button = wd.find_element_by_xpath('//*[@id="posElement"]/section/section[1]/button')
# confirm_button.click()