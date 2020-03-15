from django.conf import settings
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify




class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    text = models.TextField()
    tags = TaggableManager()
    created_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True, max_length=255, blank=True)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        #this line below give to the instance slug field a slug name
        self.slug = slugify(self.title)
        #this line below save every fields of the model instance
        super(Post, self).save(*args, **kwargs)    


class Contact(models.Model):
    email = models.EmailField(blank=False)
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=50000)
    created_date = models.DateTimeField(default=timezone.now)
    