from django.db import models
from django.utils import timezone
# Create your models here.



class Ad(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    price = models.IntegerField(default=0,null=True)
    rooms = models.CharField(max_length=20, null=True)
    surface = models.CharField(max_length=20,null=True)
    floor = models.CharField(max_length=20, default=0,null=True)
    localization = models.CharField(max_length=100, null=True, )
    latitude = models.CharField(max_length=100, null=True, )
    longitude = models.CharField(max_length=100, null=True, )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title