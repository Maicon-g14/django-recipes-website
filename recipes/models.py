from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    ingredients = models.TextField()
    directions = models.TextField()
    final_considerations = models.TextField()

    image = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("recipe-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title