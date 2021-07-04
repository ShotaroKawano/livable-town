import requests
from bs4 import BeautifulSoup
import re
import time

target_towns = ['荻窪', '練馬', '武蔵小山', '赤羽', '大山', '三鷹', '大岡山', '千歳烏山', '成増', '三軒茶屋', '阿佐ヶ谷', 'ひばりヶ丘', '経堂', '旗の台', '大森', '糀谷', '永福町', '下高井戸', '戸越銀座', '仙川', '調布', '王子', '十条', '住吉', '曳舟', '中井', '方南町', '千歳船橋', '大泉学園', '葛西']
exception_towns = {'池袋': 'https://blog.ieagent.jp/eria/ikebukurosumiyasusa-697'}

actuarl_target_towns = []
stars_data = []
for target_town in target_towns:
    time.sleep(1)
    if target_town in exception_towns.keys():
        article_url_tail = exception_towns[target_town]
    else:
        base_url = 'https://blog.ieagent.jp/'
        # search_query = '成増'
        search_query = target_town
        search_url = base_url + '?s=' + search_query
        # print(search_url)
        search_page = requests.get(search_url)

        # print(res.text)
        search_soup = BeautifulSoup(search_page.text, 'html.parser')
        category_tag = search_soup.find('p', class_='category-tag__area')
        # print(category_tag)
        article_url_tail = category_tag.parent.parent.parent.parent.attrs['href']

    article_url = base_url + article_url_tail
    # print(article_url)
    article_page = requests.get(article_url)

    article_soup = BeautifulSoup(article_page.text, 'html.parser')
    title = article_soup.select_one('body > div.inner > div.main-contents > div.contens-inner > section > h1')
    print(title.text)
    stars_imgs = article_soup.find_all('img', src=re.compile('/_wt/semicolon/img/starImg-orange-.f\.svg'), limit=6)
    # print(stars_imgs)
    stars_datum = []
    for stars_img in stars_imgs:
        # print(stars_img.attrs['alt'])
        # print(stars_img.attrs['src'][34])
        stars_datum.append(int(stars_img.attrs['src'][34]))

    # print(stars_datum)
    if stars_datum:
        actuarl_target_towns.append(target_town)
        stars_data.append(stars_datum)
    else:
        print('データ不正 ' + target_town)

print(len(actuarl_target_towns))
print(len(stars_data))
print(actuarl_target_towns)
print(stars_data)
