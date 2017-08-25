# Deploying-flask-linebot-Heroku-with-PostgreSQL
要修改三個參數:
 - linechatbot.py `YOUR_CHANNEL_ACCESS_TOKEN`
 - linechatbot.py `YOUR_CHANNEL_SECRET`
 - dbModel.py `SQLALCHEMY_DATABASE_URI`
 
 
# SQL
```sql
CREATE TABLE usermessage
(id varchar(50),
user_id varchar(50),
message text,
Birth_Date timestamp );
```

# line message json
```json
{  
   "events":[  
      {  
         "type":"message",
         "replyToken":"aa47089a9d6e47dc8097477exxxxxxxx",
         "source":{  
            "userId":"U9d7b995f148fb32bf23f5f71xxxxxxxx",
            "type":"user"
         },
         "timestamp":1503564161111,
         "message":{  
            "type":"text",
            "id":"659199807xxxx",
            "text":"gmkremge"
         }
      }
   ]
}
```

## 參考資料:
### https://github.com/line/line-bot-sdk-python
### https://github.com/twtrubiks/Deploying-Flask-To-Heroku
