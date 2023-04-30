from django.db import models

# Create your models here.
class Logger(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)

    time_log = models.TimeField(help_text = "Enter the exact time")

    # to define a customized string representation of the object in the admin interface
    def __str__(self):
        return self.first_name