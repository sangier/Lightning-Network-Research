import selenium 
import time
from selenium import webdriver
from seleniumrequests import Chrome

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

#driver = webdriver.Chrome(".")

driver.get('https://1ml.com/testnet/')
#wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("<Element path>")))
id_box=driver.find_element_by_id("q")
id_box.clear()
#response=driver.request('POST', "https://1ml.com/testnet/", data={id_box:"1445853:27:0"})
print(id_box)
#time.sleep(15)

#body_element = driver.find_element('q', 'body')
#driver.action.send_keys('1445853:27:0', end).perform

#print(body_element)


id_box.send_keys('1445853:27:0')

login_button = driver.find_element_by_name('submit')
response=login_button.click()
print(response)
#https://towardsdatascience.com/controlling-the-web-with-python-6fceb22c5f08