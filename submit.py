#!/usr/bin/env python

import sys
import hashlib
import os
from db import DB

class SUBMIT:

	def __init__(self):
		self.db = DB()

	def get_machines_for_OS(self, machine_OS):
		conf_file = open('virtualbox.conf' , 'r')
		array = []
		array_machines = []
		array = conf_file.readlines()
		for i in array:	
			if machine_OS in i:
				array_machines = i.split('=')
				array_machines = array_machines[1].split(',')
				for j in array_machines:
					if machine_OS in j:
						array_machines_for_this_analysis.append(j)
				break
		if len(array_machines)==0:
			print 'virtualbox.conf is needed "machines_32" and "machines_64"'
		return array_machines
	
	def run(self, machine_for_analysis,sample):	
		machines , array_machines = [] , []
		machines = self.db.get_running_machine_according_to_label(machine_for_analysis)
		if machine_for_analysis=='delete':
			self.db.delete_all_rows()
		elif machine_for_analysis=='getdb':
			self.db.get_db()
		elif machine_for_analysis=='-h':
			usage()
		elif machine_for_analysis=='Linux-32' and sample != None:
			array_machines = self.get_machines_for_OS('machines_32')
			self.submit(machines , array_machines , machine_for_analysis , sample)
		elif machine_for_analysis=='Linux-64' and sample != None:
			array_machines = self.get_machines_for_OS('machines_64')
			self.submit(machines , array_machines , machine_for_analysis , sample)
		else:		
			print "Usage : one argument. Example ; Linux-32"				

	def submit(self, machines , array_machines , machine_for_analysis , sample):
		machine_name = array_machines[0]
		if len(machines)>0:
			machine_name = self.get_machines_for_analysis(machines , array_machines)
		arr = []
		arr = sample.split('/')	
		file_path = sample
		file_name = arr[len(arr)-1]
		file_sha1 = hashlib.sha1(sample).hexdigest()
		file_size = os.path.getsize(sample)
		if machine_name != None:
			self.db.insert_new_sample(file_path,file_name,file_sha1,machine_name,machine_for_analysis)
		else:
			print "All machines are busy!!!"

	def get_machines_for_analysis(self, running_machine,all_machines):
		all_machines = [w.replace('\n', '') for w in all_machines]
		for i in running_machine:
			for j in all_machines:
				if i==j:
					all_machines.remove(j)
		machine = None
		if len(all_machines)>0:
			machine = all_machines[0]

		return machine
	
	def usage(self):
		print 'analysis for Linux32 : Linux-32 sample'
		print 'analysis for Linux64 : Linux-64 sample'
		print 'delete all rows      : delete'
		print 'get database         : getdb'
		print 'help                 : -h'

sbmt = SUBMIT()

if len(sys.argv)>1:
	if len(sys.argv)==2:
		argv2 = None
	else:
		argv2 = sys.argv[2]
	sbmt.run(sys.argv[1],argv2)
else:
	sbmt.usage()
