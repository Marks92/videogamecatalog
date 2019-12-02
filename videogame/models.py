from django.db import models

# Create your models here.
class People(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    age = models.IntegerField()
    user_name = models.CharField(max_length=60)
    password = models.CharField(max_length=100)
    confirm_Password = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Genres(models.Model):
    genre_type = models.CharField(max_length=100)

    def __str__(self):
        return self.genre_type

class Games(models.Model):
    game_genre = models.ForeignKey(Genres, on_delete=models.CASCADE)
    game_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.game_name}"
