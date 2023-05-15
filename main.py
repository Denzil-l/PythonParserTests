import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


URL_TEMPLATE = 'https://www.work.ua/ru/jobs-odesa/?page=2'
FILE_NAME = "test.csv"

result_list = {'href': [], 'title': [], 'about': []}
r = requests.get(URL_TEMPLATE)

print(r.status_code)
soup = bs(r.text, "html.parser")
vacancies_names = soup.find_all('div', class_='card card-hover card-visited wordwrap job-link js-hot-block')
vacancies_info = soup.find_all('p', class_='overflow')
for name in vacancies_names:
    result_list['href'].append('https://www.work.ua'+name.a['href'])
    result_list['title'].append(name.a['title'])
for info in vacancies_info:
    result_list['about'].append(info.text)


df = pd.DataFrame(result_list)
df.to_csv(FILE_NAME)