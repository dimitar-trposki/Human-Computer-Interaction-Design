from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Pilot(models.Model):
    RANK_CHOICES = [
        ("J", "Junior"),
        ("I", "Intermediate"),
        ("S", "Senior"),
    ]

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    year_born = models.IntegerField()
    total_flight_hours = models.DecimalField(max_digits=5, decimal_places=2)
    rank = models.CharField(max_length=100, choices=RANK_CHOICES)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Balloon(models.Model):
    TYPE_CHOICES = [
        ("S", "Small balloon"),
        ("M", "Medium balloon"),
        ("L", "Large balloon"),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    manufacturer = models.CharField(max_length=100)
    max_passengers = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.manufacturer}"


class Airline(models.Model):
    name = models.CharField(max_length=100)
    year_founded = models.IntegerField()
    outside_Europe = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.year_founded}"


class PilotAirLine(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.airline} {self.pilot}"


class Flight(models.Model):
    code = models.CharField(max_length=100, unique=True)
    airport_take_off = models.CharField(max_length=100)
    airport_landing = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='flight_images/', null=True, blank=True)
    balloon = models.ForeignKey(Balloon, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code} {self.airport_take_off}-{self.airport_landing}"
