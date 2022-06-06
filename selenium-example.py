
# import webdriver
from selenium.webdriver.common.by import By

import time

from selenium import webdriver
  
# create webdriver object
driver = webdriver.Chrome()
  
# get geeksforgeeks.org
driver.get("https://takeuforward.org/interviews/strivers-sde-sheet-top-coding-interview-problems/")

elements = driver.find_elements_by_tag_name('details')
time.sleep(15)
print("Starting")

final_string = ""

for k in range(0, 27):
    if(k != 0):
        elements[k].click()
    topic = elements[k].find_elements_by_tag_name('summary')[0].text
    j = 0
    for i in topic:
        if(i == ":"):
            topic = topic[j+2:]
        j = j+1
        questions = ""
        quesvar = elements[k].find_elements_by_tag_name('tr')
    for i in range(1, len(quesvar)):
        questions = questions + str(i) + ")  " + quesvar[i].find_elements_by_tag_name('td')[0].text + "\n"

    final_string = final_string + topic + "\n" + questions + "\n"

print(final_string)