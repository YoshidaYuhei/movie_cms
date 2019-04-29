import csv
import datetime
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
from telephone_range.settings import MEDIA_ROOT
from .models import Content, Cast, Director, Genre


class WebScraping():

    TARGET_URL = 'https://filmarks.com/movies/'

    def scrape(self, start, end):
        for i in range(start, end):

            url = urljoin(self.TARGET_URL, str(i))
            response = requests.get(url)

            # 404_notfoundは飛ばす
            if response.status_code == 404:
                continue

            soup = BeautifulSoup(response.content, 'html.parser')

            # モデルインスタンスの作成＋IDの作成
            content, _ = Content.objects.update_or_create(id=i)

            # title
            title = soup.h2.span.string
            content.title = title

            # thumbnail
            src = soup.find('img', alt=title).get('src')
            extention = str(src)[-4:]
            if extention != '.svg':
                r = requests.get(src)
                with open(os.path.join(MEDIA_ROOT, 'thumbnail/' + str(i) + '.jpg'), 'wb') as file:
                    file.write(r.content)

                content.thumbnail = '/thumbnail/' + str(i) + '.jpg'
            else:
                content.thumbnail = ''

            # release_date, country, duration
            h3_set = soup.select('h3.p-content-detail__other-info-title')

            h3_dict = {}
            for itr in h3_set:
                itr_str = itr.string.split('：')
                h3_dict[itr_str[0]] = itr_str[1]

            if '上映日' in h3_dict:
                if '月' in h3_dict['上映日']:
                    release_date = h3_dict['上映日'].replace('年', '-').replace('月', '-').replace('日', '')
                else:
                    release_date = h3_dict['上映日'].replace('年', '-') + '01-01'

                content.release_date = release_date
            else:
                content.release_date = '1900-01-01'

            if '製作国' in h3_dict:
                country = h3_dict['製作国']
                content.country = country
            else:
                content.country = ''

            if '上映時間' in h3_dict:
                duration = int(h3_dict['上映時間'].replace('分', ''))
                duration_delta = datetime.timedelta(minutes=duration)
                content.duration = duration_delta
            else:
                pass
                # content.duration = ''

            # genre
            genre_soup = soup.select_one('div.p-content-detail__genre')

            try:
                genre_name = genre_soup.ul.li.a.string
                genre, _ = Genre.objects.get_or_create(name=genre_name)
            except AttributeError:
                content.genre = Genre.objects.get(name='不明')

            # director
            try:
                director_soup = soup.select_one('a.c-label')
                if director_soup is not None:
                    director_name = director_soup.string
                    director, _ = Director.objects.get_or_create(name=director_name)
                else:
                    director = Director.objects.get(name='不明')

            except AttributeError:
                director = Director.objects.get(name='不明')

            content.director = director

            content.save()

            # cast
            cast_soup = soup.find('div', class_='p-content-detail__people-list-casts')
            try:
                for cast_one in cast_soup.select('a.c-label'):
                    cast, _ = Cast.objects.get_or_create(name=cast_one.string)
                    content.cast.add(cast)
            except AttributeError:
                cast = Cast.objects.get(name='不明')
                content.cast.add(cast)

            content.save()

    def csv_import(self, file):
        csv_file = csv.reader(file)

        for line in file:
            content, created = Content.objects.update_or_create(id=line[0])
            content.id = line[0]
            content.title = line[1]
            content.thumbnail = line[2]
            content.release_date = line[3]
            content.country = line[4]
            # content.duration = line[5]

            genre, _ = Genre.objects.get_or_create(name=line[6])
            content.genre = genre

            # get_or_createは辞書とBooleanのタプルで帰ってくるので辞書だけ取り出す。
            direct, _ = Director.objects.get_or_create(name=line[7])
            content.director = direct

            content.save()

            # castは複数件を想定して処理
            casts = line[8].split(';')

            for itr in casts:
                cs, _ = Cast.objects.get_or_create(name=itr)
                content.cast.add(cs)

            # content.awards = line[9]
            content.save()

