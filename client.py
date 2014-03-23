import sys
import httplib
from threading import Thread

IP_ADDRESS = 'localhost'

def make_request():
	# print urllib2.urlopen(url).read()
	connection = httplib.HTTPConnection(IP_ADDRESS)
	command = 'GET dummy.html'
	command = command.split()
	connection.request(command[0], command[1])
	rsp = connection.getresponse()
	data_received = rsp.read()
	print data_received
	connection.close()

if __name__ == '__main__':
	for _ in range(5):
		Thread(target = make_request).start()