from django.db import models
from PIL import Image
# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
class scientist(models.Model):
    img2=models.ImageField(upload_to='pics')
    dt=models.DateTimeField()
    name=models.CharField(max_length=250)
    desc=models.TextField()
def __str__(self):
    return self.name