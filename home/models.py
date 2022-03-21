from django.db import models

# Create your models here.
class IsOrganiser(models.Model):
    id = models.FloatField(primary_key=True)
    status = models.FloatField()
    username = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'is_organiser'

class Wbusers(models.Model):
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    contact = models.FloatField()
    proflepic = models.FileField(upload_to='media',max_length=100, blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'wbusers'