#!/usr/bin/env python

import time
from db import DB
from server import SERVER
import thread

class MAIN:

	def __init__(self):
		try:
			self.database = DB()	
			self.port = 12345
		except Exception,e:
			print e

	def server(self,file_path):
		try:
			srv = SERVER(file_path , self.port)
			srv.open_socket()
		except Exception,e:
			print e
	
	def main(self):
		while(True):
			try:
				ret = str(self.database.check_db_for_waiting())
				if ret != 'None': 
					arr = ret.split(',')
					file_path = arr[0]
					id_of_waiting_sample = int(arr[1])
					thread.start_new_thread(self.server, (file_path, ) )
					print "ID = " + str(id_of_waiting_sample) + " Analysis is started"	
					self.database.update_new_sample(id_of_waiting_sample)
				else:
					print "Waiting"
				time.sleep(5)
			except Exception,e:
				print e

mn = MAIN()
mn.main()
