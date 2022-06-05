"""djangoProject8 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views         #---------------------------------------------- 4. djangoproject8 views.py를 임포트하고

urlpatterns = [
    path('admin/', admin.site.urls),        #------------------------------ http://127.0.0.1:8000/admin 으로 접속

    path('test/', views.base_response, name='first_test'),          #------ 5. http://127.0.0.1:8000/test 으로 접속. views.py에 base_response 함수를 불러오는데 이름은 first test
                            #---------------------------------------------- 6. 위 주소로 접속해서 test html 뜨는지 확인해서 뜨면 잘 연결 된 것임. 그리고 templates에서 test.html을 생성

    path('first/', views.first_view,name='first_view')          #---------- 11. http://127.0.0.1:8000/first 으로 접속. views.py에 first_view 함수를 불러오는데 이름은 first view
    # --------------------------------------------------------------------- 12. 위 주소로 접속해서 '테스트 페이지'라는 텍스트가 나오면 연결된 것임.
    # --------------------------------------------------------------------- 13. views.py 작업하고 urls.py연결하는 순서를 기억하면 좋음. 다음으로 user와 postbox앱을 추가해 주겠음. [ 서버 정지 ] terminal에서 [ django-admin startapp user ] [ django-admin startapp postbox ].
    # --------------------------------------------------------------------- 14. 생성된 user앱과 postbox앱을 연결해주기 위해 djangoproject8 setting.py에 들어가서 INSTALLED_APPS 에 추가할 것임.

]
