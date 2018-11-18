from selenium import webdriver

driver = webdriver.Chrome();
driver.execute_script("window.open('http://facebook.com','_blank')");

