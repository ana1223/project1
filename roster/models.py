from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.TextField(unique=True)
    number = models.IntegerField(unique=True, max_length=2)
    position = models.TextField(unique=False)
    height = models.CharField(unique=False, max_length=4)
    weight = models.IntegerField(unique=False, max_length=3)
    year = models.CharField(unique=False, max_length=10)
    hometown = models.TextField(unique=False)
    image = models.TextField(unique=False, null=True)
    prep = models.TextField(unique=False, null=True)
    personal = models.TextField(unique=False, null=True)
    
    class Meta(object):
        ordering = ('number', 'name')
    
    def __unicode__(self):
        return U'%s %s' %(self.number, self.name)
    

    
# Create your models here.
