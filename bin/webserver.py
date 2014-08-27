#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import sys
import pickacolor

PORT_NUMBER = 8001
color = pickacolor.get_random_color()

header="""
<html>
<head>
<style> 
.deadcenter{
    width: 500px;
    height: 200px;
    font-family: Monospace;
    position: absolute;
    top:0;
    bottom: 0;
    left: 0;
    right: 0;
    font-size: 5em;

    margin: auto; 
}
</style>
<script>
function invertColor(hexTripletColor) {
    var color = hexTripletColor;
    color = color.substring(1);           // remove #
    color = parseInt(color, 16);          // convert to integer
    color = 0xFFFFFF ^ color;             // invert three bytes
    color = color.toString(16);           // convert to hex
    color = ("000000" + color).slice(-6); // pad with leading zeros
    color = "#" + color;                  // prepend #
    return color;
}
</script> 
</head>

<body style='background-color:
"""

footer="""
);</script>
 </body></html>
"""


#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		
		color_word = color.split(',')[0]
		color_hex = color.split(',')[1]
		color_hex= color_hex.replace(' ','')
		color_hex = color_hex.rstrip()
		print color
		print color_word
		print color_hex		

		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()

		# Send the html message
		html = header
		html += color_hex
		html += """
		'> <div class='deadcenter' id='color_text'>
		"""
		
		html += str(color_word)
		html += "</div><script>document.getElementById('color_text').style.color=invertColor('%s');</script> </body></html>" % (color_hex)
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
