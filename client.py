#!/usr/bin/env python
import socket

class CLIENT:
	
	def __init__(self, ip, port):
		try:
			self.ip   = ip		
			self.port = port
			self.s = socket.socket()
			self.s.connect((self.ip, self.port))

		except Exception,e:
			print e

	def send_file(self, sfile):
		try:
			cmd = 'send'+'\n%s\n' % sfile
	    		self.s.sendall(cmd)
			s_file = open(sfile,'r')	
			self.s.sendall(s_file.read())
			self.s.recv(2)
			self.close()

		except Exception,e:
			print e

	def get_file(self):
		try:
			cmd = 'get'+'\n%s\n'
			self.s.sendall(cmd)
			if self.s.recv(4) == 'True':
				file_name = self.s.recv(1024)
				file_name = file_name[:file_name.find('\n')]
				print file_name
				size = int(self.s.recv(16))
				print size
				recvd = ''
				received_file = open(file_name,'wb')
				while size > len(recvd):
					if len(recvd)==0:
						data = self.s.recv(1024)
					elif size/len(recvd) >1:
						data = self.s.recv(1024)
					else: 
						data = self.s.recv(size - len(recvd))
					received_file.write(data)
					if not data: 
						break
					recvd += data		
				self.s.sendall('ok')	
		
		except Exception,e:
			print e	
	
	def close(self):
		try:
			self.s.sendall('close\n')

		except Exception,e:
			print e

clnt = CLIENT('192.168.35.103', 12345)
clnt.get_file()










