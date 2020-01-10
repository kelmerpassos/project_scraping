from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup


def gethtml(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    except URLError as e:
        return None
    bs = BeautifulSoup(html, 'lxml')
    return bs


def gettitle(url):
        bs = gethtml(url)
        try:
            title = bs.title
        except AttributeError:
            title = None
        return title


titulo = gettitle('http://pythonscraping.com/pages/page1.html')
if titulo:
    print(titulo.get_text())
