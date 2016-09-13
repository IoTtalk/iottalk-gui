from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    @property
    def json(self):
        return {
            'pk': self.pk,
            'name': self.name,
        }


class Graph(models.Model):
    proj = models.ForeignKey(Project)

    def __str__(self):
        return 'Graph in Proj {}'.format(self.id, self.proj.name)

    @property
    def json(self):
        return {
            'pk': self.pk,
            'input': tuple(dev.pk for dev in self.dev_set.filter(type='o')),
            'output': tuple(dev.pk for dev in self.dev_set.filter(type='i')),
        }
