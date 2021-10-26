from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
# Create your models here.



class Post(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    title= models.CharField(max_length=30)
    likes = ArrayField(models.CharField(max_length=200), blank=True, default=list)
    slug= models.SlugField()
    description=models.TextField()
    date_added =  models.DateField(auto_now=True)

    def __str__(self):
        return (self.title)

    class Meta:
        ordering = ['-date_added']
