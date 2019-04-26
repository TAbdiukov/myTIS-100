from baseconv import BaseConverter
from etaprogress.progress import ProgressBar
import keyboard, mouse
import pyautogui
import string
import time


def main():
	PROGRAM_NAME = "TIdict"
	SLEEP_TIME = 1	
	DELAY = 2 #seconds
	
	HOW_TO = """
	1. Launch this script
	2. Wait for script to finish
	3. Launch AHK script and switch to the game
	[The game has to be in sandbox mode
	"""
	
	print("HOW TO")
	print(HOW_TO)

	myBase = BaseConverter(string.ascii_uppercase)
	
	brute_min = int(myBase.decode("A"))
	brute_max = int(myBase.decode("ZZZZ"))
	work = brute_max-brute_min+1
	epic = work//20
	
	bar = ProgressBar(work)
	
	d = open("dict.txt", "a+")
	
	# print for user
	print(PROGRAM_NAME+" initialised")
	print("the filling in will begin in "+str(DELAY)+"s")
	# allow user to change brute_mind
	time.sleep(DELAY)
		
	
		
	#payload
	i = 0
	for i in range(work):
		k=i+brute_min
			
		k_string = myBase.encode(k) # convertion to the text		
		
		d.write(k_string+"\n")
		
		bar.numerator = i
		if(k % epic == 0): print(str(bar).strip())

	bar.numerator = i
	print(str(bar).strip())

if __name__ == '__main__':
	main()