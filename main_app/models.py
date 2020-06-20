from django.db import models

class Fiber(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)

    def __str__(self):
     return self.title

class Figurative(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)

    def __str__(self):
     return self.title     

     #in python shell f.save() if for fibers and fg.save() is for figurative

class Digital(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)

    def __str__(self):
     return self.title 