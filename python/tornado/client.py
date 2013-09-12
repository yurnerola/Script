#!/usr/bin/python
import re
import tornado.httpclient


def str_to_dict(body):
	pattern = re.compile('(.*?)=(.*)\n')
	dict={}
	for match in pattern.finditer(body):
		dict[match.group(1)]=match.group(2)
	return dict

def get_dict(hall):
	http_client=tornado.httpclient.HTTPClient()
	try:
		response=http_client.fetch("http://123.103.108.94:18010/fcgi_bin/get_hall_info.fcgi?id="+hall)
	except tornado.httpclient.HTTPError as e:
		print "Error:",e
	#print response.body
	body=response.body
	dict=str_to_dict(body)
	http_client.close()
	return dict

