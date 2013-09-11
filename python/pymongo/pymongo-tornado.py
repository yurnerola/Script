import tornado.ioloop
import tornado.web
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId


client = MongoClient('mongodb://localhost:27017/')
db=client["test"]
users=db["users"];
class MainHandler(tornado.web.RequestHandler):
    database={}
    def get(self):
        user={"_id":1231,"name":"ttt"}
        db.users.save(user)

class ProfileHandler(tornado.web.RequestHandler):
    def get(self,username):
        user_r= users.find({"name":username})
        if user_r.count():
            for user in user_r:
                print user
        else:
            print  "No Result Found."


class PostHandler(tornado.web.RequestHandler):
    '''
        curl -d "{\"type\":\"user_info_2\",\"user_info\":{\"_id\":123,\"name\":\"Bob D.\"}}" http://localhost:8888/post
    '''
    def get(self):
        print self.request.body
        print self.request
    def post(self):
        dic = {}
        dic = eval(self.request.body)
        #self.write(self.request.body)
        uid_list=dic.get("uid_list",[])
        cursor=users.find({"_id":{"$in":uid_list}})
        user_list_sort=[]
        for user in cursor:
            user_list_sort.append(user)
        user_list=[]
        for id in uid_list:
            for user in user_list_sort:
                if id==user["_id"]:
                    user_list.append(user)
                    break;
        print u"------"
        for i in user_list:
            print i
        

application = tornado.web.Application([
    (r"/helloworld", MainHandler),
    (r'/user/(.*)',ProfileHandler),
    (r'/post',PostHandler),
])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
