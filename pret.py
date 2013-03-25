# Pret.py
import logging
import tornado.httpserver
import tornado.web
import tornado.websocket
import tornado.ioloop
import tornado.gen

import tornadoredis
from User import User
import Admin

c = tornadoredis.Client()
c.connect()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", title="Pret- Using redis to creat user login system")

class NewMessage(tornado.web.RequestHandler):
    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        password2 = self.get_argument('password2')
        """
        c.publish('test_channel', username)
        c.publish('test_channel', password)
        c.publish('test_channel', password2)
        """
        self.set_header('Content-Type', 'text/plain')
        self.write('sent: %s' % (username,))

class MessagesCatcher(tornado.websocket.WebSocketHandler):
    def __init__(self, *args, **kwargs):
        super(MessagesCatcher, self).__init__(*args, **kwargs)
        self.listen()

    @tornado.gen.engine
    def listen(self):
        self.client = tornadoredis.Client()
        self.client.connect()
        yield tornado.gen.Task(self.client.subscribe, 'test_channel')
        self.client.listen(self.on_message)

    def on_message(self, msg):
        logging.info(msg)
        if msg.kind == 'message':
            self.write_message(str(msg.body))

        if msg.kind == 'disconnect':
            # Do not forget to restart a listen loop
            # after a successful reconnect attempt.

            # Do not try to reconnect, just send a message back
            # to the client and close the client connection
            self.write_message('The connection terminated '
                               'due to a Redis server error.')
            self.close()

    def on_close(self):
        if self.client.subscribed:
            self.client.unsubscribe('test_channel')
            self.client.disconnect()

application = tornado.web.Application([
    (r'/', MainHandler),
    (r'/msg', NewMessage),
    (r'/track', MessagesCatcher),
])

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    print 'Demo is runing at 0.0.0.0:8888\nQuit the demo with CONTROL-C'
    tornado.ioloop.IOLoop.instance().start()
"""
next step
how to extract whole information from table
and store into redis
"""
