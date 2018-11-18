from selenium import webdriver
#import time

driver = webdriver.Chrome();
driver.get("http://www.google.com");
driver.find_element_by_name("q").send_keys("selenium");
driver.find_element_by_name("q").send_keys(" web");
driver.find_element_by_name("q").send_keys(" driver");
driver.find_element_by_name("q").clear();

