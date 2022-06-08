from django.shortcuts import render, redirect  # redirect 임포트함. 회원가입 후 로그인페이지로 이동시키려고
from .models import UserModel  # 유저모델 임포트해서 끌어와서 씀
from django.contrib.auth import get_user_model  # 사용자가 있는지 검사하기 위한 임포트
from django.contrib import auth  # 로그인 중복확인
from django.contrib.auth.decorators import login_required  # 로그아웃하기 위해 임포트



# Create your views here.

# ============================================================================= 로그인


def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        me = auth.authenticate(request, username=username, password=password)  # 사용자 불러오기
        # 사용자 비밀번호와 유저네임이 맞는지 한번에 확인해주는 auth.authenticate

        if me is not None:
            auth.login(request, me)  # 만약에 사용자가 비어있지 않으면 me 정보를 넣고서 로그인 시켜줌.
            return redirect('/')

        else:
            return render(request, 'user/signin.html', {'error': '유저이름 혹은 패스워드를 확인 해 주세요'})

    elif request.method == 'GET':
        user = request.user.is_authenticated

        if user:  # 로그인이 되어 있다면
            return redirect('/')

        else:  # 로그인이 되어 있지 않다면
            return render(request, 'user/signin.html')



# ============================================================================= 회원가입



def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated  # 로그인 된 사용자가 요청하는지 검사

        if user:  # 로그인이 되어있다면
            return redirect('/')

        else:  # 로그인이 되어있지 않다면
            return render(request, 'user/signup.html')

    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        bio = request.POST.get('bio', '')

        if password != password2:
            return render(request, 'user/signup.html', {'error': '비밀번호를 확인 해 주세요'})

        else:
            if username == '' or password == '':
                # 사용자 저장을 위한 username과 password가 필수라는 것을 얘기 해 줍니다.
                return render(request, 'user/signup.html', {'error': '사용자 이름과 비밀번호는 필수입니다'})


            exist_user = get_user_model().objects.filter(username=username)
            # 데이터베이스(주황색) username과 입력한 username이 같다면 exist_user(존재하는 유저)로 변수 선언하고
            # get_user_model함수를 사용해서 데이터베이스에 있는지 없는지 중복확인을 해주고

            if exist_user:
                return render(request, 'user/signup.html', {'error':'사용자가 존재합니다'})

            else:
                UserModel.objects.create_user(username=username, password=password, bio=bio)

                return redirect('/sign-in')  # import



# ============================================================================= 로그아웃


@login_required
def logout(request):
    auth.logout(request)  # 인증 되어있는 정보를 없애기
    return redirect("/")



