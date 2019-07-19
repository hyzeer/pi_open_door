from flask import render_template, request, jsonify, make_response, url_for, redirect
from openDoor import app, db, models, config
from openDoor.utils import *
import os
import time
import hashlib
import json


@app.before_request
def login_validate():
    if request.path == '/login':
        return None
    if request.path.rsplit('/', 1)[0] in config.STATIC_FILE_URLS:
        return None
    if request.path in config.REQUIRED_LOGIN_URLS:
        session = request.cookies.get('session')
        if session:
            result = Session.query.filter_by(session=session)
            if result:
                return None
    return redirect('/login')


@app.route('/', methods=['GET'])
def board_get():
    return render_template('board.html')


@app.route('/', methods=['POST'])
def board_post():
    data = json.loads(request.get_data(as_text=True))
    if data['action'] == 'up':
        rolling_up()
    if data['action'] == 'down':
        rolling_down()
    if data['action'] == 'stop':
        stop()
    return jsonify({'msg': '成功'})


@app.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    user = authenticated(username, password)
    if user != None:
        resp = make_response(redirect(url_for('board_get')))
        cookie = make_cookie(user)
        print(cookie.expire)
        resp.set_cookie(key='session', value=cookie.session, expires=cookie.expire)
        return resp
    else:
        return render_template('login.html')


@app.route('/user/add', methods=['GET'])
def add_user():
    username = request.args.get('username')
    password = hashlib.sha256(request.args.get('password').encode('utf-8')).hexdigest()
    u = models.User(username=username, password=password)
    db.session.add(u)
    db.session.commit()
    return jsonify({'msg': '注册成功'})
