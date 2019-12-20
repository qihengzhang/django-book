from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.FloatField(default=0)

    def __str__(self):
        return "<Users:({id},{name},{author},{price})>".format(id=self.id,name=self.name,author=self.author,price=self.price)

class Publisher(models.Model):
    name = models.CharField(max_length=100,null=False)
    address = models.CharField(max_length=100, null=False)