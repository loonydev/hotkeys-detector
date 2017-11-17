# First step is import library:
import hotkeys
import time

# The next step is writing the handle function:
def handle_function(event,parameter):
    print(event)
    if(event.name=='SPACE'):
        parameter['running']=False

# This is dictionary which i droped into function with flags in init HotKeysDetector
parameters={'running':True}
# Init HotKeysDetector with parameters
hotkeysdetector=hotkeys.HotKeysDetector(parameters=True)
# Add hotkeys
# "CONTROL_L+f12" - Hotkeys string
# handle_function - Handle function (yeah, c.o)
# parameters - Hmmm...Parameters (c.o)
hotkeysdetector.addhotkeys("CONTROL_L+f12",handle_function,parameters)
hotkeysdetector.addhotkeys("SPACE",handle_function,parameters)
# Start deamon
hotkeysdetector.start()
# Wait while not pressed space and handle function not set 'running'.
while parameters['running']:
    time.sleep(0.1)
# Close all thread
hotkeysdetector.cancel()
