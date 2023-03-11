from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

from ckeditor.fields import RichTextField

class Blog(models.Model):
    cover = models.ImageField(upload_to=f'blogImage/', blank=True)
    title = models.CharField(max_length=500, blank=False)
    en_title = models.CharField(max_length=500, blank=False)
    released_date = models.DateTimeField(auto_now=True)
    body = RichTextField()
    en_body = RichTextField()
    meta_description = models.CharField(max_length=100)
    en_meta_description = models.CharField(max_length=100)

class BlogComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog = models.ForeignKey("Blog", on_delete=models.CASCADE)
    user_rate = models.FloatField(null=True, default=5, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    commenter_name = models.CharField(max_length=200)
    commenter_email = models.EmailField()
    comment = models.TextField()
    date = models.DateField(auto_now=True)