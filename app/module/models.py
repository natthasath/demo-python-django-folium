from django.db import models

# Create your models here.
SEMESTER_CHOICES = (
    ("ทดสอบ", "ทดสอบ"),
    ("รัฐวิสาหกิจ", "รัฐวิสาหกิจ"),
)

class location(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    type = models.CharField(
        max_length = 20,
        choices = SEMESTER_CHOICES,
        default = '1'
    )
    latitude = models.FloatField(max_length=20)
    longitude = models.FloatField(max_length=20)

    def __str__(self):
        return self.name
    
class type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name