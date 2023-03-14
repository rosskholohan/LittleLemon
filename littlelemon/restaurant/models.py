from django.db import models

class MenuItem(models.Model):
    id        = models.IntegerField(primary_key = True)
    title     = models.CharField(max_length = 255)
    price     = models.DecimalField(max_digits = 10, decimal_places = 2)
    inventory = models.IntegerField()
    
    def __str__(self):
        return self.title

class Booking(models.Model):
    id          = models.IntegerField(primary_key = True)
    name        = models.CharField(max_length = 255)
    num_guests  = models.IntegerField()
    BookingDate = models.DateTimeField()

    def __str__(self):
        return self.name


