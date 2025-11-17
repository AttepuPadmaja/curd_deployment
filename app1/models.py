from django.db import models

class employee(models.Model):
    emp_id = models.IntegerField(unique=True)
    emp_name = models.CharField(max_length=50)
    emp_email = models.EmailField(unique=True)
    emp_salary = models.FloatField()
    emp_mobile = models.BigIntegerField()
    emp_dept = models.CharField(max_length=50)
    emp_join_date = models.DateField()
