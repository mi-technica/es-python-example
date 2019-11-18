#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: index.py
# Project: es-python-example
# File Created: Sunday, 17th November 2019 8:18:37 pm
# Author: Jaseem Jas (jaseem@socialanimal.com)
# -----
# Last Modified: Sunday, 17th November 2019 8:43:34 pm
# Modified By: Jaseem Jas (jaseem@socialanimal.com)
# -----
# Copyright 2016 - 2019 Socialanimal.com
###

from elasticsearch import Elasticsearch

import datetime

es = Elasticsearch()

titles = [
  { "index": { "_index": 'titles', "_id": 1 } },
  {
    "id": 1,
    "title": 'Traditional Marketing Vs Digital Marketing',
    "author": 'eCommerce FAQs',
    "date": "2019-11-17T11:39:17.376Z"
  },
  { "index": { "_index": 'titles', "_id": 2 } },
  {
    "id": 2,
    "title": 'Global Digital Marketing Courses Market 2019 Business Strategies ',
    "author": 'Coursera',
    "date": "2019-11-17T11:39:17.376Z"
  },
  { "index": { "_index": 'titles', "_id": 3 } },
  {
    "id": 3,
    "title": 'Big Data vs Data Warehouse',
    "author": 'Igor',
    "date": "2019-11-17T11:39:17.376Z"
  },
  { "index": { "_index": 'titles', "_id": 4 } },
  {
    "id": 4,
    "title": 'Traditional Marketing Vs Digital Marketing',
    "author": 'eCommerce FAQs',
    "date": "2019-11-17T11:39:17.376Z"
  },
  { "index": { "_index": 'titles', "_id": 5 } },
  {
    "id": 5,
    "title": 'Cloudera Data Platform gives big data users multi-cloud path',
    "author": 'Erpinnews',
    "date": "2019-11-17T11:39:17.376Z"
  },
  { "index": { "_index": 'titles', "_id": 6 } },
  {
    "id": 6,
    "title": 'IoT Event Blog Affinity IoT',
    "author": 'infoMegan Davis',
    "date": "2019-11-17T11:39:17.376Z"
  },
  { "index": { "_index": 'titles', "_id": 7 } },
  {
    "id": 7,
    "title": 'Cloud to cloud backup Solutions Archives',
    "author": 'Michael Schneider',
    "date": "2019-11-17T11:39:17.376Z"
  },
  { "index": { "_index": 'titles', "_id": 8 } },
  {
    "id": 8,
    "title": 'Car hire with car insurance',
    "author": 'Gary Hunter',
    "date": "2019-11-17T11:39:17.376Z"
  },
  { "index": { "_index": 'titles', "_id": 9 } },
  {
    "id": 9,
    "title": 'Fashion Jobs and Fashion Career Advice',
    "author": 'Randy C. Marque',
    "date": "2019-11-17T11:39:17.376Z"
  },
  { "index": { "_index": 'titles', "_id": 10 } },
  {
    "id": 10,
    "title": 'Fashion Designer Zac Posen is Shutting Down his Fashion Label',
    "author": 'MARCY OSTER, JTA',
    "date": "2019-11-17T11:39:17.376Z"
  }
]

def createTitles(body):
    try:
        resp = es.bulk(index="titles", body=body)
    except Exception  as e:
        print(e)


createTitles(titles)

def countTitles():
    try:
        resp = es.count(index="titles")
        print(resp)
    except Exception as e:
        print(e)


# countTitles()

def getTitle(id):
    try:
        resp = es.get(index="titles", id=id)
        print(resp)
    except Exception as e:
        print(e)

getTitle(11)     

def updateTitle(body):
    try:
        resp = es.update(index="titles", id=10, body=body)
        print(resp)
    except Exception as e:
        print(e)   


data = {
    "doc": {
        "title": "My own title",
        "author": "JaseemJas",
        "date": datetime.datetime.now()
    }
}

# updateTitle(data)

def deleteTitle(id):
    try:
        resp = es.delete(index="titles", id=id)
    except Exception as e:
        print(e)

# deleteTitle(10)      
# 
def searchTitles(body):
    try:
        resp = es.search(index="titles", body=body)
        print(resp)
    except Exception as e:
        print(e)  

query = {
    "query":{
        "match": {
            "title": "big data"
        }
    }
}        

# searchTitles(query)

def createTitle(body):
    try:
        resp = es.create(index="titles", id=11, body=body)
    except Exception as e:
        print(e)


body = {
    "title": "My new title",
    "author": "JaseemJas",
    "date": datetime.datetime.now()
}

# createTitle(body)