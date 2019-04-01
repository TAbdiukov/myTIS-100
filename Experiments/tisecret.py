from baseconv import BaseConverter
from etaprogress.progress import ProgressBar
import keyboard, mouse
import pyautogui
import string
import time


def main():
	PROGRAM_NAME = "TIsecret"
	SLEEP_TIME = 1	
	DELAY = 3 #seconds
	
	HOW_TO = """
	1. Launch game
	2. Open up an unsolved problem, eg STACK MEMORY SANDBOX
	3. Land your cursor in the clean block (both in game and real)
	4. Run script
	5. Within delay switch to game
	6. ?..."""
	
	print("HOW TO")
	print(HOW_TO)

	myBase = BaseConverter(string.ascii_uppercase)
	
	brute_min = int(myBase.decode("A"))
	brute_max = int(myBase.decode("ZZZZ"))
	work = brute_max-brute_min

	bar = ProgressBar(work)
		
	# print for user
	print(PROGRAM_NAME+" initialised")
	print("the bruteforce will start in "+str(DELAY)+"s")
	# allow user to change brute_mind
	time.sleep(DELAY)
		
	#payload
	i = 0
	for i in range(work+1):
		k=i+brute_min
			
		k_string = myBase.encode(k) # convertion to the text
		k_string_len = len(k_string)
		
		bar.numerator = i
		print(k_string+" "+str(bar).strip())
		
		"keyboard.write"
		# input
		keyboard.write(k_string, delay=0.1)
		
		# send for compiling
		keyboard.send("f5")
		time.sleep(0.5)
		# wait
		
		# didn't work out? Clean up after yourself
		keyboard.send('esc')
		time.sleep(0.5)

		keyboard.send('ctrl+right')
		keyboard.send('ctrl+right')
		keyboard.send('ctrl+right')
		keyboard.send('ctrl+right')
		keyboard.send('ctrl+right')
		time.sleep(0.5)
		
		keyboard.send('backspace')
		time.sleep(0.5)


if __name__ == '__main__':
	main()