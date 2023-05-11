from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=60)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.title 