from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.slug, to_lower=True)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    image = models.ImageField(upload_to='blogs/')
    # description = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.slug)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} created on {self.created_at}"

