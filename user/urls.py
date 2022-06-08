from django.urls import path # 장고 url path 임포트
from . import views # user앱 views 임포트


urlpatterns = [
    path('sign-in/', views.sign_in_view, name='sign-in'),

    path('sign-up/', views.sign_up_view, name='sign-up'),

    path('logout/', views.logout, name='logout')
]


