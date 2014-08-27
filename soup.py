#!/usr/bin/python

from bs4 import BeautifulSoup
import requests

url = "http://en.wikipedia.org/wiki/List_of_colors"
r  = requests.get(url)
data = r.text

soup = BeautifulSoup(data)

#mydivs = soup.findAll("a", { "class" : "mw-redirect" })
rows = soup.findAll("th", style = 'text-align:left; font-weight:normal; text-transform: capitalize;')
for a in rows:

	try:
		color = a.text
		#hex = soup.findAll("td", style = 'border-left:solid 2px #AAA;border-right:solid 1px #AAA;font-family:monospace;')
		hex = a.parent.findAll("td", style = 'border-left:solid 2px #AAA;border-right:solid 1px #AAA;font-family:monospace;')
	#	hex = a.parent.findAll("td")

		hex_val = ""
		for td in hex:
			hex_val =  td.renderContents() 
		print color, "," , hex_val
	except:
		print
#for link in soup.find_all('a'):
#    print(link.get('href'))
