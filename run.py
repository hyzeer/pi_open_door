from gevent import monkey
from threading import Timer
from openDoor import app
from openDoor.utils import *
from gevent.pywsgi import WSGIServer
import os


try:
    pid = os.fork()
    if pid:
        monkey.patch_all()
        http_server = WSGIServer(('0.0.0.0', 8000), app)
        http_server.serve_forever()
    else:
        while True:
            try:
                t = Timer(23.0, stop)
                while is_rolling():
                    if not t.isAlive():
                        t.start()
                if not is_rolling() and t.isAlive():
                    t.cancel()
            except:
                continue
finally:
    stop()
