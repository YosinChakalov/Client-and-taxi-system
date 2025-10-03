from django.db import models

class Trips(models.Model):
    CHOICES = [
        ('available',"AVAAILABLE"),
        ('unavailable',"UNAVAILABLE")
    ]
    title = models.CharField(max_length=100)
    from_where = models.CharField(max_length=250)
    to_where = models.CharField(max_length=250)
    date = models.DateField(auto_now_add=True)
    seats = models.IntegerField(default=4)
    time = models.TimeField()
    price = models.IntegerField()
    available = models.CharField(max_length=60, choices=CHOICES, default='available')
    driver_id = models.ForeignKey("Authenticate.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title