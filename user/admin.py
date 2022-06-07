from django.contrib import admin # 이거는 앱을 만들면 저절로 임포트되어있음.
from .models import UserModel # models.py를 불러올거고 그 중에서 UserModel을 가져올 것

# Register your models here.

admin.site.register(UserModel) # 나의 UserModel을 손쉽게 관리하도록 admin에 추가해줌.

