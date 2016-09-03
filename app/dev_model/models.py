from django.db import models

from proj.models import Graph
from user_func.models import FeatureFunc


class DevModel(models.Model):
    '''
    Device Model
    '''
    name = models.CharField(max_length=255)


class Dev(models.Model):
    '''
    The instance of a Device Model
    '''
    graph = models.ForeignKey(Graph)
    mod = models.ForeignKey(DevModel)


class Feature(models.Model):
    '''
    Device Feature
    '''
    TYPE_CHOICES = (
        ('i', 'input'),
        ('o', 'output'),)

    cate = models.CharField(max_length=255)  # category
    desc = models.TextField()  # description
    func = models.ForeignKey(FeatureFunc)
    mod = models.ManyToManyField(DevModel)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
