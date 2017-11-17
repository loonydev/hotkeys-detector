from __future__ import print_function
import threading
import pyxhook
import time
class HotKeysDetector(threading.Thread):
    """docstring for HotKeysDetector."""
    def __init__(self,parameters=False):
        threading.Thread.__init__(self)
        self.finished = threading.Event()
        # self.parameters={
        # 'pressed':'',
        # 'maximum_length':0,
        # 'list_hot_keys':{},
        # 'parameters':parameters_flag,
        # 'running':True
        # }


        self.pressed=''
        self.maximum_length=0
        self.list_hot_keys={}
        self.parameters=parameters
        self.running=True

        self.hookman = pyxhook.HookManager()
        # Define our callback to fire when a key is pressed down
        self.hookman.KeyDown = self.key_press_event
        # Hook the keyboard
        self.hookman.HookKeyboard()
        # Start our listener
        self.hookman.start()


    def key_press_event(self,event):
        # print('---------------------------')
        # print(event)
        # print('-----')
        #
        self.pressed=self.pressed+"+"+event.Key.upper()
        if(len(self.pressed.split('+'))+1>self.maximum_length):
            self.pressed=self.pressed[self.pressed.find('+')+1:]

        # print('---------------------------')
        # print(self.list_hot_keys)
        # print(self.pressed)
        for keys in self.list_hot_keys:
            if(keys in self.pressed):
                #print('HotKeys detect '+keys)
                if(self.list_hot_keys[keys]['parameter'] is None):
                    self.list_hot_keys[keys]['events'](keys)
                else:
                    self.list_hot_keys[keys]['events'](keys,self.list_hot_keys[keys]['parameter'])
    def run(self):
        while self.running:
            time.sleep(0.1)
        self.cancel()

    def cancel(self):
        self.running=False
        self.hookman.cancel()
        self.finished.set()



    def addhotkeys(self,string_key,events,parameter=None):
        self.list_hot_keys[string_key.upper()]={'events':events, 'parameter':parameter}
        if(len(string_key.split("+"))+1>self.maximum_length):
            self.maximum_length=len(string_key.split("+"))+1



class hotkey:
    """docstring for hotkey."""
    def __init__(self, hotkey_string):
        super(hotkey, self).__init__()
        self.arg = arg
