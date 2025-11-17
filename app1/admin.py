from django.contrib import admin
from app1.models import employee
class employee_admin(admin.ModelAdmin):
    list_display = ['emp_id','emp_name','emp_email','emp_salary','emp_mobile','emp_dept','emp_join_date']
admin.site.register(employee,employee_admin)
