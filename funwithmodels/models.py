from django.db import models

# Create your models here.
class CommonDataTypes(models.Model):
    binary = models.BinaryField(blank=True, null=True)
    bool = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    time = models.TimeField(auto_now_add=True, blank=True, null=True)
    str = models.TextField(max_length=129)
    int = models.IntegerField(blank=True, null=True)
    float = models.FloatField(blank=True, null=True)
    #img = models.ImageField(blank=True, null=True)


class FKModel(models.Model):
    foreignkey = models.ForeignKey(CommonDataTypes, related_name='fkname', on_delete=models.CASCADE, blank=True,
                                   null=True)