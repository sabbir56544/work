from django.db import models

class AreaList(models.Model):
    area_no = models.IntegerField()
    area_name = models.CharField(max_length=30)
    area_size = models.IntegerField()
    area_disc = models.TextField()

    def __str__(self):
        return self.area_name
