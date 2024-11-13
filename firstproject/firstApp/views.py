from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def employeeView(request):
    emp = {
        'id':123,
        'name':'John',
        'salary':50000
    }
    
    return JsonResponse(emp)