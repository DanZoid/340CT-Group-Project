from django.db import models


class Modules(models.Model):
    ModuleCode = models.CharField(max_length=10)
    ModuleTitle = models.CharField(max_length=40)
    ModuleTutor = models.CharField(max_length=40)

    def __str__(self):
        return self.ModuleCode + ' ' + self.ModuleTitle + ' ' + self.ModuleTutor


class Student(models.Model):
    StudentID = models.IntegerField()
    StudentFirstName = models.CharField(max_length=20)
    StudentLastName = models.CharField(max_length=20)
    Address = models.CharField(max_length=100)
    Postcode = models.CharField(max_length=7)

    def __str__(self):
        return str(self.StudentID) + ' ' + self.StudentFirstName + ' ' + self.StudentLastName + ' ' + self.Address + ' ' + self.Postcode


class Marks(models.Model):
    StudentID = models.ForeignKey('Student', on_delete=models.CASCADE)
    ModuleCode = models.ForeignKey('Modules', on_delete=models.CASCADE)
    ModuleMark = models.IntegerField()
    SubmittedDate = models.DateTimeField()

    def __str__(self):
        return str(self.StudentID) + ' ' + str(self.ModuleCode) + ' ' + str(self.ModuleMark) + ' ' + str(self.SubmittedDate)


class Coursework(models.Model):
    ModuleCode = models.ForeignKey('Modules', on_delete=models.CASCADE)
    CourseworkNo = models.CharField(max_length=10)
    CourseworkTitle = models.CharField(max_length=50)
    AssessmentType = models.CharField(max_length=50)
    IssueDate = models.DateField()
    DueDateTime = models.DateTimeField()


class Login(models.Model):
    UserName = models.CharField(max_length=50)


class Password(models.Model):
    Password = models.CharField(max_length=50)