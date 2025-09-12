from django.db import models

class News(models.Model):
    CATEGORY_CHOICES = [
        ("jahon", "Jahon"),
        ("uzbekiston", "O'zbekiston"),
        ("sport", "Sport"),
        ("texnika", "Fan-texnika"),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="news_images/", blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="uzbekiston")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

