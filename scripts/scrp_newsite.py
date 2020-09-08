from bs4 import BeautifulSoup
import requests
import logging

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# retry methods
logging.basicConfig(level=logging.DEBUG)
s = requests.Session()
retries = Retry(total=1000, backoff_factor=1, status_forcelist=[ 502, 503, 504 ])
s.mount('http://', HTTPAdapter(max_retries=retries))

start_seat = 0
end_seat = 10000000
file = open("../raw_data/out.txt", "a")

for k in range(start_seat, end_seat):  
    url = "https://nezakr.qalubiaedu.org/?t=num&k=" + str(k)
    page = s.get(url).text

    soup = BeautifulSoup(page, 'html.parser')
    lst = []
    for link in soup.find_all('td'):
        lst.append(link.get_text().strip())

    if len(lst) > 20 :
        for i in range(1, 20, 2):
            file.write(lst[i] + ",")

        for i in range(20, len(lst), 1):
            if lst[i] == "اللغة العربية (80)" or  lst[i] == "اللغة الإنجليزية (50)" or \
                lst[i] == "اللغة الأجنبية الثانية (40)" or  lst[i] == "الفيزياء (60)" or \
                lst[i] == "الكيمياء (60)" or  lst[i] == "الأحياء (60)" or \
                lst[i] == "الفلسفة والمنطق (60)" or  lst[i] == "علم النفس (60)" or \
                lst[i] == "التاريخ (60)" or  lst[i] == "الجغرافيا (60)" or \
                lst[i] == "الرياضيات 1 (60)" or  lst[i] == "الرياضيات 2 (60)" or \
                lst[i] == "الچيولوچيا (60)" or  lst[i] == "التربية الدينية (25)" or \
                lst[i] == "اللغة الأجنبية الثانية (40)" or  lst[i] == "الفيزياء (60)" or \
                lst[i] == "الاقتصاد والإحصاء (50)" or  lst[i] == "التربية الوطنية (25)":
                file.write(lst[i+1] + ",")
        file.write("\n")
file.close()
