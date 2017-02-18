from __future__ import unicode_literals

from django.db import models

class Word(models.Model):
    current = models.CharField(max_length=255)
    meaning = models.TextField()

    def __str__(self):
        return self.current
