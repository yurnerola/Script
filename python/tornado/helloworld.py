import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    database={}
    def get(self):
        self.write("Hello, world\n")
        self.write(self.request.arguments)
        self.write("\n")
        self.write(self.request.path+"\n")

class ProfileHandler(tornado.web.RequestHandler):
	def initialize(self,database):
		self.database=database;
		print self.database

	def get(self,username):
		print username
        print self.database

class PostHandler(tornado.web.RequestHandler):
    def get(self):
        print self.request.body
        print self.request
    def post(self):
        dic = {}
        dic = eval(self.request.body)
        #self.write(self.request.body)
        self.write(dic)


application = tornado.web.Application([
    (r"/helloworld", MainHandler),
    (r'/user/(.*)',ProfileHandler,dict(database={'Swaroop':'Swaroop@byteofpython.info','Larry':'larry@wall.org','Matsumoto':'matz@ruby-lang.org'})),
    (r'/post',PostHandler),
])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
