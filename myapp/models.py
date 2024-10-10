from django.db import models

class OpeningHours(models.Model):
    day_of_week = models.CharField(max_length=10)
    venue = models.CharField(max_length=30)
    opening_time = models.CharField(max_length=30)
    

    def __str__(self):
        return f"{self.day_of_week}, {self.venue}, {self.opening_time}"
# Create your models here.
