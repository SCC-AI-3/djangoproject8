from django.http import HttpResponse
from django.shortcuts import render         #---------- 8. html을 불러오기 위해 render를 임포트함.


#================================================================== base_response test


def base_response(request):     #---------------------- 1. base_response 함수 정의하고 djangoproject8 urls.py에 가서 path 지정해주기
    return HttpResponse("test")         #-------------- 2. Http응답으로 리턴해주는데 test라는 텍스트를 띄워주라


#================================================================== test.html 불러오기


def first_view(request):        #----------------------- 9. first_view 함수 정의하고 djangoproject8 urls.py에 가서 path 지정해주기
    return render(request, 'test.html')         #------- 10. templates에서 test.html을 render해라

