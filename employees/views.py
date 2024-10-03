from django.shortcuts import render
from django.http import JsonResponse
from .models import Subdivision


def get_employees(request):
    """
    Target func that returns all subdivisions and fetch employees
    :param request: default request parameter
    :return: all subdivisions
    """
    deps = Subdivision.objects.prefetch_related('employees').all()
    return render(request, "employees/deps.html", {'deps': deps})


def load_employees(request, id):
    """
    Func that load all employees from certain subdivision
    :param request: default request parameter
    :param id: subdivision id
    :return: employees of subdivision
    """
    subdivision = Subdivision.objects.prefetch_related('employees').get(id=id)
    employees = list(subdivision.employees.values('full_name', 'position', 'salary', 'hire_date'))
    return JsonResponse(employees, safe=False)
