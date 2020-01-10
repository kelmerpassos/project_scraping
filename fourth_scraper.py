from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen('https://pt.wikipedia.org/wiki/Batalha_de_Tuiuti')
bs = BeautifulSoup(html.read(), 'html.parser')
links = bs.find_all(lambda tag: tag == 'a')

