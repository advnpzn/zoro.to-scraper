import requests
from bs4 import BeautifulSoup
import lxml
import json
from pprint import pprint



class Zoro:


    def __init__(self) -> None:
        self.__url = "https://zoro.to/"
        self.__search = "search?keyword="


    def __request(self, uri):

        try:
            res = requests.get(self.__url+uri)
            return res.content
        except Exception:
            print("error")


    def search(self, query: str)-> list:

        animeListRes = self.__request(self.__search+query)
        soup = BeautifulSoup(animeListRes, 'lxml')

        __animeList = []

        for i in soup.find_all('div', {"class":"flw-item"}):
            img = i.img['data-src']
            name = i.find('a', {'class':'dynamic-name'})
            href = self.__url+"watch"+name['href']
            name = name.string
            __animeList.append({"name": name, "poster": img, "watch_url": href})
        
        return __animeList


        
a = Zoro()
pprint(a.search(input("Enter Anime Name : ")))

