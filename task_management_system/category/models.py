from django.db import models
# from task.models import Task 

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    # task = models.ManyToManyField(Task)

    def __str__(self):
        return self.category_name
    
    
