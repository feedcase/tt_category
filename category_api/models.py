from django.db.models import *


class Categories(Model):
    parent = ForeignKey('self', on_delete=CASCADE, verbose_name='Parent', related_name='children', null=True, blank=True)
    name = CharField(max_length=50, unique=True)
