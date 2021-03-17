from django.db import models

# Create your models here.

class Task(models.Model):
    task_title = models.CharField(max_length=250)
    task_description = models.TextField()
    status =models.BooleanField(default=True)

    def __str__(self):
       return self.task_title

