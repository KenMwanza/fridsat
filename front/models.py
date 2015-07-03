from django.db import models

class Business(models.Model):
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=50, blank=False, null=False)
    county = models.CharField(max_length=20)
    street_address = models.CharField(max_length=100)
    email = models.EmailField(max_length=70,blank=True)
    phone_number = models.CharField(max_length=25, blank=True)
    description = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

class County(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name_plural = "counties"

    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __unicode__(self):
        return self.name