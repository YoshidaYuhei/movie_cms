import csv
import datetime
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

from telephone_range.settings import MEDIA_ROOT

rooturl = 'https://filmarks.com/movies/'

output_list = []
for i in range(10):
    if i == 0:
        continue

    # 1レコードを格納するDict
    record_dict = {}

    url = urljoin(rooturl, str(i))
    response = requests.get(url)

    # 404_notfoundは飛ばす
    # if response.status_code == 404:
    #     continue

    soup = BeautifulSoup(response.content, 'html.parser')

    # id
    record_dict['id'] = i

    # title
    title = soup.h2.span.string
    record_dict['title'] = title

    # thumbnail
    src = soup.find('img', alt=title).get('src')
    extention = str(src)[-4:]
    if extention != '.svg':
        r = requests.get(src)
        with open(os.path.join(MEDIA_ROOT, 'thumbnail/' + str(i) + '.jpg'), 'wb') as file:
            file.write(r.content)

        record_dict['thumbnail'] = '/thumbnail/' + str(i) + '.jpg'
    else:
        record_dict['thumbnail'] = ''

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

        record_dict['release_date'] = release_date
    else:
        record_dict['release_date'] = '1900-01-01'

    if '製作国' in h3_dict:
        country = h3_dict['製作国']
        record_dict['country'] = country
    else:
        record_dict['country'] = ''

    if '上映時間' in h3_dict:
        duration = int(h3_dict['上映時間'].replace('分', ''))
        duration_delta = datetime.timedelta(minutes=duration)
        record_dict['duration'] = duration_delta
    else:
        record_dict['duration'] = ''

    # genre
    genre = soup.select_one('div.p-content-detail__genre')

    try:
        record_dict['genre'] = genre.ul.li.a.string
    except AttributeError:
        record_dict['genre'] = '不明'

    # director
    try:
        director = soup.select_one('a.c-label')
        if director is not None:
            record_dict['director'] = director.string
        else:
            record_dict['director'] = '不明'

    except AttributeError:
        record_dict['director'] = '不明'

    # cast
    cast_soup = soup.find('div', class_='p-content-detail__people-list-casts')
    cast_list = ''
    try:
        for cast in cast_soup.select('a.c-label'):
            cast_list += cast.string + ';'

            record_dict['cast'] = cast_list
    except AttributeError:
        record_dict['cast'] = '不明'

    output_list.append(record_dict)

with open('/Users/yoshidayuuhei/Desktop/sample_writer.csv', 'w') as f:
    writer = csv.writer(f)
    for row in output_list:
        writer.writerow(row.values())

