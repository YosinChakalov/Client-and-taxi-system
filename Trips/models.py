from django.db import models

class Trips(models.Model):
    title = models.CharField(max_length=100)
    from_where = models.CharField(max_length=250)
    to_where = models.CharField(max_length=250)
    date = models.DateField(auto_now_add=True)
    seats = models.IntegerField(default=4)
    time = models.IntegerField()
    price = models.IntegerField()
    driver_id = models.ForeignKey("Authenticate.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title