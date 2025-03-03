from django.db import models

# Create your models here.
class post (models.Model):
    category_choices=[
        ('Technology','Technology'),
        ('Sports','Sports'),
        ('Education','Education'),
        ('Health','Health'),
    ]

    title= models.CharField(max_length=255)
    content=models.TextField()
    category=models.CharField(choices=category_choices)
    tags=models.JSONField(default=list)