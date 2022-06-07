from django.http import HttpResponse
from django.shortcuts import render         # html을 불러오기 위해 render를 임포트함.


#================================================================== base_response test


def base_response(request):
    return HttpResponse("test")


#================================================================== test.html 불러오기


def first_view(request):
    return render(request, 'test.html')

