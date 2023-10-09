'''
Author: yangxingchen
Date: 2023-09-23 17:16:06
LastEditors: yangxingchen
LastEditTime: 2023-09-24 11:17:39
Description: 
'''
import uuid
from django.db import models

# Create your models here.


class RelationShip(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    name = models.CharField(max_length=20)

GENDER_CHOICES = (
    ("MALE", "Male"),
    ("FEMAL", "Female"),
    ("UNKNOW", "Unkonw"),
)


class People(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    name = models.CharField(max_length=255)
    b_date = models.DateTimeField(verbose_name="birthday", blank=True, null=True)
    d_date= models.DateTimeField(verbose_name="death day", blank=True, null=True)
    gender = models.CharField(verbose_name="gender", choices=GENDER_CHOICES, 
                              max_length=10,
                              default="UNKNOW")
    father = models.ForeignKey("self", on_delete=models.CASCADE,
                                related_name="l_children", blank=True, null=True,
                                verbose_name="father"
                                )
    mother = models.ForeignKey("self", on_delete=models.CASCADE, related_name="r_children", 
                               blank=True, null=True,
                               verbose_name="mother"
                               )
    def __str__(self) -> str:
        return self.name

class Event(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    name = models.CharField(max_length=255)