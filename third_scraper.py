import re
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

from bs4 import BeautifulSoup


def get_html(url):
    try:
        html = urlopen(url)
    except HTTPError:
        return None
    except URLError:
        return None
    return BeautifulSoup(html.read(), 'html.parser')


def get_children_table(url):
    bs = get_html(url)
    return bs.find('table', {'id': 'giftList'}).children


def get_next_siblings(url):
    bs = get_html(url)
    return bs.find('table', {'id': 'giftList'}).tr.next_siblings


def get_father(url):
    bs = get_html(url)
    return bs.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text()


def get_img(url):
    bs = get_html(url)
    return bs.find_all('img', {'src': re.compile('\.\.\/img\/gifts\/img[1-9]*\.jpg')})


def get_lambda(url):
    bs = get_html(url)
    return bs.find_all(lambda tag: len(tag.attrs) == 2)


option = input('Digite a opção:')
URL = 'http://pythonscraping.com/pages/page3.html'
if option == '1':
    resp_list = get_children_table(URL)
    for resp in resp_list:
        print(resp)
elif option == '2':
    resp_list = get_father(URL)
    print(resp_list)
elif option == '3':
    resp_list = get_next_siblings(URL)
    for resp in resp_list:
        print(resp)
elif option == '4':
    resp_list = get_img(URL)
    for resp in resp_list:
        print(resp.attrs['src'])
elif option == '5':
    resp_list = get_lambda(URL)
    for resp in resp_list:
        print(resp)


