import datetime

from django.db import models
from django.db.models import Count
from django.db.models.functions import Coalesce


class Timepass(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(date__lt=datetime.datetime.now())


class Notask(models.Manager):
    def with_counts(self):
        return self.annotate(num_responses=Coalesce(models.Count("category_id"), 0))


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, default='salam')
    date = models.DateTimeField()
    objects = models.Manager()
    timepass = Timepass()
    notask = Notask()

    def __str__(self):
        return self.title
