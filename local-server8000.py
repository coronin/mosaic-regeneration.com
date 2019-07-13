#!/usr/bin/env python

#### https://stackoverflow.com/questions/10607621/a-simple-website-with-python-using-simplehttpserver-and-socketserver-how-to-onl

import SimpleHTTPServer
import SocketServer
import os.path
import sys

class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):            
        possible_name = self.path.strip("/")+'.html'
        if self.path == '/':
            # default routing, change index.html if needed
            self.path = '/index.html'
        elif os.path.isfile(possible_name):
            # extensionless page serving
            self.path = possible_name
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyRequestHandler

port = 8000
if len(sys.argv) > 1:
    try:
        p = int(sys.argv[1])
        port = p
    except ValueError:
        print 'port value provided must be an integer'

print "serving on port {0}".format(port)
server = SocketServer.TCPServer(('0.0.0.0', port), Handler)
server.serve_forever()
