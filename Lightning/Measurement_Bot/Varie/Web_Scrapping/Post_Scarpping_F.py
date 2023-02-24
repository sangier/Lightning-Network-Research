
#N.B. The execution of this 2 command before running this script is Mandatory. : 
# 1 :Xvfb -ac :99 -screen 0 1280x1024x16 &
# 2 :export DISPLAY=:99


from selenium import webdriver
from selenium.webdriver.common import action_chains, keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from seleniumrequests import Chrome
import time 


headless_browser=True
multi_logs=True
nogui=True 


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://1ml.com/testnet/")
assert 'q' in driver.page_source
action = action_chains.ActionChains(driver)
#action2=action_chains.ActionChains(driver)

# open up the developer console, mine on MAC, yours may be diff key combo


#action.send_keys(keys.Keys.ALT+'1445853:27:0')
#action.perform()
print("blblblbl")
#action.perform()
#time.sleep(3)
action.send_keys('1480451:9:0')
#action.perform()
action.send_keys(keys.Keys.ENTER)
action.perform()

#time.sleep(3)


#to find the exact x path of an element: right click on the element -> analizza elemento -> right click -> copia -> Xpath 
pageText = driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[1]/ul[2]/li[1]/div/a/h2").text


print(pageText)

driver.close()




#export DISPLAY=:99