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
    '''
        curl -d "{\"type\":\"user_list\",\"uid_list\":[10622,10888,10010]}" http://localhost:8888/post
    '''
    def get(self):
        print self.request.body
        print self.request
    def post(self):
        dic = {}
        dic = eval(self.request.body)
        #self.write(self.request.body)
        uid_list=dic["uid_list"]
        sort_list=dic["uid_list"]
        sort_list.sort()
        for uid in uid_list:
            self.write(str(uid)+"\n")
        for uid in sort_list:
            self.write(str(uid)+"\n")


application = tornado.web.Application([
    (r"/helloworld", MainHandler),
    (r'/user/(.*)',ProfileHandler,dict(database={'Swaroop':'Swaroop@byteofpython.info','Larry':'larry@wall.org','Matsumoto':'matz@ruby-lang.org'})),
    (r'/post',PostHandler),
])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
