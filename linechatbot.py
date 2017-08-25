# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 10:54:15 2017

@author: goingcosme20
"""

from flask import Flask, request, abort
from dbModel import *
from datetime import datetime

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import json

app = Flask(__name__)

#
line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
#
handler = WebhookHandler('YOUR_CHANNEL_SECRET')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    bodyjson=json.loads(body)
    #app.logger.error("Request body: " + bodyjson['events'][0]['message']['text'])
    app.logger.error("Request body: " + body)
    
    #insertdata
    add_data = usermessage(
            id = bodyjson['events'][0]['message']['id'],
            user_id = bodyjson['events'][0]['source']['userId'],
            message = bodyjson['events'][0]['message']['text'],
            birth_date = datetime.fromtimestamp(int(bodyjson['events'][0]['timestamp'])/1000)
        )
    db.session.add(add_data)
    db.session.commit()
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()