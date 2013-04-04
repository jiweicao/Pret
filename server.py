import logging
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import tornado.escape
import os

from Pret import Pret
from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/ws", SocketHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
            )
        tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class SocketHandler(tornado.websocket.WebSocketHandler):
    machine = Pret()
    machine.start()

    def open(self):
        pass

    def query_result_got(self, message):
        msg = {}
        msg["command"] = "result"
        msg["arg"] = result
        try:
            self.write_message(msg)
        except:
            logging.error("Error sending message", exc_info=True)

    def on_message(self, message):
        logging.info("got message %r", message)
        parsed  = tornado.escape.json_decode(message)
        if parsed["command"] == "search":
            SocketHandler.machine.search(parsed["query"], self.query_result_got)
            
    def on_close(self):
        SocketHandler.machine.close()

def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
