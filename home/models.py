from django.db import models


# Create your models here.
class Project(models.Model):
    projectAuthor = models.CharField(max_length=50,auto_created=True)
    date = models.DateField(null=True)
    projectTitle = models.CharField(max_length=100)
    file = models.FileField(upload_to='projects/')
    approval = models.BooleanField(default=False)

    def __str__(self):
        self.projectInfo = (self.projectAuthor, self.date, self.projectTitle, self.file)
        return str(self.projectInfo)
