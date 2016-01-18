from slacker import Slacker

import websocket
import yaml
import json
from urllib import parse

with open('secret.txt', 'r') as f:
    API_KEY=f.readline().rstrip())
slack = Slacker(API_KEY)
deets = slack.rtm.start()
# websocket.enableTrace(True)
ws = websocket.WebSocketApp(deets.body['url'])

import re

USER_ID = ''

def on_open(ws):
    print('Open')
    ws.user_id = slack.users.get_user_id('slacktex')
def on_message(ws,message):
    message = yaml.load(message)
    print(message)
    if message['type'] == 'message':
        if message['user'] != ws.user_id:
            if re.match(r'\$[\S\s]+\$', message['text']) is not None:
                corrected = re.sub(r'\\\\',r'\\',message['text'])
                corrected = re.sub(r'\$','',corrected)
                slack.chat.post_message(message['channel'],'Rendered that for you.',
                attachments=json.dumps([{'title':'Equation',
                'image_url':'https://latex.codecogs.com/gif.latex?%5Cdpi%7B300%7D%20%5Cbg_white%20'+corrected}]),
                as_user=True)

ws.on_open = on_open
ws.on_message = on_message
ws.run_forever()
