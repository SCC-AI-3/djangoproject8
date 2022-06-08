from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  # 게시글 삭제시 로그인된 사용자만 접근이 가등하도록 만들기 위해

# Create your views here.


# 사용자가 로그인 했는지 확인해서 페이지를 나눠보여주도록 함

# ============================================================================= home

def home(request):
    user = request.user.is_authenticated  # 사용자가 인증을 받아서 로그인이 되어있는지 확인하기

    if user:  # 사용자가 있으면
        return redirect('/postbox')  # postbox url로

    else:     # 사용자가 없다면
        return redirect('/sign-in')   # 로그인 페이지로


# ============================================================================= postbox


def postbox(request):
    if request.method == 'GET':
        user = request.user.is_authenticated  # 사용자가 로그인이 되어 있는지 확인하기

        if user:  # 로그인 한 사용자라면
            return render(request, 'postbox/index.html')

        else:  # 로그인이 되어 있지 않다면
            return redirect('/sign-in')


# ============================================================================= mypage








