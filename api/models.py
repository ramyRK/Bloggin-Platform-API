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
    category=models.CharField(choices=category_choices,max_length=255)
    tags=models.JSONField(default=list)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title