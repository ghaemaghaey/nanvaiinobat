from django.db import models

# Create your models here.
class nobat(models.Model):
    id = models.IntegerField(primary_key=True,default=0)
    name = models.CharField(max_length=100,default='nothing')
    amount = models.IntegerField(default=0)
    def __str__(self):
        return str(self.name)