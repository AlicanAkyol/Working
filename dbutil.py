#!/usr/bin/python

import sqlite3

class DBUTIL:
	def __init__(self):
   		print 'dbutil.py is worked successfully!!!'

	def connect_DB(self):
		conn = sqlite3.connect('textDB.db')
		return conn
