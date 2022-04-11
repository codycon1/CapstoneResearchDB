from django.db import models


# Create your models here.
class Project(models.Model):

    projectAuthor = models.CharField(max_length=50)
    date = models.DateField()
    projectTitle = models.CharField(max_length=100)
    file = models.FileField(upload_to='projects/')
    dataFiles = models.FileField(upload_to='projects/datasets')
    resultFiles = models.FileField(upload_to='projects/results')
    approval = models.BooleanField(default=False)

    def __str__(self):
        self.projectInfo = (self.projectAuthor, self.date, self.projectTitle, self.file)
        return str(self.projectInfo)
