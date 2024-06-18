from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateField(null=True)

    def __str__(self) -> str:
        return self.title

