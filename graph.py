'''
Author: yangxingchen
Date: 2023-09-24 11:35:06
LastEditors: yangxingchen
LastEditTime: 2023-09-24 11:35:07
Description: 
'''
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hisperson.settings")

django.setup()


from app.models import People

p = People()