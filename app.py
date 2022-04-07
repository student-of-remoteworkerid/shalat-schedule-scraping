import requests
from bs4 import BeautifulSoup
import datetime

url = 'http://jadwalsholat.pkpu.or.id/?id=21'

contents = requests.get(url)

response = BeautifulSoup(contents.text, "html.parser")


date = response.find('td').find('b').text
current_time = datetime.datetime.now()
title = response.find('td').find('small')
temp = str(title.text).lstrip("(").rstrip(")")
tmp = temp.replace('Untuk Kota Banjarmasin GMT +8', 'Untuk Kota Banjarmasin (GMT +8)').strip()
print(f"Tanggal {current_time.day} {date}, {tmp}")

data = response.find_all('tr', 'table_highlight')
data = data[0]

shalat = {}
i = 0
for j in data:
    if i == 1:
        shalat['subuh'] = j.get_text()
    elif i == 2:
        shalat['dzuhur'] = j.get_text()
    elif i == 3:
        shalat['ashar'] = j.get_text()
    elif i == 4:
        shalat['maghrib'] = j.get_text()
    elif i == 5:
        shalat['isya'] = j.get_text()
    i += 1
print("Jadwal Shalat: ")
print(f"Shalat Shubuh: {shalat['subuh']}")
print(f"Shalat Dzuhur: {shalat['dzuhur']}")
print(f"Shalat Ashar: {shalat['ashar']}")
print(f"Shalat Maghrib: {shalat['maghrib']}")
print(f"Shalat Isya: {shalat['isya']}")

