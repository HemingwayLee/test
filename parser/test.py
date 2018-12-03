import time
from selenium import webdriver

driver = webdriver.Chrome('/Users/Rosemary/Downloads/chromedriver') 
driver.get('http://npb.jp/bis/2018/stats/idb2_g.html')
time.sleep(5) # Let the user actually see something!

tbody = driver.find_element_by_xpath('//*[@id="stdivmaintbl"]/table/tbody')
# print("tbody: ", tbody)

for tr in tbody.find_elements_by_class_name('ststats'):
  for td in tr.find_elements_by_tag_name('td'):
    print(td.text)

driver.quit()


