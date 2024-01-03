from django.db import models

# Create your models here.
from django.db import models

class HomePostNews(models.Model):
    sarlavha = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    matn = models.TextField()
    rasm = models.ImageField(upload_to="media")
    url = models.URLField(blank=True)
    yaratilgan_sana = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-yaratilgan_sana"]

    def __str__(self):
        return self.sarlavha



class AboutMe(models.Model):
    sarlavha = models.CharField(max_length=100)
    rasm = models.ImageField(blank=True, null=True)
    matn = models.TextField()

    def __str__(self):
        return self.sarlavha
