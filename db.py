#!/usr/bin/env python

import sqlite3
from dbutil import DBUTIL

class DB:

	

	def __init__(self):
   		self.db = DBUTIL()
		self.conn = self.db.connect_DB()
	
	def add_new_column(self,column):
		self.conn.execute("alter table task add column '%s' 'text'" % column)
	
	def get_db(self):
		cursor = self.conn.execute("SELECT * from task")
		for row in cursor:
			print row

	def get_running_machine_according_to_label(self,machine_label):
		cursor = self.conn.execute("SELECT machine_name from task Where (machine_state='Running' OR machine_state='Waiting') AND machine_label='%s'" %machine_label)		
		machine = []
		for row in cursor:
			machine.append(row[0])
		return machine

	def insert_new_sample(self,file_path,file_name,file_sha1,machine_name,machine_label):
		self.conn.execute("INSERT INTO task (machine_name,machine_state,machine_label,file_path,file_name,file_sha1,analysis_state) VALUES ('%s','Waiting','%s','%s','%s','%s','Waiting')" %(machine_name,machine_label,file_path,file_name,file_sha1));
		self.conn.commit()

	def update_new_sample(self,ID):
		self.conn.execute("UPDATE task SET machine_state = 'Running', analysis_state = 'Running' WHERE ID='%d';" %ID);
		self.conn.commit()

	def check_db_for_waiting(self):
		cursor = self.conn.execute("SELECT file_path,id from task Where machine_state='Waiting'")
		file_path = None
		for row in cursor:
			file_path = row[0]+ ','+ str(row[1])
			break
		return file_path
		
	def delete_all_rows(self):
		self.conn.execute("DELETE FROM task");
		self.conn.commit()


