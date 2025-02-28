from django.db import models
from django.urls import reverse


class List(models.Model):
    def get_absolute_url(self):
        return reverse("lists:view_list", args=[self.id])


# Create your models here.
class Item(models.Model):
    text = models.TextField(default='', blank=False)
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)
