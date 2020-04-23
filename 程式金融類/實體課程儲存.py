#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 13:27:58 2020

@author: ivan
"""

#登入mongodb
from pymongo import MongoClient
import urllib.parse
import datetime
import pandas as pd

#db setting
username = urllib.parse.quote_plus('ivan8425982dsgare')
password = urllib.parse.quote_plus('h2d8d2t8r54fd5w8s5')
dbname='login'
collection='login'

client = MongoClient('mongodb://%s:%s@35.188.123.248:26003/%s?authMechanism=SCRAM-SHA-1' % (username, password,dbname))
#select db
db = client[collection]
coll = db['offline_class']

#--- 線下課程
className=['用Python打造股票行動機器人',
            '手把手打造輿情監控機器人',
           'Python機器學習商務實戰',
           'RFM顧客分類大師：用Python 打造客群地圖，走向獲利最大化',
           'Python X RFM會員分析戰情室【週間班】：新增視覺化互動網頁＆零售業與運輸業實戰案例分析',
           'Python 0 到 1 基礎商業分析實戰',
           'Python 0 到 1 連續性製程分析實戰',
           'Python 行銷策略分析實戰',
           '🎯AI行銷學：原來 Python 可以這樣用 🎯',
           '全台首創最多商務應用的 Python 0 到 1 基礎課程'
           ]
note=['2020年 4/18-19','2020年 5/30 - 31','2020年 5/16 - 17','2020年 5/9 - 10','2020年','2020年 4/25 - 26',
      '2020年 4/11-12','2020年 3/28-29','2020年 3/21','2020年']
url=['https://tmrgood.kktix.cc/events/stockbot0418-19',
     'https://tmrgood.kktix.cc/events/tmrchatbot0530-31',
     'https://tmrgood.kktix.cc/events/pythonml202001',
     'https://tmrgood.kktix.cc/events/rfm0509-10',
     'https://tmrgood.kktix.cc/events/rfm0429weekday',
     'https://tmrgood.kktix.cc/events/python0to10425-26',
     'https://tmrgood.kktix.cc/events/pythonprocess2020',
     'https://tmrgood.kktix.cc/events/pythonstp20200411-12',
     'https://tmrgood.kktix.cc/events/aimarketing-talk0321',
     'https://tmrgood.kktix.cc/events/python0to1weekday'

     ]
image=['https://i.imgur.com/3fCCj1K.png',
       'https://i.imgur.com/19F5Qu2.png',
       'https://i.imgur.com/PZMhjec.png',
       'https://i.imgur.com/MElpNzt.png',
       'https://i.imgur.com/MElpNzt.png',
       'https://i.imgur.com/dF8otcs.png',
       'https://i.imgur.com/gtRIBhh.png',
       'https://i.imgur.com/gtRIBhh.png',
       'https://i.imgur.com/gtRIBhh.png',
       'https://i.imgur.com/gtRIBhh.png']
for i in range(len(className)):
    coll.insert({'className':className[i],
                 'note':note[i],
                  'url':url[i],
                  'image':image[i],
                  'classType':'實體',
                  'sort':i,
                  "date_info": datetime.datetime.utcnow()
                  })


classData = list(coll.find().sort('sort')) #取得所有資料





#--- 線上課程
coll = db['online_class']
className=['Python 0 到 1 商業數據分析',
            '股票小秘書',
           '用 Python 機器學習創造商業新價值',
           'Word課程 A系列',
           'Word課程 B+C系列'
           ]
note=['','','','','']
url=['https://hahow.in/cr/python0-1',
     'https://hahow.in/cr/stock-secretary',
     'https://hahow.in/cr/python-ml',
     'https://hahow.in/cr/tmr-word1',
     'https://hahow.in/cr/tmr-word2'

     ]
image=['https://i.imgur.com/gtRIBhh.png',
       'https://i.imgur.com/3fCCj1K.png',
       'https://i.imgur.com/A6Oy4pr.png',
       'https://i.imgur.com/dvgvUoV.png',
       'https://i.imgur.com/aOu7Ctd.png']
for i in range(len(className)):
    coll.insert({'className':className[i],
                 'note':note[i],
                  'url':url[i],
                  'image':image[i],
                  'classType':'線上',
                  'sort':i,
                  "date_info": datetime.datetime.utcnow()
                  })