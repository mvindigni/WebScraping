from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://leagueoflegends.fandom.com/wiki/List_of_champions")

try:
    element = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH, '//*[@id="mw-content-text"]/table[2]/tbody'))
    )
finally:
    champTable = driver.find_element_by_xpath('//*[@id="mw-content-text"]/table[2]/tbody')

champList = champTable.find_elements(By.TAG_NAME, "tr")

champions = []
counter = 1

for row in champList:
    name = row.find_element_by_xpath(
        '// *[ @ id = "mw-content-text"] / table[2] / tbody / tr[' + str(counter) + '] / td[1]'
    )
    champions.append(name.get_attribute('data-sort-value'))
    counter += 1

driver.close()

print(champions)
