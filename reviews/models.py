from django.db import models
from django_comments.models import Comment

class CommentWithTitle(Comment):
	title = models.CharField(max_length=300)
# Create your models here.
