from django.db import models

# Create your models here.
import sys

import users

sys.path.insert(0, '~/PycharmProjects/capstone/users')


class proposal(models.Model):
    name = models.CharField(max_length=128, blank=False)
    description = models.CharField(max_length=256, blank=False)
    # user = models.ForeignKey(users.User)
    approval = models.BooleanField(default=False)
