# using selenium and chrome webDriver to automate the facebook login

from selenium import webdriver 

# taking user_id & password from user

user_id = input("Enter the email")
user_pass = input("Enter the password")

# opening Chrome

browser = webdriver.Chrome('C:\\webdrivers\\chromedriver.exe')

# opening facebook

browser.get('https://www.facebook.com/')

#  finding fb input field by id and filling it  

email_element = browser.find_element_by_id("email")
email_element.send_keys(user_id)
pass_element = browser.find_element_by_id("pass")
pass_element.send_keys(user_pass)

# finding and clicking the login button

login_btn = browser.find_element_by_id("u_0_b")
login_btn.click()

# closing browser

browser.quit()