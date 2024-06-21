from selenium.webdriver.common.by import By


####################################################
############# Browser configuration ################
####################################################
## Available locators
locator_map = {
    "id": By.ID,
    "name": By.NAME,
    "xpath": By.XPATH,
    "css_selector": By.CSS_SELECTOR,
    "class_name": By.CLASS_NAME,
    "tag_name": By.TAG_NAME,
    "link_text": By.LINK_TEXT,
    "partial_link_text": By.PARTIAL_LINK_TEXT,
}
