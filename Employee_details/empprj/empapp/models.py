from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Employee(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Name=models.CharField(max_length=225)
    Emp_id=models.CharField(max_length=20,unique=True)
    DOB=models.DateField()
    GENDER_CHOICES=(
        ('M','Male'),
        ('F','Female'),
        ('O','Others'),
    )
    Gender=models.CharField(max_length=1,choices=GENDER_CHOICES)
    Mobile_no=models.CharField(max_length=15)
    Email=models.EmailField()
    Designation=models.CharField(max_length=100)
    Department=models.CharField(max_length=100)
    Salary=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name
