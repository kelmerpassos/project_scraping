from urllib.error import HTTPError, URLError
from urllib.request import urlopen

from bs4 import BeautifulSoup


def gethtml(url):
    try:
        html = urlopen(url)
    except HTTPError:
        return None
    except URLError:
        return None
    return BeautifulSoup(html, 'lxml')


def getnames(url):
    bs = gethtml(url)
    return bs.find_all(attrs={'id': 'text'})


names = getnames('http://pythonscraping.com/pages/warandpeace.html')
print(len(names))
for name in names:
    print(name.get_text())
