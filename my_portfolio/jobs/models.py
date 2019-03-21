from django.db import models

class Job(models.Model):
    image =models.ImageField(upload_to="images/")
    summary = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    created_at = models.DateField(auto_created=True)
