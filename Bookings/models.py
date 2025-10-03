from django.db import models

class Bookings(models.Model):
    CHOICES = (
        ('active', 'Active'),
        ('cancelled', 'Cancelled')
    )

    trip = models.ForeignKey("Trips.Trips", on_delete=models.CASCADE)
    user = models.ForeignKey("Authenticate.User", on_delete=models.CASCADE)
    seats_quantity = models.IntegerField()
    status = models.CharField(max_length=10,choices=CHOICES, default='active')