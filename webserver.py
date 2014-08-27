#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import sys
import pickacolor

PORT_NUMBER = 8001
color = pickacolor.get_random_color()

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		
		color_word = color.split(',')[0]
		color_hex = color.split(',')[1]
		print color
		print color_word
		print color_hex		

		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		# Send the html message
		html = "<html><body style='background-color: %s '>" % str(color_hex)
		html += str(color_word)
		html += "</body></html>"
		self.wfile.write(html)
		return

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
