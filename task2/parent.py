import os
import random as rnd
import time
import sys

def fork():
	child_pid = os.fork()
	if child_pid > 0:
		print('Parent[', os.getpid(), ']: I ran children process with PID', child_pid, '.')
	else:
		rand_num = rnd.randint(5,10)
		os.execl(sys.executable, sys.executable, "child.py", str(rand_num))
	return child_pid

def work(fork_count: int):
	processes = []
	for i in range(fork_count):
		processes.append(fork())
	while processes:
		child_pid, exit_code = os.wait()
		exit_code = os.waitstatus_to_exitcode(exit_code)
		if child_pid != 0:
			print('Parent[', os.getpid(), ']: Child with PID', child_pid, 'terminated. Exit Status', exit_code,'.')
			processes.remove(child_pid)
			if exit_code != 0:
				processes.append(fork())
			
def main():
	work(int(sys.argv[1]))



main()
