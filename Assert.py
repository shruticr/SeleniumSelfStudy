import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome();
driver.get("http://testwisely.com/demo");
print(driver.title);
assert driver.page_source
driver.find_element_by_link_text("Assertion").click()
match_str = "Text assertion " \
            "(new line before)!"
assert match_str, driver.find_elements_by_tag_name("body").text
driver.quit();
