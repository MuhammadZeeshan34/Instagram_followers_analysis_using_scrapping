import pandas as pd
import os
import requests, urllib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import (
    presence_of_element_located)
from selenium.webdriver.support.wait import WebDriverWait

data = "/Users/zeeshannawaz/UpWork/Scrapping/instagram_beautybrands"
business_file = os.path.join(data,'business4_followers.csv')
business_file_dict = os.path.join(data,'business_dict_followers.csv')
final_business_file = os.path.join(data, 'Followers_Data.csv')


# business_accounts_dict = {}
# df = pd.read_csv(business_file)
# count = 1
# for index, row in df.iterrows():
#     if row[1] not in business_accounts_dict:
#         business_accounts_dict[row[1]] = 1
#     else:
#         business_accounts_dict[row[1]] = business_accounts_dict[row[1]] + 1
#     count += 1
#
#     if count % 100 == 0:
#         print(count, len(business_accounts_dict))
#
# with open(business_file_dict, 'w') as file:
#     for key, value in business_accounts_dict.items():
#         file.write(str(key) + "," + str(value) + "\n" )


saving_file = os.path.join(data,'usernames2.csv')
with open(saving_file,'w') as saving_file_writer:
    driver = webdriver.Chrome(r"/Users/zeeshannawaz/Downloads/chromedriver")
    df = pd.read_excel(final_business_file)
    for index, row in df.iterrows():
        username = row[0]
        if username not in []:
            url = "https://www.instagram.com"
            user_profile = os.path.join(url, username)
            driver.get(user_profile)
            name = int(driver.find_elements_by_class_name('g47SY')[1].get_attribute('title').replace(",",""))
            print(username,name)
            saving_file_writer.write(username + "," + str(name) + "\n")







