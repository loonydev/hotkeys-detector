#
# -*- coding: utf-8 -*-

from __future__ import print_function

import pyxhook
import time

def kbevent(event,test_dict):
	global running,prev_key
	# print key info
	#print(event.Ascii)
	print(test_dict)
	if((prev_key==227) and(event.Ascii==99)):
		test_dict['test']=2
		# result=get_word(pyperclip.paste(),cursor)
		# for res in result:
		# 	print('##')
		# 	for i in res:
		# 		#print(i)
		# 		pretty_string_gen(i)
		#get_word_api_reverso(pyperclip.paste())
		print('------------------------------------------------------------')
		#pyperclip.copy('')


	prev_key=event.Ascii

	# If the ascii value matches spacebar, terminate the while loop
	if event.Ascii == 32:
		running = False


prev_key=0
test_dict={'test':1}
# Create hookmanager
hookman = pyxhook.HookManager()
# Define our callback to fire when a key is pressed down
hookman.KeyDown = kbevent
hookman.KeyDownParameters = test_dict
# Hook the keyboard
hookman.HookKeyboard()
# Start our listener
hookman.start()

# Create a loop to keep the application running
running = True
while running:
	print(test_dict['test'])
	time.sleep(0.1)

# Close the listener when we are done
hookman.cancel()

if __name__ == '__main__':
	main()
