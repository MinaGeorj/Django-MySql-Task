from django.db import models

class Device(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    status = models.CharField(max_length=255,default='')
    chassis_type = models.CharField(max_length=255,default='')
    service_type = models.CharField(max_length=255,default='')
    device_type = models.CharField(max_length=255,default='')
    toposite_name = models.CharField(max_length=255,default='')
    site_name = models.CharField(max_length=255,default='')
    ico01 = models.IntegerField(default=0)

    class Meta:
        db_table = "devices"
