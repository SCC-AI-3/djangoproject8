from django.db import models # 얘는 앱을 생성하면 저절로 임포트 되어있음.
from django.contrib.auth.models import AbstractUser # 장고에서 기본 모델에서 모델을 추가할 때 AbstractUser를 씀.

# Create your models here.


# ==================================================================  user model


class UserModel(AbstractUser): # class이름 : UserModel. 모델의 정보를 담고 있는 곳. AbstractUser을 상속해서 쓰는데 bio를 추가해서 쓰겠음
    class Meta:
        db_table = "sns_user"

    bio = models.TextField(max_length=1000, blank=True)
    # 유저의 소개글 object - dafault, null, blank 설명은 https://daeguowl.tistory.com/64





