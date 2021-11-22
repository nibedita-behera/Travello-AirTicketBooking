from django.db import models
class Destination(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
