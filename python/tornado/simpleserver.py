import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
class StoryHandler(tornado.web.RequestHandler):
	def get(self,story_id):
		self.write("You requested the story "+story_id+".")
class PostHandler(tornado.web.RequestHandler):
	def get(self):
		self.write('<html><body><form action="/post" method="post">'
			'<input type="text" name="message">'
			'<input type="submit" value="Submit">'
			'</form></body></html>')
	def post(self):
		self.set_header("Content-Type","text/plain")
		self.write("You wrote "+self.get_argument("message"))
class ErrorHandler(tornado.web.RequestHandler):
	def get(self):
		raise tornado.web.HTTPError(403)

application = tornado.web.Application([
    (r"/", MainHandler),
	(r"/story/([0-9]+)",StoryHandler),
	(r"/post",PostHandler),
	(r"/error",ErrorHandler)
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
