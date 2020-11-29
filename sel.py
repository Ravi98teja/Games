# import required modules 
from selenium import webdriver 
from time import sleep 
chrome_options = webdriver.ChromeOptions()
capabilities = {'browserName': 'chrome', 'javascriptEnabled': True}
capabilities.update(chrome_options.to_capabilities())

# assign url in the webdriver object 
path = "/home/dell/git_selenium/chromedriver"
driver = webdriver.Chrome(path) 
driver.set_window_size(1920, 1080)
driver.implicitly_wait(10)
driver.get("https://www.google.co.in/maps/@12.9475078,77.6137011,21591m/data=!3m1!1e3") 
sleep(2) 
# search locations 
def searchplace(): 
	driver.find_element_by_xpath("//*[@id='searchboxinput']").send_keys("Mahaveer flora")
	driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button").click() 
	 

# get directions 
def directions(): 
	sleep(10) 
	directions = driver.find_element_by_xpath( 
		"/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[1]/div/button") 
    
	directions.click() 



# find place 
def find(): 
	sleep(6) 
	find = driver.find_element_by_xpath( 
		"/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input") 
	find.send_keys("Tirunelveli") 
	sleep(2) 
	search = driver.find_element_by_xpath( 
		"/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]") 
	search.click() 


# get transportation details 
def kilometers(): 
	sleep(5) 
	Totalkilometers = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/div")
        
	print("Total Kilometers:", Totalkilometers.text) 
	sleep(5) 
	Bus = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]") 
	print("Bus Travel:", Bus.text) 
	sleep(7) 
	Train = driver.find_element_by_xpath( 
		"/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[2]/div[1]/div[2]/div[1]/div") 
	print("Train Travel:", Train.text) 
	sleep(7) 

if __name__ == '__main__':
    searchplace() 
    directions() 
    find() 
    kilometers() 





