from django.db import models

# Create your models here.


class userinfo(models.Model):
    title = models.CharField(max_length=20)
    code = models.BigIntegerField()
    language = models.BigIntegerField()
    style = models.DateField()
    

    def __str__(self):
        return self.name
