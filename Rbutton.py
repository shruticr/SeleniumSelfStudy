from selenium import webdriver

driver = webdriver.Chrome();
driver.get("http://testwisely.com/demo/survey");
driver.find_element_by_xpath("//input[@name = 'role' and @value = '50%']").click();

assert(driver.find_element_by_xpath("//input[@name = 'role' and @value = '50%']").is_selected());

driver.quit();


