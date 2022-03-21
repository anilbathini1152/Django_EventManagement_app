from django.db import models
import uuid


# Create your models here.
class Events(models.Model):
    evntid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    ename = models.CharField(max_length=30)
    etype = models.CharField(max_length=10)
    place = models.CharField(max_length=20)
    edate = models.DateField()
    etime = models.CharField(max_length=20)
    edesc = models.CharField(max_length=200, blank=True, null=True)
    orgusrname = models.CharField(max_length=30)     
    amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'events'

class Evntorganisers(models.Model):
    contact = models.FloatField()
    org_no = models.CharField(max_length=30, blank=True, null=True)
    org_name = models.CharField(max_length=30, blank=True, null=True)
    prof = models.FileField(upload_to='media',default='media/default.png',max_length=100, blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'evntorganisers'
        
class Evntregistrations(models.Model):
    regid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    evntid = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    ename = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'evntregistrations'