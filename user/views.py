from django.shortcuts import render, redirect  # redirect 임포트함. 회원가입 후 로그인페이지로 이동시키려고
from django.http import HttpResponse
from .models import UserModel  # 유저모델 임포트해서 끌어와서 씀
from django.contrib.auth import get_user_model  # 사용자가 있는지 검사하기 위한 임포트
from django.contrib import auth  # 로그인 중복확인
from django.contrib.auth.decorators import login_required # 로그아웃하기 위해 임포트

# Create your views here.

# ============================================================================= 로그인


def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        me = auth.authenticate(request, username=username, password=password)  # 사용자 불러오기
        # 사용자 비밀번호와 유저네임이 맞는지 한번에 확인해주는 auth.authenticate

        if me is not None:  # 저장된 사용자의 패스워드와 입력받은 패스워드 비교 / 사용자가 있는지 없는지만 구분해주면 됨.
            auth.login(request, me) # 만약에 사용자가 비어있지 않으면 me 정보를 넣고서 로그인 시켜줌.
            return redirect('/') # [ postbox앱 ] - urls에 기본 path('', 기본 Home 함수로 넘어감 !!!!!

        else: # 로그인이 실패하면 다시 로그인 페이지를 보여주고 error 띄우기
            return render(request,'user/signin.html',{'error':'유저이름 혹은 패스워드를 확인 해 주세요'})


    elif request.method == 'GET':
        user = request.user.is_authenticated  # 사용자가 로그인 되어 있는지 검사

        if user:  # 로그인이 되어 있다면 로그인페이지로 보내지 않기 위해서 redirect하고
            return redirect('/')

        else:  # 로그인이 되어 있지 않다면 로그인하라는 페이지로
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

        # 패스워드가 패스워드2와 같지 않다면
        if password != password2:
            return render(request, 'user/signup.html'), {'error': '비밀번호가 다릅니다'}

        # 패스워드와 패스워드2가 같다면
        else:
            if username == '' or password == '':
                # 사용자 저장을 위한 username과 password가 필수라는 것을 얘기 해 줍니다.
                return render(request, 'user/signup.html', {'error': '사용자 이름과 패스워드는 필수 값 입니다'})

            exist_user = get_user_model().objects.filter(username=username)
            # exist_user = UserModel.objects.filter(username=username)
            # 데이터베이스(주황색) username과 입력한 username이 같다면 exist_user(존재하는 유저)로 변수 선언하고
            # get_user_model함수를 사용해서 데이터베이스에 있는지 없는지 중복확인을 해주고

            if exist_user:  # 만일 존재하는 유저일 경우
                return render(request, 'user/signup.html', {'error': '이미 사용중인 이름입니다'})
                # 사용자가 존재하기 때문에 사용자를 저장하지 않고 회원가입 페이지를 다시 띄움
                # 사용자가 존재하지 않으면 아래로

            else:
                UserModel.objects.create_user(username=username, password=password, bio=bio)
                # 바로 유저를 생성해서 저장해줌.

                return redirect('/sign-in')


# ============================================================================= 로그인 유저 postbox접근 제한


def postbox(request):
    if request.method == 'GET':  # 요청하는 방식이 GET 방식인지 확인하기
        user = request.user.is_authenticated  # 사용자가 로그인이 되어 있는지 확인하기

        if user:  # 로그인 한 사용자라면
            return render(request, 'postbox/index.html')

        else:  # 로그인이 되어 있지 않다면
            return redirect('/sign-in')


# ============================================================================= 로그아웃


@login_required
def logout(request):
    auth.logout(request) # 인증 되어있는 정보를 없애기
    return redirect("/")



