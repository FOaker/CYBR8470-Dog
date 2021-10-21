from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

SIZE_CHOICES = (
    ("TINY", "Tiny"),
    ("SMALL", "Small"),
    ("MEDIUM", "Medium"),
    ("LARGE", "Large"),
)


# Create your models here.
class Breed(models.Model):
    name = models.CharField(max_length=30)
    size = models.CharField(max_length=30, choices=SIZE_CHOICES)
    friendliness = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    trainability = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    sheddingamount = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    exerciseneeds = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])

    def __str__(self):
        return self.name

    # def __int__(self):
    #     return self.friendliness, self.trainability, self.sheddingamount, self.exerciseneeds


class Dog(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    favoritefood = models.CharField(max_length=30)
    favoritetoy = models.CharField(max_length=30)

    # def __str__(self):
    #     return self.name, self.age, self.breed, self.gender, self.color, self.favoritefood, self.favoritetoy
