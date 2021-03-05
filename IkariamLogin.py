from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
from City import City

def click(Xpath):
        startTime = time.time()
        flag = False
        while not flag:
            try:
                driver.find_element_by_xpath(Xpath).click()        
                flag = True
                break
            except:
                time.sleep(0.2)        
                flag = False
            if(time.time()-startTime) >5:
                print("Cant Click")
                flag = True
                break
            
def clickCooky(Xpath_Arr):
    flag = False
    startTime = time.time()
    while not flag:
        for path in Xpath_Arr:
            if (time.time()-startTime > 5):
                    flag = True
                    break
            try:
                driver.find_element_by_xpath(path).click()        
                flag = True
                break
            except:
                print(path)
                time.sleep(0.2)
                flag = False
                
                

def sendKeys(Xpath, Keys):
    flag = False
    while not flag:
        try:
            driver.find_element_by_xpath(Xpath).send_keys(Keys)
            flag = True
        except:
            time.sleep(0.2)
            flag = False


myMail= 'ekrem.basari2@gmail.com'
myPassword= 'Noparola10'

# Bos Insa Alani/Title = print(driver.find_element_by_xpath(rightMarinaZoneXPath).get_attribute('title'))

# Cities own

citiesMenuXpaths=["/html/body/div[1]/div[16]/div[1]/ul/li"]



# Login XPaths
loginMailXPath = "/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/form/div[1]/div/input"
loginPasswordXPath = "/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/form/div[2]/div/input"
loginButton1Xpath = "/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/ul/li[1]/span"
loginButton2Xpath = "/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/form/p/button[1]/span"
playButton1XPath = "/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/a/button/span"
# Server PAN play button
playButton2XPath = "/html/body/div[1]/div/div/div/div[2]/section[1]/div[2]/div/div/div[1]/div[2]/div/div/div[11]/button/span"
#Cokies
cookiesButton1XPath = ["/html/body/div[3]/div/div/span[2]/button[2]","/html/body/div[4]/div/div/span[2]/button[2]"]
cookiesButton2XPath = ["/html/body/div[3]/div/a","/html/body/div[4]/div/a"]


# City Map Locations XPaths
leftMarinaZoneXPath = "/html/body/div[1]/div[7]/div/div/div[1]/div[4]/a"
rightMarinaZoneXPath = "/html/body/div[1]/div[7]/div/div/div[1]/div[7]/a"


# Main User interface Buttons
marinaPupCloseXPath = "/html/body/div[1]/div[15]/div/div[1]/div[2]"                 
sehriGosterButtonXPath = "/html/body/div[1]/div[2]/div[1]/div[2]/form/div[4]/a"
dropDownCityMenu = "/html/body/div[1]/div[2]/div[1]/div[2]/form/div[1]/span"

# Navigation Arrows XPaths. It is neccessary, since can't find item if it is not in perspective.
navDownButtonXPath = "/html/body/div[1]/div[12]/div/div[1]/ul/li[7]/a"
navUpButtonXPath = "/html/body/div[1]/div[12]/div/div[1]/ul/li[2]/a"



driver = webdriver.Chrome()
driver.maximize_window() # Max Browser window


driver.get("https://tr.ikariam.gameforge.com/")
click(loginButton1Xpath) #Login

sendKeys(loginMailXPath, myMail)
sendKeys(loginPasswordXPath,myPassword)

click(loginButton2Xpath)
click(playButton1XPath)
click(playButton2XPath)
clickCooky(cookiesButton1XPath)

# switch to the new window which is second in window_handles array
driver.switch_to.window(driver.window_handles[1])

#driver.get("https://s39-tr.ikariam.gameforge.com/?view=city&oldBackgroundView=city&containerWidth=1366px&containerHeight=651px&worldviewWidth=1366px&worldviewHeight=605px&cityTop=-404px&cityLeft=-1865px&cityRight=&cityWorldviewScale=0.55")
clickCooky(cookiesButton2XPath)


click(navDownButtonXPath) #Move down the map
click(navDownButtonXPath)

click(leftMarinaZoneXPath)
click(marinaPupCloseXPath)


click(navUpButtonXPath) #Move Up the map
click(navUpButtonXPath)

anaSehir = City(driver,citiesMenuXpaths[0])




