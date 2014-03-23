import time
import os
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer, test as _test
from SocketServer import ThreadingMixIn

HOST_NAME = 'localhost'
PORT_NUMBER = 80

# concurrent server
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
	pass

# sequential server
# class ThreadedHTTPServer(HTTPServer):
#     pass 

class MyHandler(BaseHTTPRequestHandler):
	def do_HEADS(self):
		self.send_response(200)
		self.send_header("Content-type", "text-html")
		self.end_headers()

	def do_GET(self):
		file_dir = 'C:/Dropbox/Courses/Concurrent Programming/project/webserver/files/'
		f = open(file_dir + self.path)
		self.send_response(200)
		self.send_header("Content-type", "text-html")
		self.end_headers()
		# self.wfile.write("Entered GET request handler --- ")
		self.wfile.write(f.read())
		time.sleep(1)
		self.wfile.write("Sending response!")

# test(HandlerClass=<class BaseHTTPServer.BaseHTTPRequestHandler>, ServerClass=<class BaseHTTPServer.HTTPServer>)
# Test the HTTP request handler class. This runs an HTTP server on port 8000
# def test(HandlerClass = SlowHandler, ServerClass = ThreadedHTTPServer):
# 	_test(HandlerClass, ServerClass)

if __name__ == '__main__':
	# test()
	server_class = ThreadedHTTPServer
	# if want to test the sequential http server
	# server_class = HTTPServer
	my_server = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
	my_server.serve_forever()
