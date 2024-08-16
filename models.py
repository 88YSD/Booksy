from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    genre = models.CharField(max_length=50)
    overview = models.TextField(max_length=900)
    cover = models.ImageField(upload_to='book_covers/', blank=True, null=True)

    def __str__(self):
        return self.title

# Create your models here.
