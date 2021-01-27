from django.db.models import *


class Categories(Model):
    parent = ForeignKey('self',
                        on_delete=CASCADE,
                        related_name='children',
                        null=True,
                        blank=True)
    name = CharField(max_length=50,
                     unique=True)


class Siblings(Model):
    parent_id = OneToOneField(Categories,
                              to_field='parent',
                              primary_key=True,
                              db_column='parent_id',
                              on_delete=CASCADE,
                              unique=True),
    siblings = ForeignKey(Categories, to_field='id',
                          on_delete=CASCADE,
                          related_name='siblings')
