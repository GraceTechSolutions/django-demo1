from django.db import models

# Create your models here.
class ToDo(models.Model):
    name = models.CharField(max_length=50)
    completed = models.BooleanField()
    
    # date
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name