import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world\n")
        self.write(self.request.arguments)
        self.write("\n")
        self.write(self.request.path+"\n")


application = tornado.web.Application([
    (r"/helloworld", MainHandler),
])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
