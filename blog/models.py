from django.db import models
from datetime import datetime
from django.conf import settings
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Categories'

  
class Author(models.Model):
    author = models.CharField(max_length=100)
    author_slug = models.SlugField(max_length=150, allow_unicode=True, null=True, blank=True)
    author_image = models.ImageField(upload_to = "user_images")

    def __str__(self):
        return self.author

    def get_absolute_url(self):
        return reverse('author_blogs', kwargs={'slug':self.author_slug})
    
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"


class Blog (models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, allow_unicode=True, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to = "blog_images",null=True,blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    desc = models.TextField()
    read_count = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
   
    def __str__(self) -> str:
        return f'id: {self.id} -- Blog by {self.title}'
    
    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug':self.slug})
        
    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        


class Comment (models.Model):
    name=models.CharField(max_length=50)
    date=models.DateTimeField(auto_now_add=True)
    email=models.EmailField()
    comment = models.TextField()
    blog= models.ForeignKey(Blog, related_name='comments',  on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name="Comment"
        verbose_name_plural="Comments"

    def __str__(self):
        return f' Comment by  {self.name}'
    





