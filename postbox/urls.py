from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'), # 127.0.0.1:8000 과 views.py 폴더의 home 함수 연결

    path('postbox/', views.PostBox, name='postbox') # 127.0.0.1:8000/postbox와 views.py 폴더의 postbox 함수 연결
]


