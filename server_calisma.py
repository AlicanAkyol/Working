#!/usr/bin/env python

from SimpleXMLRPCServer import SimpleXMLRPCServer
from xmlrpclib import Binary
import datetime
import hashlib
import os

server = SimpleXMLRPCServer(('localhost', 9000), logRequests=True, allow_none=True)
server.register_introspection_functions()
server.register_multicall_functions()

class ExampleService:
    
	def ping(self):
		"""Simple function to respond when called to demonstrate connectivity."""
		return True

	def now(self):
		"""Returns the server current date and time."""
		return datetime.datetime.now()

	def show_type(self, arg):
		"""Illustrates how types are passed in and out of server methods.

		Accepts one argument of any type.  
		Returns a tuple with string representation of the value, 
		the name of the type, and the value itself.
		"""
		return (str(arg), str(type(arg)), arg)

	def raises_exception(self, msg):
		"Always raises a RuntimeError with the message passed in"
		raise RuntimeError(msg)

	def send_back_binary(self, bin):
		"Accepts single Binary argument, unpacks and repacks it to return it"
		data = bin.data
		response = Binary(data)
		return response

	def recv_file(self, name):
		with open("file", "wb") as handle: 
       			handle.write(name)
		

	def get_file(self, malware):
		file_sha1 = hashlib.sha1(malware).hexdigest()
		file_size = os.path.getsize(malware)

		return file_sha1,file_size

server.register_instance(ExampleService())

try:
    print 'Use Control-C to exit'
    server.serve_forever()
except KeyboardInterrupt:
    print 'Exiting'
