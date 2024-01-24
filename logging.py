from selenium import webdriver
from selenium.webdriver.common.by import By
from mahdix import *

try:
    file=open('is_pass_file.txt','r').read().splitlines()
except:
    p('File Not Fount');exit()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
for id_pas in file:
    user_name=id_pas.split('|')[0]
    password=id_pas.split('|')[1]
    clear()
    driver.get("https://twitter.com/i/flow/login")
    sleep(5)
    # Username login
    # user_name="Leonard97896056"
    # password='twitterscraper2024'
    driver.find_element(By.CSS_SELECTOR, '#layers > div > div > div > div > div > div > div.css-175oi2r.r-1ny4l3l.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv.r-1awozwy > div.css-175oi2r.r-1wbh5a2.r-htvplk.r-1udh08x.r-1867qdf.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1 > div > div > div.css-175oi2r.r-1ny4l3l.r-6koalj.r-16y2uox.r-14lw9ot.r-1wbh5a2 > div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-13qz1uu.r-1ye8kvj > div > div > div > div.css-175oi2r.r-1f1sjgu.r-mk0yit.r-13qz1uu > label').send_keys(user_name)
    btns = driver.find_element(By.XPATH, '//div[@role="button"]//*[text()="Next"]').click()
    sleep(1)
    driver.find_element("name","password").send_keys(password)
    sleep(1)
    button_xpath = '//div[@data-testid="LoginForm_Login_Button"]'
    login_button = driver.find_element(By.XPATH, button_xpath)
    login_button.click()
    clear()
    sleep(2)


    cookies = driver.get_cookies()

    formatted_cookies = ";".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
    if 'ct0' in formatted_cookies:
        print(formatted_cookies)
        open('twitter_cookes.txt','a').write(f'{formatted_cookies.replace(" ","")}\n')
        print(mahdilinx())

    driver.delete_all_cookies()
driver.quit()
