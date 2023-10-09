'''
Author: yangxingchen
Date: 2023-09-23 17:16:06
LastEditors: yangxingchen
LastEditTime: 2023-09-23 17:37:26
Description: 
'''
from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import RelationShip, People, Event

admin.site.register(RelationShip)
admin.site.register(People)
admin.site.register(Event)