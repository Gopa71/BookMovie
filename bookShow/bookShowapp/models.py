from django.db import models

# Create your models here.
class Movies(models.Model):
    name=models.CharField(max_length=250)
    rate=models.CharField( max_length=250)
    photo=models.ImageField(upload_to='mvpic')
    bgphoto=models.ImageField(upload_to='bgppic')
    screen=models.CharField(max_length=50)
    language=models.CharField(max_length=50)
    date_dur=models.CharField(max_length=100)
    desc=models.TextField()

    def __str__(self):
        return self.name