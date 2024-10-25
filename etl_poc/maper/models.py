from django.db import models

# Create your models here.



class Maper(models.Model):
    id= models.CharField(max_length=100,db_column='employee_id',primary_key=True)
    employee_name = models.CharField(max_length=100,db_column="employee_name")

    def __str__(self):
        return self.employee_name

    class Meta:
        db_table = '[dev_api_test].[employee]'

# class ETLLoger(models.Model):
#     source = models.CharField(max_length=100)
#     created = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=100)
#     error = models.TextField(blank=True, null=True)

