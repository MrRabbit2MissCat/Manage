from django.db import models

# Create your models here.
class Usertable(models.Model):
    username = models.CharField(unique=True, max_length=50, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'usertable'