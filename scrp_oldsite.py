from bs4 import BeautifulSoup
import urllib.request, urllib.parse
import ssl
import requests
import logging

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def print_headers(file):
    lst = [ "Name", "Seat No.", "School", "Mangement", "Gover.", "Sum","Percentage",    \
            "Status", "Major", "Num of fails", "Arabic", "English", "Forign", "Physics" ,\
            "Chemistry", "Biology", "Gology", "religion", "Economy", "Watina"]
    for item in lst:
        file.write(item + ",") 
    file.write("\n")

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# retry methods
logging.basicConfig(level=logging.DEBUG)
s = requests.Session()
retries = Retry(total=1000, backoff_factor=1, status_forcelist=[ 502, 503, 504 ])
s.mount('http://', HTTPAdapter(max_retries=retries))

start_seat = 0
end_seat = 10000000

file = open("out.txt", "a")
# print_headers(file)

for k in range(start_seat, end_seat):
    url = "https://nezakr.qalubiaedu.org/?t=num&k=" + str(k)
    page = s.get(url).text

    soup = BeautifulSoup(page, 'html.parser')
    lst = []
    for link in soup.find_all('td'):
        lst.append(link.get_text().strip())
    # filter the fields
    if len(lst) > 20 :
        for i in range(0, 20, 2):
            if i % 2 == 1:
                file.write(lst[i] + ",")
        for i in range(29, len(lst)-3, 3):
            if i % 3 == 0:
                file.write(lst[i] + ",")
        file.write("\n")
    if k % 20 == 0:
        print("Progress:", k)
file.close()

