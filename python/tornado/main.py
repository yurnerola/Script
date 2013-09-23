# -*- coding: utf-8 -*- 
import tornado.ioloop
import tornado.web
import client
import re
from urllib import unquote

class HallinfoHandler(tornado.web.RequestHandler):
	def get(self):
		arguments={}
		arguments=self.request.arguments
		if arguments.get("hallid",0):
			hallid=arguments["hallid"][0]
			dict=client.get_dict(hallid)
			if dict.get("hall_id",0):

				hall_pwd=dict["hall_pwd"]
				hall_property=int(dict["hall_property"])
				hall_property2=int(dict["hall_property2"])
				str_property=dict["str_property"]
				#pattern=re.compile(r'area:(.*)#(.*)')
				#match=pattern.match(str_property)
				#if match:
				#	hall_city=match.group(1)
				hall_time=unquote(str_property).decode("gbk").encode("utf-8")
				print hall_time

				self.write("房间号："+dict["hall_id"]+"<br/>")
				self.write("CRS所在服务器ID："+dict["gas_id"]+"<br/>")
				self.write("CRS所在服务器IP："+dict["gas_ip"]+"<br/>")
				self.write("<hr/>")

				if hall_property2&0x00000040:
					self.write("房间类型为：好声音"+"<br/>")
					self.write("送礼时间段为："+hall_time+"<br/>")
				elif hall_property2&0x00000080:
					self.write("房间类型为：开心果"+"<br/>")
					self.write("送礼时间段为："+hall_time+"<br/>")
				elif hall_property2&0x00000100:
					self.write("房间类型为：网舞"+"<br/>")
					self.write("送礼时间段为："+hall_time+"<br/>")
				elif hall_property2&0x00000200:
					self.write("房间类型为：同城"+"<br/>")
					#self.write("同城属性为："+hall_city+"<br/>")
					self.write("送礼时间段为："+hall_time+"<br/>")

				else:
					self.write("房间类型：None"+"<br/>")

				self.write("<hr/>")

				if hall_property&0x00000001:
					self.write("是否支持锁：是"+"<br/>")
				else:
					self.write("是否支持锁：否"+"<br/>")


				if hall_property&0x00000002:
					self.write("当前锁状态：已锁；密码为："+hall_pwd+"<br/>")
				else:
					self.write("当前锁状态：未锁"+"<br/>")

				if hall_property&0x00000040:
					self.write("房间是否支持自动锁：是"+"<br/>")
				else:
					self.write("房间是否支持自动锁：否"+"<br/>")

			else:
				self.write("Hall "+hallid+" does't exist.")
		else:
			self.write("Wrong argument")


application = tornado.web.Application([
    (r"/hallinfo", HallinfoHandler),
])

if __name__=="__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
