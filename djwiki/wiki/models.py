from django.db import models

class Page(models.Model):
    name = models.CharField(max_length=40, unique=True)
    content = models.TextField()

    def __unicode__(self):
        return self.title    