from django.db import models

# Create your models here.
class feedbackdata(models.Model):
    name=models.CharField(max_length=100)
    rating = models.IntegerField()
    date= models.DateTimeField(max_length=100)
    feedback=models.TextField(max_length=100)





