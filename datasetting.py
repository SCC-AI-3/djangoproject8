from django.http import HttpResponse
import csv
import pandas as pd
from postbox.models import movieModel
import requests

def inputData(requests):
    with open('/Users/kimhyukjin/djangoproject8/moviesmovies.csv', 'r', encoding='utf-8') as f: ## moviesmovies 파일 경로지정해주세요
        dr = csv.DictReader(f)
        df = pd.DataFrame(dr)
    dataSet = []

    for i in range(len(df)):
        tmp = (df['title'][i], df['genre'][i], df['Poster'][i])
        dataSet.append(tmp)

    for i in range(len(dataSet)):
        movieModel.objects.create(title=dataSet[i][0], genre=dataSet[i][1], Poster=dataSet[i][2])

    return HttpResponse('성공')