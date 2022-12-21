from bs4 import BeautifulSoup
import requests
import lxml

class ZoroAnime:

    def __init__(self, title: str, watch_url: str, poster: str) -> None:
        self.title = title
        self.watch_url = watch_url
        self.poster = poster
        self.description = self.__get_description()


    def __get_description(self) -> str:

        res = requests.get(self.watch_url).content

        soup = BeautifulSoup(res, 'lxml')

        try:
            desc = soup.find('div', {"class" : "anis-content"}).find('div', {'class': 'film-description m-hide'}).div.string
            return desc
        except Exception as e:
            print(e)
            exit
        

