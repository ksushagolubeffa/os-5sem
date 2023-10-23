import os
import time
import random as rnd
import sys

class Child:
	@staticmethod
	def work(arg: int):
		pid = os.getpid()
		print('Child[', pid, ']: I am started. My PID', pid, '. Parent PID', os.getppid(), '.')
		time.sleep(arg)
		print('Child[', pid, ']: I am ended. PID', pid, 'Parent PID', os.getppid(), '.')
		exit_code = rnd.randint(0,1)
		os._exit(exit_code)
def main():
	Child.work(int(sys.argv[1]))

main()
