# using selenium and chrome webDriver to automate

from selenium import webdriver

# taking email or phone no. and password as input
 
user_id  = input("Enter your E-mail or phone no. ")
user_pass = input("Enter your Password")

# opening browser

browser = webdriver.Chrome("C:\\webdrivers\\chromedriver.exe")

# opening facebook

browser.get("https://facebook.com")

# finding text fields and giving inputs

email_element = browser.find_element_by_id("email")
email_element.send_keys(user_id)
pass_element = browser.find_element_by_id("pass")
pass_element.send_keys(user_pass)

# find and click the login button

login = browser.find_element_by_id("u_0_b")
login.click()

# finding the no of people have birthday today
# * is to search all elements

k = '//*[@id="home_birthdays"]/div/div/div/div/a/div/div/span/span[2]'
n = browser.find_element_by_xpath(k).get_attribute('textContent')
num = n[0]
num = int(num)

# go to events to wish birthday

browser.get("https://www.facebook.com/events/birthdays/")

# find and write message in field 
bday_list=browser.find_elements_by_xpath("//*[@class ='enter_submit uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea inlineReplyTextArea mentionsTextarea textInput']")

c=0
for element in bday_list: 
    element_id = str(element.get_attribute('id')) 
    XPATH = '//*[@id ="' + element_id + '"]'
    post = browser.find_element_by_xpath(XPATH) #To fetch the box where to enter text
    post.send_keys("Happy Birthday, Best wishes.") # To enter the bday wish
    post.send_keys(Keys.RETURN) #To send the wish
    c=c+1
    if(c>num):  # This prevents putting wishes for belated birthday
        break

browser.quit()