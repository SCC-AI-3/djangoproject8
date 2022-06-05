from django.db import models        #------------------------------ 얘는 앱을 생성하면 저절로 임포트 되어있음.

# Create your models here.


#================================================================== 23. user model 만들기


class UserModel(models.Model):        #----------------------------- 24. class이름 : UserModel. 모델의 정보를 담고 있는 곳
    class Meta:        #-------------------------------------------- 25. db 정보 : Meta
        db_table = "sns_user"        #------------------------------ 26. db_table 이름 : sns_user

        # ========================================================== 27. user model의 object들 만들기
        # ========================================================== 28. 장고에서 제공하는 모델을 사용해서 각 요소에 어떤 데이터의 형식이 들어갈지 정해주는 것임.

    username = models.CharField(max_length=20, null=False)    #====== 29. 유저의 이름 object - 문자열 모델 - 최대 문자 길이 20. 빈 문자열 저장하지 않음 (False)
    password = models.CharField(max_length=256, null=False)    #===== 30. 비밀번호  object
    bio = models.CharField (max_length=256, default='')    #========= 31. 유저의 소개글 object - dafault, null, blank 설명은 https://daeguowl.tistory.com/64
    created_at = models.DateTimeField(auto_now_add=True)    #======== 32. 생성일 object - 해당 레코드 생성시 (auto) 자동으로 (now) 지금 시간을 (add) 저장.
    updated_at = models.DateField(auto_now=True)    #================ 33. 수정일 object - 해당 레코드 갱신시 (auto) 자동으로 (now) 현재 시간 저장

    # 34. [ 문자열 ] CharField, TextField, SlugField, EmailField, CommaSeparatedIntegerField, UUIDField
    # 35. [ 날짜 / 시간 ] DateTimeField, DateField, TimeField
    # 36. [ 다른 테이블과 연관을 지어줄 때 ] ForeignKey

    # 37. 모델의 object를 만들면 생성해준 object를 데이터베이스에 적용하기 위해 terminal에서 [ python manage.py makemigrations ]를 해주고 [ python manage.py migrate ]해야함.
    # 38. [ 서버 재실행 ] http://127.0.0.1:8000/admin 홈페이지 들어가서 admin 페이지 열리는지 확인.
    # 39. terminal에서 [ python manage.py createsuperuser ] 계정만들기
    # 40. admin Username : admin8
    # 41. Password : 1234
    # 42. 그리고 user admin 페이지에 위 object 들을 관리할 수 있도록 user admin.py에 추가해줘야 함. user admin.py로 이동




