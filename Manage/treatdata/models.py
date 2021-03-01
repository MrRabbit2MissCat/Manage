from django.db import models

# Create your models here.
class DataFromweb(models.Model):
    productname = models.CharField(db_column='ProductName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    mj = models.FloatField(max_length=50, blank=True, null=True)
    high = models.FloatField(max_length=50, blank=True, null=True)
    crown = models.FloatField(db_column='Crown', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dj = models.FloatField(max_length=50, blank=True, null=True)
    price = models.CharField(max_length=50, blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    note = models.CharField(max_length=50, blank=True, null=True)
    time = models.DateField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_fromweb'