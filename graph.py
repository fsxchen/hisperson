'''
Author: yangxingchen
Date: 2023-09-24 11:35:06
LastEditors: yangxingchen
LastEditTime: 2023-09-24 11:35:07
Description: 
'''
import os
import django

from py2neo import Node, Relationship, Graph, NodeMatcher, RelationshipMatcher#导入我们需要的头文件

from asset import People, Event

user     = "neo4j"            # your user name
password = "111qqq..."

G = Graph('http://localhost:7474',auth=('neo4j',password), name="neo4j")









os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hisperson.settings")

django.setup()


from app.models import People

for p in People.objects.all():
    print(p)