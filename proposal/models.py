from django.db import models

# Create your models here.
import sys

from capstone import settings

sys.path.insert(0, '~/PycharmProjects/capstone/users')


class proposal(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=128, blank=False)
    description = models.CharField(max_length=256, blank=False)  # TODO: Temporary: Replace with file upload
    approval = models.BooleanField(default=False)

    def __str__(self):
        return self.title
