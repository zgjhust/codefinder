#!/usr/bin/python
# -*- encoding:utf-8 -*-
from flask import Flask, request, render_template, g
from werkzeug.local import LocalProxy
import sae.kvdb
import json
import hashlib
import sys
import time
import xml.etree.ElementTree as ET

app = Flask(__name__)


def get_kv_client():
    kv = getattr(g, '_kvclient', None)
    if kv is None:
        kv = g._kvclient = sae.kvdb.Client()
    return kv

kv = LocalProxy(get_kv_client)


@app.teardown_appcontext
def teardown_kvclient(exception):
    kv = getattr(g, '_kvclient', None)
    if kv is not None:
        kv.disconnect_all()


def init_msg_code(code_file_name):
    with open(code_file_name) as fp:
        codes = json.load(fp)
    for key, value in codes.iteritems():
        utf8_key = key.encode('utf-8')
        if not kv.add(utf8_key, value):
            kv.replace(utf8_key, value)


@app.route("/initdbcode")
def initdbcode():
    code_file_name = 'formatted/codes_db2codes.txt'
    init_msg_code(code_file_name)
    return 'init successful!'


@app.route("/initdbmsg")
def initdbmsg():
    code_file_name = 'codes_db2msg.txt'
    init_msg_code(code_file_name)
    return 'init successful!'


@app.route("/initcics")
def initcics():
    code_file_name = ['formatted/codes_abend.txt', 'formatted/codes_axm.txt',
                      'formatted/codes_dfh1.txt', 'formatted/codes_dfh2.txt',
                      'formatted/codes_eyu.txt']
    for fn in code_file_name:
        init_msg_code(fn)
    return 'init successful!'


@app.route("/initmvs1")
def initmvs1():
    code_file_name = ['formatted/codes_101.txt',
                      'formatted/codes_201.txt',
                      'formatted/codes_301.txt'
                      ]
    for fn in code_file_name:
        init_msg_code(fn)
    return 'init successful!'


@app.route("/initmvs2")
def initmvs2():
    code_file_name = ['formatted/codes_401.txt',
                      'formatted/codes_501.txt',
                      'formatted/codes_601.txt'
                      ]
    for fn in code_file_name:
        init_msg_code(fn)
    return 'init successful!'


@app.route("/initmvs3")
def initmvs3():
    code_file_name = ['formatted/codes_701.txt',
                      'formatted/codes_802.txt',
                      'formatted/codes_902.txt',
                      'formatted/codes_a01.txt'
                      ]
    for fn in code_file_name:
        init_msg_code(fn)
    return 'init successful!'


@app.route("/<code>")
def get_code_description(code):
    # kv = sae.kvdb.Client()
    value = kv.get(code.upper().encode('utf-8'))
    if value is None:
        app.logger.error('key %s not found!', code)
        value = 'key not found'
    return value


@app.route('/weixin/', methods=['GET', 'POST'])
def weixin_textmsg_handler():
    if request.method == 'GET':
        token = 'your weixin token'
        signature = request.args.get('signature', '')
        timestamp = request.args.get('timestamp', '')
        nonce = request.args.get('nonce', '')
        echostr = request.args.get('echostr', '')
        sha1 = hashlib.sha1()
        codelist = [token, timestamp, nonce]
        codelist.sort()
        map(sha1.update, codelist)
        hashcode = sha1.hexdigest()
        app.logger.error(hashcode+':::'+signature)
        if hashcode == signature:
            return echostr
        return False
    if request.method == 'POST':
        xmldata = request.data
        xmlroot = ET.fromstring(xmldata)
        msgType = xmlroot.find('MsgType').text
        fromUser = xmlroot.find('FromUserName').text
        toUser = xmlroot.find('ToUserName').text
        if msgType == 'text':
            content = xmlroot.find('Content').text.strip()
            content = get_code_description(content)
            if len(content) >= 2048:
                ix = content.rfind(' ', 0, 2000)
                content = content[0:ix] + '...'
            try:
                tp = render_template('weixin_msg.xml',
                                     fromUser=toUser,
                                     toUser=fromUser,
                                     createTime=int(time.time()),
                                     content=content)
            except:
                print sys.exc_info()
            return tp
        else:
            content = '''Welcome to GeekSpace!
                        We only support text message for now!'''
            return render_template('weixin_msg.xml',
                                   fromUser=toUser,
                                   toUser=fromUser,
                                   createTime=int(time.time()),
                                   content=content)

if __name__ == "__main__":
    app.run()
