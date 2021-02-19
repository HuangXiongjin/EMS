import redis
import json
import ast
from datetime import datetime
import os
import tornado
from tornado.web import RequestHandler
from tornado.websocket import WebSocketHandler
from tornado.options import define, options, parse_command_line
from tornado.ioloop import IOLoop
import asyncio
import threading
import time
import gc
import datetime

# pool = redis.ConnectionPool(host=constant.REDIS_HOST) #, password=constant.REDIS_PASSWORD,decode_responses=True
from database.connect_db import REDIS_HOST, REDIS_TABLENAME

pool = redis.ConnectionPool(host=REDIS_HOST)
redis_conn = redis.Redis(connection_pool=pool)

clients = dict()

# 设置服务器端口
define("port", default=5002, type=int)

class IndexHandler(RequestHandler):
    def get(self):
        self.render("chat-client.html")

class SendThread(threading.Thread):
    def run(self):
        runcount = 0
        failcount = 0
        asyncio.set_event_loop(asyncio.new_event_loop())
        msg = ''
        # asyncio.set_event_loop(loop)
        while True:

            try:
                oclass = redis_conn.hgetall(REDIS_TABLENAME)
                oc_dict_i_tag = {}
                for oc in oclass:
                    oc_dict_i_tag[returnb(oc)] = returnb(oclass.get(oc))
                json_data = json.dumps(oc_dict_i_tag)
                bytemsg = bytes(json_data,encoding="utf-8")
                for key in clients.keys():
                    clients[key]["object"].write_message(bytemsg)
                runcount = runcount + 1
                time.sleep(2)
            except Exception as e:
                print(e)
                failcount = failcount + 1
                break
            finally:
                pass


class ChatHandler(WebSocketHandler):
    def open(self):
        remote_ip, port = self.request.connection.context.address
        self.id = remote_ip + ":" + str(port)
        clients[self.id] = {"id": self.id, "object": self}  # 保存Session到clients字典中

    def on_message(self, message):
        print("Client %s received a message:%s" % (self.id, message))

    def on_close(self):
        remote_ip, port = self.request.connection.context.address
        if self.id in clients:
            print(clients[self.id])
            del clients[self.id]
        gc.collect()

    def check_origin(self, origin):
        return True  # 允许WebSocket的跨域请求

def strtofloat(f):
    try:
        if f == None or f == "" or f == b'':
            return 0.0
        else:
            return round(float(f), 2)
    except Exception as e:
        print(e)
def returnb(rod):
    if rod == None or rod == "" or rod == b'':
        return rod
    else:
        return rod.decode()


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/socket", ChatHandler),
    ],
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        # debug=True
    )
    SendThread().start()
    parse_command_line()
    app.listen(options.port)
    # 挂起运行
    tornado.ioloop.IOLoop.instance().start()
