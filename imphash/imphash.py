import pefile
from hashlib import md5
import sys

class IMPHASH:
	
	def __init__(self, filepath):
		self.filepath = filepath
		
	def get_imphash(self):
		return pefile.PE(self.filepath).get_imphash()

if len(sys.argv) == 2:
	try:
		calculate_imphash = IMPHASH(sys.argv[1])
		print calculate_imphash.get_imphash()
	except Exception,e:
		print e
else:
	print "Have to give one argument 'filepath'"