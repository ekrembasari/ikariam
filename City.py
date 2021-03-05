import time

class City:
    def __init__(self,driver,cityXPath):
        self.driver = driver
        self.cityXPath = cityXPath
        

        self.cityBuildings = []
        self.dropDownCityMenu = "/html/body/div[1]/div[2]/div[1]/div[2]/form/div[1]/span"
        self.sehriGosterButtonXPath = "/html/body/div[1]/div[2]/div[1]/div[2]/form/div[4]/a"
        self.buildingUpgradeButtonId = "js_buildingUpgradeButton"
                                      

        self.arrBuildings()

    def click_XP(self,Xpath):
        startTime = time.time()
        flag = False
        while not flag:
            try:
                self.driver.find_element_by_xpath(Xpath).click()        
                flag = True
                break
            except:
                time.sleep(0.2)        
                flag = False
            if(time.time()-startTime) >10:
                print("Cant Click")
                flag = True
                break

    def click_Id(self,Id):
        startTime = time.time()
        flag = False
        while not flag:
            try:
                elements = self.driver.find_elements_by_id(Id)
                for e in elements: # ticaret limaninda upgrade yapmayi denedigimde birden fazla ayni Id'li button vardi.
                    try:
                        e.click()
                    except:
                        print("This Id="+ Id + "is not button")
                
                
            except:
                time.sleep(0.2)        
                flag = False
            if(time.time()-startTime) >10:
                print("Cant Click")
                flag = True
                break

    def arr_Buildings(self):
        self.cityBuildings = []

        positionValues = ["Need Burokrasi","Empty"]

        for pos in range(20):
            temp = self.driver.find_element_by_id("js_CityPosition"+str(pos)+"Link").get_attribute('title')
            if temp == "Boş inşa alanı" :
                self.cityBuildings.append(positionValues[1])
                
            elif temp == "Buraya inşa yapabilmeniz için, Bürokrasi`yi araştırmanız gerekmektedir":
                self.cityBuildings.append(positionValues[0])
            else:
                print(str(pos) +". Position = "+temp)
                temp = temp.split('(')
                temp1 = temp[1].split(')')
                self.cityBuildings.append(["js_CityPosition"+str(pos)+"Link",temp[0][:len(temp[0])-1],temp1[0]])

    def open_City(self):
        """
        İslem yapmak istedigimiz sehri webdriverda aciyor
        """
        self.click_XP(self.dropDownCityMenu)
        self.click_XP(self.cityXPath)
        self.click_XP(self.sehriGosterButtonXPath)


    # def isUpgrading(self)

    # def enoughResource(self)

    def upgrade(self,buildingName):
        self.openCity()
        buildingId=[]

        for b in self.cityBuildings:
            if b[1] == buildingName:
                buildingId.append([b[0],b[2]])

        minLev=buildingId[0] 
        print(minLev)      
        for m in buildingId:
            if minLev[1] >= m[1]:
                minLev=[m[0],m[1]]   

        self.click_Id(minLev[0])
        self.click_Id(self.buildingUpgradeButtonId)

    