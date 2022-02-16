from django.db import models

# Create your models here.
import users


class proposal(models.Model):
    name = models.CharField(max_length=128, required=True)
    description = models.CharField(max_length=256, required=True)
    user = models.ForeignKey(users.User)
    approval = models.BooleanField(default=False)
