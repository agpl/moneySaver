from django.db import models
from datetime import date
# Create your models here.
from django_extensions.db.fields import (
    CreationDateTimeField, ModificationDateTimeField, UUIDField,
)

class Base(models.Model):
    id = models.AutoField(primary_key=True)
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta(object):
        abstract = True

class Ticket(Base):
    place = models.TextField(default='Brak')
    date = models.DateField(blank=False, null=False)
    serial = models.CharField(default='Brak', max_length=50)
    total = models.FloatField(blank=False, null=False)

    def __unicode__(self):
        return "%s %s" % (self.place, self.serial)

class Category(Base):
    name = models.CharField(max_length=50, blank=False, null=False)
    parent = models.ForeignKey('Category', blank=True, null=True)

    def __unicode__(self):
        return self.name

class Item(Base):
    name = models.CharField(blank=False, null=False, max_length=100)
    cost = models.FloatField(blank=False, null=False)
    number = models.FloatField(blank=False, null=False, default=1)
    singleCost = models.FloatField(blank=False, null=False, default=0)
    category = models.ForeignKey(Category)
    ticket = models.ForeignKey(Ticket)

    def __unicode__(self):
        return self.name