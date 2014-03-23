import sys
import httplib
from threading import Thread

IP_ADDRESS = sys.argv[1]

def make_request():
	# print urllib2.urlopen(url).read()
	connection = httplib.HTTPConnection(IP_ADDRESS)
	while True:
		command = raw_input('input command: ')
		command = command.split()
		if command[0] == 'exit':
			break
		connection.request(command[0], command[1])
		rsp = connection.getresponse()
		data_received = rsp.read()
		print data_received
	connection.close()

# def main():
# 	port = 8000
# 	for _ in range(10):
# 		Thread(target = make_request, args = ("http://localhost:%d" % port,)).start()

# main()

make_request()