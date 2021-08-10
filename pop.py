import time
from threading import Thread
from pynput.keyboard import Key, Listener
from pynput.keyboard import Controller

class Spam(Thread):
	keyboard = Controller()
	def __init__(self, key):
		super(self.__class__, self).__init__()
		self.key = key
		self.spamming = False
		self.end = False
		
	def run(self):
		while not self.end:
			if self.spamming:
				Spam.keyboard.press(self.key)
				Spam.keyboard.release(self.key)
			time.sleep(0.055)
			
	def spam(self):
		self.spamming = True
		
	def pause(self):
		self.spamming = False
		
	def leave(self):
		self.end = True
		

spam = Spam('a')
spam.start()

def on_release(key):
	try:
		if key == Key.esc:
			spam.leave()
		elif key.char == 's':
			spam.spam()
		elif key.char == 'p':
			spam.pause()
	except:
		pass

print('按下s開始,p暫停,Esc離開...')
Listener(on_release=on_release).start()
spam.join()