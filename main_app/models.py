from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Fiber(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
     return self.title

    def get_absolute_url(self):
     return reverse('detail', kwargs={'fiber_id': self.id}) 

class Figurative(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
     return self.title     

     #in python shell f.save() if for fibers and fg.save() is for figurative
    def get_absolute_url(self):
     return reverse('detail', kwargs={'figurative_id': self.id})

class Digital(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
     return self.title 

    def get_absolute_url(self):
     return reverse('detail', kwargs={'digital_id': self.id})