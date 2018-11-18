from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome();
driver.get("http://testwisely.com/demo");
time.sleep(1);
driver.set_window_size(1024,768);
driver.set_window_position(100,100);
driver.implicitly_wait(10);
driver.find_element_by_link_text("Customer Interview").click();
driver.find_elements_by_link_text("Show Answer")[1].click();

driver.get("http://testwisely.com/demo/netbank");
assert(driver.find_element_by_id("transfer_btn").is_displayed());
time.sleep(10);

driver.get("http://testwisely.com/demo/survey");
select_box = Select(driver.find_element_by_name("role")).select_by_visible_text("Manager");
time.sleep(10);

driver.quit();





