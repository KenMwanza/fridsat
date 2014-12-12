from django.db import models

class Device(models.Model):
    name = models.TextField()
    category = models.TextField(blank=True, null=True)
    brand = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
