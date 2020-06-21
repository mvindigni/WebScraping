from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://leagueoflegends.fandom.com/wiki/List_of_champions")

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="mw-content-text"]/table[2]'))
    )
finally:
    champList = driver.find_elements_by_xpath('//*[@id="mw-content-text"]/table[2]')

champions = []

for champ in champList:
    champions.append(champ.find_element_by_xpath(
        '// *[ @ id = "mw-content-text"] / table[2] / tbody / tr[1] / td[1]'
    ).get_attribute("data-sort-value"))

driver.close()

print(champions)
