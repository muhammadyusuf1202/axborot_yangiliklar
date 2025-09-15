from django.db import models
from django.utils import timezone
from datetime import timedelta

class News(models.Model):
    CATEGORY_CHOICES = [
        ('jahon', 'Jahon'),
        ('uzbekiston', "O'zbekiston"),
        ('sport', 'Sport'),
        ('texnika', 'Fan-texnika'),
    ]

    title = models.CharField(max_length=10000)
    content = models.TextField()
    image = models.ImageField(upload_to="news/", blank=True, null=True)
    video = models.FileField(upload_to="news/videos/", blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def is_new(self):
        """3 kundan oshmagan yangiliklar uchun NEW belgisi chiqadi"""
        return timezone.now() - self.created_at <= timedelta(days=3)

    def __str__(self):
        return self.title
