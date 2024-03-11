from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.urls import reverse



class Post(models.Model):
    title = models.CharField(max_length=120)
    slug = AutoSlugField(populate_from='title')
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('singolo', kwargs={'id': self.id, 'slug': self.slug})