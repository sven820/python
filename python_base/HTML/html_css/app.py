__author__ = "JJ.sven"

import tornado.web
from tornado import ioloop

class MainHandle(tornado.web.RequestHandler):
    def get(self):
        self.__login()


    def post(self, *args, **kwargs):
        self.__login()

    '''==========private=========='''
    def __login(self):
        name = self.get_argument('user')
        pwd = self.get_argument('pwd')
        print(name, pwd)
        if name=='jxf' and pwd=='123':
            self.write('success')
        else:
            self.write('fail')


application = tornado.web.Application([
    (r'/index', MainHandle),
])

if __name__ == '__main__':
    application.listen(9090, address='localhost')
    ioloop.IOLoop.instance().start()