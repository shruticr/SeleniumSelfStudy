from selenium import webdriver

driver = webdriver.Chrome();
driver.get("http://testwisely.com/demo");
driver.find_element_by_link_text("Survey").click();
driver.find_element_by_xpath("//input[@name = 'role' and @value = '10%']").click();