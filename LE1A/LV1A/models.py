from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Translator(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    publication_date = models.DateField()
    user_added = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_pages = models.IntegerField()
    book_cover = models.ImageField(upload_to="book_covers/", null=True, blank=True)
    is_available = models.BooleanField(default=True)
    translators = models.ManyToManyField(Translator)

    def __str__(self):
        return self.name


class Rating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    comment = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.book.name} - {self.rating}"
