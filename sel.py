from selenium import webdriver 
from time import sleep 
import chromedriver_autoinstaller
import speech_recognition as sr 
import pyttsx3 
import cv2

r = sr.Recognizer() 

chrome_options = webdriver.ChromeOptions()
capabilities = {'browserName': 'chrome', 'javascriptEnabled': True}
capabilities.update(chrome_options.to_capabilities())

# assign url in the webdriver object 
# path = "/home/dell/git_selenium/chromedriver"
chromedriver_autoinstaller.install()
# driver = webdriver.Chrome(path) 
driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)
driver.implicitly_wait(10)
driver.get("https://www.google.co.in/maps/@12.9475078,77.6137011,21591m/data=!3m1!1e3") 
sleep(2) 


def SpeakText(command): 
	
	# Initialize the engine 
	engine = pyttsx3.init() 
	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[1].id)
	engine.say(command) 
	engine.runAndWait() 



# search locations 
def searchplace(): 
	SpeakText("Enter your search place")

	with sr.Microphone() as source2: 
			
			
		r.adjust_for_ambient_noise(source2, duration=0.2) 
			
			
		audio2 = r.listen(source2) 
			
			
		MyText = r.recognize_google(audio2) 
		MyText = MyText.lower() 


	driver.find_element_by_xpath("//*[@id='searchboxinput']").send_keys(MyText)
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
	find.clear()
	sleep(1)
	# find.clear()
	# sleep(1)

	SpeakText("Enter your starting point")
	
	with sr.Microphone() as source2: 
			
			
		r.adjust_for_ambient_noise(source2, duration=0.2) 
			
			
		audio2 = r.listen(source2) 
			
			
		MyText = r.recognize_google(audio2) 
		MyText = MyText.lower() 


	find.send_keys(MyText) 
	sleep(2) 
	search = driver.find_element_by_xpath( 
		"/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]") 
	search.click() 


# get transportation details 
def kilometers(): 
	sleep(5) 
	Totalkilometers = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/div")
        
	print("Total Kilometers:", Totalkilometers.text) 
	SpeakText("Total Kilometers" + Totalkilometers.text)

	sleep(5) 
	Bus = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]") 
	print("Bus Travel:", Bus.text) 
	sleep(5) 
	SpeakText("Bus Travel takes" + Bus.text)
	sleep(2)

	SpeakText("Thank you ! Visit Again ")
	# Train = driver.find_element_by_xpath( 
	# 	"/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[2]/div[1]/div[2]/div[1]/div") 
	# print("Train Travel:", Train.text) 
	# sleep(5) 
	# SpeakText("Train Travel takes" + Train.text)
	# sleep(5)
	#As there are no train facility at the moment , hence commented!
	sleep(2)

	SpeakText("Please Help us with your identity . Press spacebar to update your photo or press escape to exit")

	sleep(2)

	cam = cv2.VideoCapture(0)

	cv2.namedWindow("test")

	img_counter = 1

	while True:
		ret, frame = cam.read()
		if not ret:
			print("failed to grab frame")
			break
		cv2.imshow("test", frame)

		k = cv2.waitKey(1)
		if k%256 == 27:
			# ESC pressed
			SpeakText("Bye have a great day!")
			print("Escape hit, closing...")
			break
		elif k%256 == 32:
			# SPACE pressed
			img_name = "user {}.png".format(img_counter)
			cv2.imwrite(img_name, frame)
			print("{} written!".format(img_name))
			SpeakText("User {} photo updated".format(img_counter))
			img_counter += 1

	cam.release()

	cv2.destroyAllWindows()


if __name__ == '__main__':
    searchplace() 
    directions() 
    find() 
    kilometers()
	# capturee()