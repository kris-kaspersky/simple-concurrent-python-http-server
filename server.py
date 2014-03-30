import time
import os
import threading
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn

HOST_NAME = 'localhost'
PORT_NUMBER = 8080
file_dir = os.getcwd() + '/serverfiles/'
log = []
logLock = threading.RLock()
flights_schedule = {}

# convert the file into filght dict
def get_flights(filename):
	file_in = open(file_dir + filename)
	flights = {}
	flight_day = []
	flight_time = []
	flight_name = []
	for line in file_in:
		line = line.strip('\n')
		line_list = line.split(',')
		flight_name.append(line_list[0])
		flight_day.append(line_list[1])
		flight_time.append(line_list[2])
	for i in range(0, len(flight_name)):
		flights[flight_name[i]] = {}
	for i in range(0, len(flight_name)):
		flights[flight_name[i]][flight_day[i]] = flight_time[i]
	return flights

# concurrent server
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
	pass

# sequential server
# class ThreadedHTTPServer(HTTPServer):
# 	pass

class eachLog:
	ipaddress = ''
	dateandtime = ''
	requiredfile = ''
        
class MyHandler(BaseHTTPRequestHandler):
	def do_HEADS(self):
		self.send_response(200)
		self.send_header("Content-type", "text-html")
		self.end_headers()

	def do_GET(self):
		# file_dir = 'C:/Dropbox/Courses/Concurrent Programming/project/webserver/files/'
		# f = open(file_dir + self.path)
		self.send_response(200)
		self.send_header("Content-type", "text-html")
		self.end_headers()
		# self.wfile.write("Entered GET request handler --- ")
		# self.wfile.write(f.read())
		query = self.path.split('-')
		self.wfile.write(flights_schedule[query[0]][query[1]])
		time.sleep(1)
		# self.wfile.write("Sending response!")
		# create log
		mylog = eachLog()
		mylog.ipaddress = self.client_address[0]
		mylog.dateandtime = self.log_date_time_string()
		mylog.requiredfile = self.path
		# append log
		logLock.acquire()
		log.append(mylog)
		logLock.release()
                

# test(HandlerClass=<class BaseHTTPServer.BaseHTTPRequestHandler>, ServerClass=<class BaseHTTPServer.HTTPServer>)
# Test the HTTP request handler class. This runs an HTTP server on port 8000
# def test(HandlerClass = SlowHandler, ServerClass = ThreadedHTTPServer):
#       _test(HandlerClass, ServerClass)

if __name__ == '__main__':
	# test()
	# get flight dict
	flights_schedule = get_flights('flights.csv')
	server_class = ThreadedHTTPServer
	# if want to test the sequential http server
	# server_class = HTTPServer
	my_server = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
	try:
		my_server.serve_forever()
	except KeyboardInterrupt:
		print '\n'
		for i in log:
		#print i.ipaddress
			print 'log:'+'  '+i.ipaddress+'  '+i.dateandtime+'  '+i.requiredfile
			#print 'log:'+'  '+i.ipaddress+'  '+i.requiredfile+'\t\n'
	my_server.server_close()
	# print flights_schedule['UA001']['Mon']
