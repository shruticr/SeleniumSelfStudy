from selenium import webdriver
#from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome();
driver.get("http://www.amazon.com");
select_option = driver.find_element_by_id("searchDropdownBox");
options_all = select_option.find_elements_by_tag_name("option");
for i in options_all:
    if i.text == "Amazon Devices":
        i.click();


    #print(i.text);

#driver.find_element_by_id("twotabsearchtextbox").send_keys("MacBook");

#driver.quit();
