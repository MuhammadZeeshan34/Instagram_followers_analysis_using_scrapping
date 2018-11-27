from bs4 import BeautifulSoup
import pandas as pd
import os, time, re, itertools, sys, random
import requests, urllib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import (
    presence_of_element_located)
from selenium.webdriver.support.wait import WebDriverWait

data = "/Users/zeeshannawaz/UpWork/Scrapping/instagram_beautybrands"

def site_login(driver):
    url = "https://www.instagram.com"
    login_url = os.path.join(url, "accounts","login")
    driver.get(login_url)
    time.sleep(1)
    driver.find_element_by_name('username').send_keys('')
    driver.find_element_by_name('password').send_keys('')
    time.sleep(1)
    driver.find_elements_by_class_name('oF4XW')[1].click()

def get_followers(driver, user_id):


    driver.get(user_id)
    followers = ""

    if len(driver.find_elements_by_class_name('p-error')) > 0:
        return followers

    follow_link = driver.find_elements_by_class_name('_5f5mN')
    if len(follow_link) == 0:
        return followers
    follow_link[0].click()

    time.sleep(2)



    basic_details = driver.find_elements_by_class_name('-nal3')

    # html = driver.page_source

    # selector = 'header > section > ul > li > a > span'
    # basic_details = soup.select(selector)
    # basic_details = soup.find_all('div')
   # print("Total posts : ", basic_details[0].text)
    print("Following : ", basic_details[2].text)
   # print("Following : ", basic_details[2].text)
    time.sleep(2)
    is_found_followers = False

    #allfoll = int(str(driver.find_elements_by_class_name('g47SY')[2].get_property('title')).replace(",", ""))
    allfoll = int(driver.find_elements_by_class_name('g47SY')[2].text.replace(',',''))
    for element in basic_details:
        if element.get_attribute('href'):
            basic_details[2].click()
            #element.click()
            is_found_followers = True
            break

            # basic_details[1].click()

            # elm4 = driver.find_element_by_xpath("//div[2]/ul/li[2]/a")
            # elm4.click()

            # followers_url = basic_details[1].get_attribute('href')
    # driver.find_element_by_class_name(followers_url)
    # print(driver.find_element_by_class_name('eiUFA'))
    # next = len(driver.find_elements_by_class_name('wo9IH'))
    # print("Sleeping")
    # time.sleep(random.randint(500, 1000) / 100)
    # print("Sleeping end")
    time.sleep(2)
    if is_found_followers:
        followers_dialoge = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]")
        prev_length = 0
        next_length = 0
        while (len(driver.find_elements_by_class_name('FPmhX')) < 5):
            time.sleep(1)

        count = 0
        count_other = 0
        stuck_count = 0

        n = 2
        condition = True
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_dialoge)
        driver.execute_script("arguments[0].scrollDown = arguments[0].scrollHeight / 2", followers_dialoge)
        while(condition):
            next_length = len(driver.find_elements_by_class_name('FPmhX'))
            # if i % 10 == 0:
            #     print("COUNT ==== ", count)
            #     print("COUNT- Other ==== ", count_other)
            #if next_length != prev_length:
              #  new_followers = driver.find_elements_by_class_name('FPmhX')[-12:]
              #  count_other += 12

                # with open(followers_dir, "a") as followers_file:
                #
                #     for element in new_followers:
                #         if element.get_property('href'):
                #             title = element.get_property('title')
                #             href = element.get_property('href')
                #             followers_file.write(title + "," + href + "," + "\n")
                #             count += 1


            time.sleep(0.3)
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_dialoge)
            time.sleep(0.3)
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_dialoge)
            #time.sleep(random.randint(500, 1000) / 1000)
           # time.sleep(0.5)


            prev_length = next_length


           # print("Extracting friends %", round((i / (allfoll / n) * 100), 2), "from", "%100")
           # next = len(driver.find_elements_by_class_name('FPmhX'))

            followers = driver.find_elements_by_class_name('FPmhX')
            next_length = len(followers)
            if next_length == prev_length and len(followers) > 29:
                print (stuck_count)
                print(len(followers))
                stuck_count += 1

            if len(followers)+10 >= allfoll or len(followers) > 503 or stuck_count > 17:
                condition = False
    return followers

def get_user_location(profile_id):
    driver.get(profile_id)


def get_number(profile_id):
   # driver = webdriver.Chrome(r"/Users/zeeshannawaz/Downloads/chromedriver")
    driver = webdriver.Firefox()

    driver.get(profile_id)
    number = ""
    if driver.page_source.find('"business_phone_number":null') == -1:
        soup = BeautifulSoup(driver.page_source,'html.parser')
        for xx in str(soup.find_all('script')[7]).split(","):
            if "business_phone_number" in xx:
                number = xx.split(":")[1]
                break
    driver.close()

    return number


def insta_scrapping(profile_url):
    #driver = webdriver.Chrome(r"/Users/zeeshannawaz/Downloads/chromedriver")
    driver = webdriver.Firefox()
    #response = requests.get(profile_url)
    #soup = BeautifulSoup(response.text, 'html.parser')
    site_login(driver)
    time.sleep(2)

    followers = get_followers(driver, profile_url)
    print(len(followers))

    #count = 1
    followers_dir = os.path.join(data,"followers_final.csv")
    with open(followers_dir,"w") as followers_file:
        #followers_list = {}
       # for element in followers:
            if element.get_property('href'):
          #      print(count)
          #      count += 1
                title = element.get_property('title')
                href =  element.get_property('href')
                #ph_no = get_number(href)
                #followers_list[title] = href
                followers_file.write(title + "," + href + "," + "\n")




    # list of followers that you have followed
    #return ([nm1[i] for i in [i for i, x in enumerate(st1) if x == "Following"]])


def get_business_page_details(username,  fols_dict, file):

    #driver = webdriver.Chrome(r"/Users/zeeshannawaz/Downloads/chromedriver")
    driver = webdriver.Firefox()
    #site_login(driver)

    for index, value in fols_dict.items():
        name = index
        url  = value
        driver.get(url)

        if len(driver.find_elements_by_class_name('p-error')) > 0:
            continue

        if driver.page_source.find('"business_phone_number":null') == -1:
            ph_number = ""
            business_name = name
            business_category = ""
            business_city = ""
            business_email = ""
            business_country = ""
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            for xx in str(soup.find_all('script')[7]).split(","):
                if "business_phone_number" in xx:
                    ph_number = xx.split(":")[1]
                if "business_email" in xx:
                    business_email = xx.split(":")[1]
                if "business_category_name" in xx:
                    business_category = xx.split(":")[1]
                    business_category = ":".join(business_category.split("\\u0026"))
                if "city_name" in xx:
                    business_city = xx.split(":")[1]
                if "country_code" in xx:
                    business_country =  xx.split(":")[1]

            file.write(username + "," + business_name + "," + business_category + "," +  ph_number + ","
                   + business_email + "," + business_city + "," + business_country + "\n")








if __name__ == '__main__':
   # insta_server = 'https://www.instagram.com'
   # user_name = 'lanolips'
   # user_profile = os.path.join(insta_server, user_name)
    #fol1 = insta_scrapping(user_profile)
    driver = webdriver.Chrome(r"/Users/zeeshannawaz/Downloads/chromedriver")
    #driver = webdriver.Firefox()
# response = requests.get(profile_url)
# soup = BeautifulSoup(response.text, 'html.parser')
    check_file = os.path.join(data, "check2.csv")
    with open(check_file, 'a') as f_check:
        f_check.write("\n")
    driver.delete_all_cookies()
    site_login(driver)
    time.sleep(2)
    followers_dir = os.path.join(data, "followers5.csv")
    business_dir = os.path.join(data, "business4_followers.csv")

    with open(followers_dir, 'r') as file:
        with open(business_dir, 'a') as b_file:
            b_file.write("Username" + "," + "Business Name" + "," + "Category" + "," + "Phone Number" + ","
                          + "Email" + "," + "City" + "," + "Country" + "\n")
            count = 1
            for line in file:
                is_already_scrapped = False
                username = line.split(",")[0]

                with open(check_file, 'r') as f_check:
                # Check if this username is present in the file or not
                    for line_check in f_check:
                        if str(line_check).rstrip('\n') == username:
                            is_already_scrapped = True




                if is_already_scrapped == False:
                    fol_link = line.split(",")[1]
                    followers = get_followers(driver, fol_link)
                    if followers != "":
                        if len(followers) > 500:
                            followers = followers[:500]
                        dict_ = {}
                        for sub_fol in followers:
                            #dict_[sub_fol.text] = sub_fol.get_attribute('href')
                            # Go to each follower and check if it is a business page and get details if it is
                        #print ("Count " + str(count) + " username")
                       # get_business_page_details(username, dict_, b_file)
                            b_file.write(username + "," + sub_fol.text + "\n")
                         #   print (username, sub_fol.text)

                        with open(check_file, 'a') as f_check:
                            f_check.write(username + "\n")
                        count += 1
                    else:
                        with open(check_file, 'a') as f_check:
                            f_check.write(username + "\n")


            c = 0





# Strategy

# get a url from the list
# Open it in the driver
# Open its followers
# Go to each follower
# Open profile and check if it is a business page
# If business page, check its name and category and save it in a file
# username - business page name - business page category
