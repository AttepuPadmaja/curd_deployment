from django.shortcuts import render,redirect

from app1.models import employee
from app1.forms import employee_form
from django.http import HttpResponse
from app1.forms1 import update_employee_form

def details(request):
    data = employee.objects.all()

    context = {
        'data' : data
    }
    return render(request,'frontend_app1/home.html',context)

def emp_form(request):
    form = employee_form()

    if request.method == 'POST':
        form = employee_form(request.POST)

        if form.is_valid():
            form.save()
            return redirect('emp_form1')

        else:
            return HttpResponse('Invalid data')
    else:
        form = employee_form()
        
    context = {
        'form':form
    }
    return render(request,'frontend_app1/employee_form.html',context)

def update(request,id):
    data = employee.objects.get(id=id)

    if request.method == 'POST':
        form = update_employee_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse("invalid data")
    else:
        form = update_employee_form(instance=data)
        context = {
            'form':form

        }
        return render(request,'frontend_app1/update_form.html',context)
def delete(request,id):
    data = employee.objects.get(id=id)
    data.delete()
    return redirect('home')
