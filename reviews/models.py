from django.db import models
from django.contrib.auth.models import User
from front.models import Business

class Vote(models.Model):
    voter = models.ForeignKey(User)
    business = models.ForeignKey(Business)

    def __unicode__(self):
        return "%s upvoted %s" % (self.voter.username, self.business.name)