import sys
import httplib
from threading import Thread
from random import randrange

IP_ADDRESS = 'localhost'
flights = ['UA001', 'UA002', 'UA003', 'UA004', 'UA005']
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
types = ['Query', 'Order']

def make_request():
	# print urllib2.urlopen(url).read()
	connection = httplib.HTTPConnection(IP_ADDRESS, 8080)
	# create random query
	rand0, rand1, rand2 = randrange(0, 2), randrange(0, 5), randrange(0, 5)
	query = types[rand0] + '-' + flights[rand1] + '-' + days[rand2]
	command = 'GET ' + query
	command = command.split()
	connection.request(command[0], command[1])
	rsp = connection.getresponse()
	data_received = rsp.read()
	print data_received
	# print 'received'
	connection.close()

if __name__ == '__main__':
	for _ in range(10):
		Thread(target = make_request).start()
