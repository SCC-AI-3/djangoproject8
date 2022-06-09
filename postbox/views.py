from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  # 게시글 삭제시 로그인된 사용자만 접근이 가등하도록 만들기 위해

import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse

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
                    # 타겟 URL을 읽어서 HTML를 받아오고,
            headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
            data = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4+%EC%88%9C%EC%9C%84',headers=headers)

            # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
            # soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
            # 이제 코딩을 통해 필요한 부분을 추출하면 된다.
            soup = BeautifulSoup(data.text, 'html.parser')

            # select를 이용해서, 크롤링할 범
            movies = soup.select('#main_pack > div.sc_new.cs_common_module.case_list.color_1._au_movie_list_content_wrap > div.cm_content_wrap > div > div > div.mflick > div._panel_popular._tab_content > div.list_image_info.type_pure_top > div > ul > li')
            movie_list = [] #크롤링할 것들을 리스트 형태로 

            for movie in movies: #크롤링할 것들 반복문 사용
                movie_dic = {}
                imgSrc = movie.select_one('a > div > div.thumb > img')['src']
                link = movie.select_one('a')['href']
                title = movie.select_one('a > div > div.title_box > strong').text
            
                movie_dic['imgSrc'] = imgSrc  
                movie_dic['link'] = "https://search.naver.com/search.naver"+link
                movie_dic['title'] = title
                
                movie_list.append(movie_dic)
            return render(request, 'postbox/index.html', {'movie_list':movie_list})

        else:  # 로그인이 되어 있지 않다면
            return redirect('/sign-in')



# ============================================================================= mypage
# ===







