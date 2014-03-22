import sys
import urllib2

from threading import Thread

def make_request(url):
    print urllib2.urlopen(url).read()

def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    for _ in range(10):
        Thread(target=make_request, args=("http://localhost:%d" % port,)).start()

main()