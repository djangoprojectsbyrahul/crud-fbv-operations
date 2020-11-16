from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Beer(models.Model):
    brand = models.CharField(max_length=128)
    taste = models.CharField(max_length=128)
    color = models.CharField(max_length=64)
    price = models.FloatField()

    def __str__(self):
        return self.brand

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
