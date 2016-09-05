from django.db import models


class FuncBase(models.Model):
    name = models.CharField(max_length=255)
    code = models.TextField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class FeatureFunc(FuncBase):
    '''
    Device Feature Function
    '''


class JoinFunc(FuncBase):
    '''
    Join Function
    '''
