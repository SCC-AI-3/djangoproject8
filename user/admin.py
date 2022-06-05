from django.contrib import admin            #----------------- 이거는 앱을 만들면 저절로 임포트되어있음.
from .models import UserModel            #-------------------- 43. models.py를 불러올거고 그 중에서 UserModel을 가져올 것

# Register your models here.

admin.site.register(UserModel)            #------------------- 44. 나의 UserModel을 손쉽게 관리하도록 admin에 추가해줌.
                                          #------------------- 45. admin 주소를 다시 들어가서 로그인하면 USER 아래 User models가 생성된 것을 확인.
                                          # ------------------ 46. 다음으로 postbox 모델을 만들고 데이터베이스로 연결할 것임. postbox에 models.py로 이동

