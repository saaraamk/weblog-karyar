from django.db import models

class Author(models.Model):
    user_name = models.CharField(max_length=50)
    bio = models.TextField(unique=True)
    email = models.EmailField()
    created_at = models.DateField()

    def __str__(self) -> str:
        return self.user_name


class Post(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateField(null=True)

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    text = models.TextField()
    created_at = models.DateField(null=True)

    def __str__(self) -> str:
        return f'{self.author}-{self.post}'
    

class Like(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='ulikes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='plikes')

    def __str__(self):
        return f'{self.author} liked {self.post}'

