from django.db import models            #----------------- 이거는 앱을 만들면 저절로 임포트되어있음.
from user.models import UserModel            #------------ 47. user앱에 있는 models를 임포트 해줘야함. 유저와 글이 연결되어야 하니까


# Create your models here.

#======================================================================== 48. postbox model 만들기


class PostBox(models.Model):        #------------------------------------ 49. class이름 : PostBox. 모델의 정보를 담고 있는 곳
    class Meta:        #------------------------------------------------- 50. db 정보 : Meta
        db_table = "user_postbox"        #------------------------------- 51. db_table 이름 : user_postbox

        # =============================================================== 52. postbox model의 object들 만들기
        # =============================================================== 53. 장고에서 제공하는 모델을 사용해서 각 요소에 어떤 데이터의 형식이 들어갈지 정해주는 것임.

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    # ====== 54. author : postbox를 작성하는 작성자
    # ====== 55. ForeignKey : models에 있는 UserModel을 가져와서 구분해서 사용하겠다. 각 사용자를 구분해야 하므로
    # ====== 56. UserModel : UserMedel의 사용자가 작성 한 글임. ForeignKey의 영향을 받음.
    # ====== 57. on_delete=models.CASCADE : 사용자를 삭제하면 해당 object를 참고하는 object도 삭제해라. 계정을 삭제 했을 때 postbox도 같이 삭제되는 것을 생각하면 됨.

    content = models.CharField(max_length=5000, null=False)  # ========== 58. content object - 문자열 모델 - 최대 문자 길이 5000. 빈 문자열 저장하지 않음 (False)
    creat_at = models.DateTimeField(auto_now_add=True)  # =============== 59. 생성일 object - 해당 레코드 생성시 (auto) 자동으로 (now) 지금 시간을 (add) 저장.
    update_at = models.DateTimeField(auto_now=True)  # ================== 60. 수정일 object - 해당 레코드 갱신시 (auto) 자동으로 (now) 현재 시간 저장

    # ====== CharField, TextField, SlugField, EmailField, CommaSeparatedIntegerField, UUIDField: 문자열
    # ====== DateTimeField, DateField, TimeField : 날짜 / 시간
    # ====== ForeignKey : 다른 테이블과 연관을 지어 줄 때

    # ====== 61. [ 서버 정지 ] 모델의 object를 만들면 생성해준 object를 데이터베이스에 적용하기 위해 terminal에서 [ python manage.py makemigrations ]를 해주고 [ python manage.py migrate ]해야함.
    # ====== 62. 다음으로 postbox 모델을 관리하기 위해 admin에 추가해줘야 함. postbox admin.py로 이동



