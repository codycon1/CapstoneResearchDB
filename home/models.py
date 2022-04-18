from django.db import models


# Create your models here.
class Project(models.Model):
    email = models.EmailField(max_length=256)
    date = models.DateField(auto_now=True)
    projectAuthor = models.CharField(max_length=128)
    projectTitle = models.CharField(max_length=100, verbose_name="Project Title")
    projectDescription = models.CharField(max_length=256, verbose_name="Project Description")
    proposalFile = models.FileField(upload_to='projects/proposals', verbose_name="Proposal", null=True)
    approval = models.BooleanField(default=False)

    def __str__(self):
        self.projectInfo = (self.projectAuthor, self.date, self.projectTitle, self.proposalFile)
        return str(self.projectInfo)


class ProjectFile(models.Model):
    projectID = models.ForeignKey(Project, on_delete=models.CASCADE)
    userEmail = models.EmailField(max_length=256)
    file = models.FileField(upload_to='projects/')
    uploadDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
