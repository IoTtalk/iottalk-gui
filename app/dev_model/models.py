from django.db import models

from proj.models import Graph
from user_func.models import FeatureFunc


class DevModel(models.Model):
    '''
    Device Model
    '''
    name = models.CharField(max_length=255)
    desc = models.TextField(null=True, blank=True)  # description

    def __str__(self):
        return '{} {}'.format(self.id, self.name)


class ModelTag(models.Model):
    '''
    Device Model Tag

    for searching, categorizing ... etc.
    '''
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Dev(models.Model):
    '''
    The instance of a Device Model.

    Each instance will be mapped to a card on GUI in graph.
    If user create the instance with both IDF and ODF enabled,
    we will create two ``Dev`` and distinguish them via ``type`` field.
    '''
    TYPE_CHOICES = (
        ('i', 'input'),
        ('o', 'output'),)

    graph = models.ForeignKey(Graph)
    mod = models.ForeignKey(DevModel)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)

    def __str__(self):
        return '{} Model {}'.format(self.id, self.mod.name)


class Category(models.Model):
    '''
    Feature Category
    '''
    name = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.name)


class Feature(models.Model):
    '''
    Device Feature
    '''
    TYPE_CHOICES = (
        ('i', 'input'),
        ('o', 'output'),)

    cate = models.ForeignKey(Category)
    desc = models.TextField(null=True, blank=True)  # description
    func = models.ForeignKey(FeatureFunc)
    mod = models.ManyToManyField(DevModel)
    # to show enabled/disabled on instance
    dev = models.ManyToManyField(Dev)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)

    def __str__(self):
        return '{}df {}'.format(self.type, self.name)
