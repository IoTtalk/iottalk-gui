from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Graph(models.Model):
    proj = models.ForeignKey(Project)

    def __str__(self):
        return 'Graph in Proj {}'.format(self.id, self.proj.name)
