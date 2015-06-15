from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=10, blank=True, null=True)
    brand = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)

class Brand(models.Model):
    name = models.CharField(max_length=20)

class County(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name_plural = "counties"

    def __unicode__(self):
        return self.name
