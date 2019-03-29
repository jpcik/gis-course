from django.db import models
from django.contrib.gis.db import models

# Create your models here.


class City(models.Model):
    city_name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "cities"
    
    def __str__(self):
        return self.city_name
    
    

class Hospital(models.Model):
    hospital_name = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.hospital_name
    
    
class Canton(models.Model):
    name=models.CharField(max_length=200)
    geom=models.MultiPolygonField(srid=21781,null=True)
    
    
    class Meta:
        db_table = "cantons"
        
    def __str__(self):
        return self.name