from django.contrib import admin            #----------------- 이거는 앱을 만들면 저절로 임포트되어있음.
from .models import PostBox            #---------------------- 63. models.py를 불러올거고 그 중에서 UserModel을 가져올 것

# Register your models here.

admin.site.register(PostBox)            #--------------------- 64. 나의 postbox를 손쉽게 관리하도록 admin에 추가해줌.
                                          #------------------- 65. admin 주소를 다시 들어가서 로그인하면 POSTBOX 아래 post boxs가 생성된 것을 확인.


