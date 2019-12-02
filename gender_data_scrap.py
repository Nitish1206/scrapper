import csv
from selenium import webdriver
import pandas as pd
import time
image_link_list=[]
driver = webdriver.Chrome('/home/nitish/nitish/scrapping/chromedriver')
driver.get('https://www.google.com/search?q=indian+car+number+plate+images&tbm=isch&source=univ&sa=X&ved=2ahUKEwiJl6vz9JPkAhUChuYKHSwSCxcQ7Al6BAgHEBs&biw=1375&bih=723')
# contect=
content = driver.find_elements_by_class_name("rg_bx rg_di rg_el ivg-i")
temp_3 = driver.find_elements_by_tag_name('href').click()

for image in temp_3:
    image_link=image.get_attribute('src')
    image_link_list.append(image_link)
# driver.execute_script("window.scrollTo(0, 1000)")


# new_height = driver.execute_script("return document.body.scrollHeight")
# driver.execute_script("window.scrollTo(0,63830)")
# SCROLL_PAUSE_TIME = 0.5
# while True:
#     last_height = driver.execute_script("return document.body.scrollHeight")
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(SCROLL_PAUSE_TIME)
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(SCROLL_PAUSE_TIME)
#         new_height = driver.execute_script("return document.body.scrollHeight")
#         if new_height == last_height:
#
#             temp4 = driver.find_element_by_id('smc')
#             temp5 = temp4.find_element_by_id('smbw')
#             temp6 = temp5.find_element_by_class_name('ksb').click()
            # for tag in temp4:
            #     temp5=tag.get_attribute('ksb')
            #     temp5.click()
#         else:
#             last_height = new_height
#             continue
# print(image_link_list)
df = pd.DataFrame(image_link_list)
df.to_csv("car_image.csv")
# with open('image_link.csv', mode='w') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for row in csv_reader:
#         print(row[1])

# csv_file.close()
