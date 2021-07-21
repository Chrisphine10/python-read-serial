# Author: www.freenove.com

import string
from ctypes import windll
import time
import os

def get_drives():
	drives = []
	bitmask = windll.kernel32.GetLogicalDrives()
	for letter in string.ascii_uppercase:
		if bitmask & 1:
			drives.append(letter)
		bitmask >>= 1
	return drives

if __name__ == '__main__':
	before = set(get_drives())
	pause = input("Please insert your USB stick and press Enter key:")
	print("Please wait kiasi...")
	time.sleep(5)
	after = set(get_drives())
	drives = after - before
	delta = len(drives)
	if (delta):
		for drive in drives:
			if os.system("cd " + drive + ":") == 0:
				newly_mounted = drive
				print("Delta: %d, Drives: %s, New: %s" %(delta, drive, newly_mounted))
			else:
				print("Sorry")
	else:
		print("No USB stick inserted.")