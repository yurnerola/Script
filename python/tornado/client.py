#!/usr/bin/python
import sys
import re
import com

from  tornado.httpclient import HTTPClient

http_client=HTTPClient()

def str_to_dict(body):
	pattern = re.compile('(.*)=(.*)\n')
	dict={}
	for match in pattern.finditer(body):
	# 	dict[match.group(1)]=match.group(2)
	# print dict
		print match.group()

if len(sys.argv)<2:
	com.usage()
	exit(0)

try:
	response=http_client.fetch("http://123.103.108.94:18010/fcgi_bin/get_hall_info.fcgi?id="+sys.argv[1])
except httpclient.HTTPError as e:
	print "Error:",e
#print response.body
body=response.body
str_to_dict(body)


http_client.close()

