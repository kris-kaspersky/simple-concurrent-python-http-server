import sys
import httplib
from threading import Thread
from random import randrange
from datetime import datetime
from multiprocessing import Process

IP_ADDRESS = 'localhost'
flights = ['UA001', 'UA002', 'UA003', 'UA004', 'UA005']
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
# types = ['Query', 'Order']

def make_query_request():
	# print urllib2.urlopen(url).read()
	connection = httplib.HTTPConnection(IP_ADDRESS, 8080)
	# create random query
	rand1, rand2 = randrange(0, 5), randrange(0, 5)
	query = 'Query-' + flights[rand1] + '-' + days[rand2]
	command = 'GET ' + query
	command = command.split()
	connection.request(command[0], command[1])
	rsp = connection.getresponse()
	data_received = rsp.read()
	# print data_received
	# print 'received'
	connection.close()

def make_order_request():
	# print urllib2.urlopen(url).read()
	connection = httplib.HTTPConnection(IP_ADDRESS, 8080)
	# create random query
	rand1, rand2 = randrange(0, 5), randrange(0, 5)
	query = 'Order-' + flights[rand1] + '-' + days[rand2]
	# query = 'Order-' + flights[0] + '-' + days[0]
	command = 'GET ' + query
	command = command.split()
	connection.request(command[0], command[1])
	rsp = connection.getresponse()
	data_received = rsp.read()
	# print data_received
	# print 'received'
	connection.close()


if __name__ == '__main__':
	start_time = datetime.now();

	threads = [Thread(target = make_query_request) for _ in range(100)]
	other_threads = [Thread(target = make_order_request) for _ in range(100)]
	threads.extend(other_threads)
	# threads = [Thread(target = make_order_request) for _ in range(200)]

	for thread in threads:
		thread.start()
	for thread in threads:
		thread.join()

	# processes = [Process(target = make_query_request) for _ in range(200)]
	# for process in processes:
	# 	process.start()
	# for process in processes:
	# 	process.join()


	end_time = datetime.now();
	print 'Running time: ' + str((end_time - start_time).microseconds) + ' microseconds'
