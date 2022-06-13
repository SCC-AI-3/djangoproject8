import json
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import seaborn as sns
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from postbox.models import favorite, MovieData



movie_data = pd.read_csv('movies.csv')
rating_data1 = pd.read_csv('ratings.csv')

rating_data = rating_data1.drop(['timestamp'], axis=1)

user_movie_rating1 = pd.merge(rating_data, movie_data, on='movieId')


movie_user_rating = user_movie_rating1.pivot_table('rating', index = 'movieId', columns='userId')
user_movie_rating = user_movie_rating1.pivot_table('rating', index = 'userId', columns='movieId')


movie_user_rating.fillna(0, inplace=True)


item_based_collabor = cosine_similarity(movie_user_rating)
item_based_collabor = pd.DataFrame(data=item_based_collabor, index=movie_user_rating.index, columns=user_movie_rating.columns)






# Create your views here.
"""qs = movieModel.objects.all().values()
ps = ratingModel.objects.all().values()
movie_data1 = pd.DataFrame(qs)
rating_data1 = pd.DataFrame(ps)


movie_data = movie_data1.drop(['id'], axis=1)

rating_data = rating_data1.drop(['id','timestamp'], axis=1)


user_movie_rating1 = pd.merge(rating_data, movie_data, on='movieId')

print(user_movie_rating1)
print(user_movie_rating1.info())

movie_user_rating1 = user_movie_rating1.pivot_table('rating', index = 'movieId', columns='userId')
user_movie_rating = user_movie_rating1.pivot_table('rating', index = 'userId', columns='title')



print(movie_user_rating1.columns)
print(user_movie_rating.columns)

print(movie_user_rating1)
print(user_movie_rating)

movie_user_rating = movie_user_rating1.drop(index=['162672', '163949'], axis=0)
movie_user_rating.fillna(0, inplace=True)


item_based_collabor = cosine_similarity(movie_user_rating)
item_based_collabor = pd.DataFrame(data=item_based_collabor, index=movie_user_rating.index, columns=user_movie_rating.columns)

def get_item_based_collabor(title):
    return item_based_collabor[title].sort_values(ascending=False)[:6]"""




def recommend_movie(request):
        user = request.user.is_authenticated  # 사용자가 로그인이 되어 있는지 확인하기

        if user:  # 로그인 한 사용자라면
            movie_list = MovieData.objects.all()  # 크롤링할 것들을 리스트 형태로

            # 내가 찜한 영화

            favorite_movie = favorite.objects.filter(author=request.user)

            favorite_movie1= favorite_movie.values_list()
            favorite_movie2 = list(favorite_movie1)

            print(favorite_movie2)
            title =[i for _, _, i, _ in favorite_movie2]


            # recommend 추천시스템

            totalRating = pd.DataFrame(index =['movieId'], columns=['result']) # 빈데이터 프레임 설정

            for a in title:
                topKRating = pd.DataFrame(item_based_collabor[a].sort_values(ascending=False)[:10])#10개 내림차순 정리
                topKRating.columns = ['result']
                totalRating = totalRating.append(topKRating)

            totalRating2 = totalRating.sort_values(by='result', ascending=False)[:10] # 합친 데이터 프레임 10개 내림차순
            totalRating3 = totalRating2.loc[~totalRating2.index.duplicated(keep='first')]

            movieIds = totalRating3.index.tolist()
            movie_list1 = []  #
            for movieId in movieIds:
                 movie_dic1={}
                 movie = movie_data[movie_data['movieId'] == movieId].iloc[0]

                 movie_dic1['movieId'] = movie.movieId
                 movie_dic1['title'] = movie.title
                 movie_dic1['Poster'] = movie.Poster

                 movie_list1.append(movie_dic1)

            return render(request, 'index.html', {'movie_list': movie_list, 'class_object': movie_list1, 'favorite_movie': favorite_movie})


        else:  # 로그인이 되어 있지 않다면
            return redirect('/sign-in')




@login_required()
def reviews(request, id):
    user = request.user.is_authenticated
    if user:
        favorite_movie = favorite.objects.filter(author=request.user)

        favorite_movie1 = favorite_movie.values_list()
        favorite_movie2 = list(favorite_movie1)


        title =[i for _, _, i, _ in favorite_movie2]


        totalRating = pd.DataFrame(index=['movieId'], columns=['result'])  # 빈데이터 프레임 설정
        for a in title:
            topKRating = pd.DataFrame(item_based_collabor[a].sort_values(ascending=False)[:10])  # 10개 내림차순 정리
            topKRating.columns = ['result']
            totalRating = totalRating.append(topKRating)

        totalRating2 = totalRating.sort_values(by='result', ascending=False)[:10]  # 합친 데이터 프레임 10개 내림차순
        totalRating3 = totalRating2.loc[~totalRating2.index.duplicated(keep='first')]

        movieIds = totalRating3.index.tolist()
        movie_list1 = []  # 크롤링할 것들을 리스트 형태로
        for movieId in movieIds:
            movie_dic1 = {}
            movie = movie_data[movie_data['movieId'] == movieId].iloc[0]

            movie_dic1['movieId'] = movie.movieId
            movie_dic1['title'] = movie.title
            movie_dic1['genre'] = movie.genres
            movie_dic1['Poster'] = movie.Poster

            movie_list1.append(movie_dic1)

        movie2 = pd.DataFrame(movie_list1)

        movie3 = movie2[movie2['movieId']==id]

        movie_list2 = movie3.to_dict('records')


        context = {'class_object': movie_list2}

        return render(request, 'review.html', context)
    else:
        redirect('/recommend')



