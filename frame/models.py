from django.db import models

# Create your models here.
class FrameModel(models.Model):
    normal_image = models.ImageField(blank=True)
    depth_image = models.ImageField(blank=True)
    processed_image = models.ImageField(blank=True)

    normal_image_loc = models.CharField(max_length=100,blank=True)
    depth_image_loc = models.CharField(max_length=100,blank=True)
    processed_image_loc = models.CharField(max_length=100,blank=True)

    mean = models.DecimalField(max_digits=10,decimal_places=2)
    median = models.DecimalField(max_digits=10,decimal_places=2)
    # mode = models.DecimalField(max_digits=10,decimal_places=2)
    variance = models.DecimalField(max_digits=10,decimal_places=2)
    standard_deviation = models.DecimalField(max_digits=10,decimal_places=2)
    image_type = models.CharField(max_length=10)

    def __str__(self):
        return str(self.id)

