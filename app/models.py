'''
Author: yangxingchen
Date: 2023-09-23 17:16:06
LastEditors: yangxingchen
LastEditTime: 2023-10-15 15:15:30
Description: 
'''

import uuid
from django.db import models
from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    # If you only inherit GenericUUIDTaggedItemBase, you need to define
    # a tag field. e.g.
    # tag = models.ForeignKey(Tag, related_name="uuid_tagged_items", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class RelationShip(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    name = models.CharField(max_length=20,  verbose_name="关系")
    
    fro = models.ForeignKey("People", on_delete=models.CASCADE,
                                related_name="re_from", blank=True, null=True,
                                verbose_name="from"
                                )
    
    to = models.ForeignKey("People", on_delete=models.CASCADE,
                                related_name="re_to", blank=True, null=True,
                                verbose_name="to"
                                )


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
    brief = models.TextField(verbose_name="简介", blank=True, null=True)
    tags = TaggableManager(through=UUIDTaggedItem)
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
    tags = TaggableManager(through=UUIDTaggedItem)