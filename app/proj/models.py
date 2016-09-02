from django.db import models


class Graph(models.Model):
    name = models.CharField(max_length=255)


class Project(models.Model):
    name = models.CharField(max_length=255)
