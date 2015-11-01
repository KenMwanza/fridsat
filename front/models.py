from django.db import models
from django.db.models import Count
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager

class BusinessVoteCountManager(models.Manager):
    def get_queryset(self):
        return super(BusinessVoteCountManager,
self).get_queryset().annotate(
        votes=Count('vote')).order_by('-rank_score', '-votes')

class Business(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200, unique=True)
    category = models.CharField(max_length=50, blank=False, null=False)
    county = models.CharField(max_length=20)
    area = models.CharField(max_length=80, blank=True, null=True)
    street_address = models.CharField(max_length=100)
    email = models.EmailField(max_length=70, blank=True)
    phone_number = models.CharField(max_length=25, blank=True)
    description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='documents/%Y/%m/%d',  blank=True, null=True)
    slug = models.SlugField(max_length=1000, blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    rank_score = models.FloatField(default=0.0)

    with_votes = BusinessVoteCountManager()
    objects = models.Manager() #default manager

    tags = TaggableManager()


    class Meta:
        verbose_name_plural = "businesses"

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)

        super(Business, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return "/%s/" % (self.slug)

class County(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name_plural = "counties"

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)

        super(County, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return "/county/%s/" % (self.slug)

class Area(models.Model):
    name = models.CharField(max_length=80, unique=True)
    county = models.ForeignKey(County)
    slug = models.SlugField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)

        super(Area, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return "/county/%s/%s/" % (self.county.slug, self.slug)

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=1000, blank=True, null=True)
    icon = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        verbose_name_plural = "categories"

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)

        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return "/category/%s/" % (self.slug)

class CustomBusinessGroup(models.Model):
    name = models.CharField(max_length=200, unique=True)
    about = models.TextField()
    slug = models.SlugField(max_length=1000, blank=True, null=True)

    tags = TaggableManager()

    class Meta:
        verbose_name = "custom business group"
        verbose_name_plural = "custom business groups"

    def __unicode__(self):
        return self.name
            
    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)

        super(CustomBusinessGroup, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return self.slug