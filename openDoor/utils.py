from threading import Thread
from .config import *
from openDoor.models import *
from datetime import datetime, timedelta
import RPi.GPIO as GPIO
import time
import hashlib
import uuid
import os


GPIO.setmode(GPIO.BCM)
GPIO.setup(pin['up'], GPIO.OUT)
GPIO.setup(pin['down'], GPIO.OUT)
GPIO.setup(pin['ctrl'], GPIO.OUT)
GPIO.setup(pin['led'], GPIO.OUT)
GPIO.output(pin['up'], action['off'])
GPIO.output(pin['down'], action['off'])
GPIO.output(pin['ctrl'], action['on'])
GPIO.output(pin['led'], False)


def rolling_up():
    GPIO.output(pin['ctrl'], action['off'])
    GPIO.output(pin['down'], action['off'])
    GPIO.output(pin['up'], action['on'])


def rolling_down():
    GPIO.output(pin['ctrl'], action['off'])
    GPIO.output(pin['up'], action['off'])
    GPIO.output(pin['down'], action['on'])


def stop():
    GPIO.output(pin['up'], action['off'])
    GPIO.output(pin['down'], action['off'])
    GPIO.output(pin['ctrl'], action['on'])


def is_rolling():
    time.sleep(0.1)
    down_status = 'gpio -g read {}'.format(pin['down'])
    up_status = 'gpio -g read {}'.format(pin['up'])
    exe_down = os.popen(down_status)
    exe_up = os.popen(up_status)
    down = not bool(int(exe_down.read().replace('\n', '')))
    up = not bool(int(exe_up.read().replace('\n', '')))
    return down or up


# def new_threading(func):
#     def wrap():
#         t = Thread(target=func)
#         return t.start()
#     return wrap


def authenticated(usr, psw):
    password = hashlib.sha256(psw.encode('utf-8')).hexdigest()
    return User.query.filter_by(username=usr, password=password).first()


def make_cookie(usr):
    sessionid = str(uuid.uuid1())
    data = usr.username
    expire = datetime.now().timestamp() + SESSION_DURATION
    s = Session(session=sessionid, data=data, expire=expire)
    db.session.add(s)
    db.session.commit()
    return s
