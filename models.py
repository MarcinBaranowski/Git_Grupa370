# coding=utf-8
from google.appengine.ext import db
import logging

def article_key(name="default"):
    return db.Key.from_path("articles",name)

class Article(db.Model):
    image = db.BlobProperty(required=False)
    title=db.TextProperty(required=True)
    skladniki=db.TextProperty(required=True)
    content=db.TextProperty(required=True)
    created=db.DateTimeProperty(auto_now_add=True)
    modified=db.DateTimeProperty(auto_now=True)
    
    @classmethod
    def by_key(cls,key):
        logging.info("DB QUERY"+key)        
        article=db.get(db.Key.from_path('Article',key,parent=article_key()))
        return article
