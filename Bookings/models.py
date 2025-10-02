from django.db import models

class Bookings(models.Model):
    trip_id = models.ForeignKey("Trips.Trips", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    user_id = models.ForeignKey("Authenticate.User", on_delete=models.CASCADE)
