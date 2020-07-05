from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image= models.ImageField(upload_to="portfolio/images/")
    url = models.URLField(blank=True)