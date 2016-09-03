from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)


class Graph(models.Model):
    name = models.CharField(max_length=255)
    proj = models.ForeignKey(Project)
