#!/usr/bin/env python
import socket

class SERVER:
	
	def __init__(self, filename , port):
		self.c = None
		self.s = None
		self.port = port
		self.file_name = filename

	def send_file(self):
		with open(self.file_name, 'rb') as f:
		    data = bytearray(f.read())
		
		arr = self.file_name.split('/')
		name_of_file = arr[len(arr)-1]
		self.s.sendall(name_of_file+'\n')
		self.s.recv(2)
		self.s.sendall('%16d' % len(data))
		self.s.sendall(data)
		self.s.recv(2)

	def get_file(self):
		try:
			size = str(self.s.recv(16))
			recvd = ''
			received_file = open('file_from_remote','w')
			while size > len(recvd):
				data = self.s.recv(1024)
				received_file.write(data)
				if not self.s.recv(1024): 
			    		break
				recvd += data	
			self.s.sendall('ok')
		except Exception,e:
			print e
		
	def open_socket(self):
		self.c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.c.bind(('', self.port))
		self.c.listen(1)
		self.s,a  = self.c.accept()
		while True:
			try:
				data = self.s.recv(1024)
				cmd = data[:data.find('\n')]				
				if cmd == 'send':
					self.get_file()
				if cmd == 'get':
					self.s.sendall('True')
					self.send_file()
				if cmd == 'close':
					self.close_socket()
					break
			except Exception,e:
				print e
		
	def close_socket(self):
		self.s.close()
		self.c.close()
