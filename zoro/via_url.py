import requests
from bs4 import BeautifulSoup
import json

class ZoroViaUrl:
    def __init__(self):
        self.base_url = 'https://zoro.to'

    def _get_soup(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'html.parser')
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Connection Error: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Something went wrong: {err}")
        return None

    def _get_name(self,soup):
        name = soup.find('h2',class_='film-name dynamic-name').text
        return name
    
    def _get_poster(self,soup):
        image = soup.find('img',class_='film-poster-img')['src']
        return image
    
    def _get_genre(self,soup):
        genre = soup.find('div',class_='item item-list').text
        return genre.replace('\n', ' ').replace('\r', '').replace('\t', '').replace('  ', '').replace('Genres: ', '')
    
    def _get_description(self,soup):
        desc = soup.find('div',class_='text').text
        return desc.replace('\n', '').replace('\r', '').replace('\t', '').replace('  ', '')
    
    def _get_watch(self,soup):
        watch = soup.find('a',class_='btn btn-radius btn-primary btn-play')['href']
        return watch
    
    def _get_watch2gether(self,soup):
        watch = soup.find('a',class_='btn btn-watch2gether')['href']
        return watch
        
    
    def Search(self,url):
        self.url = url
        self.soup = self._get_soup(self.url)
        name = self._get_name(self.soup)
        image = self._get_poster(self.soup)
        desc = self._get_description(self.soup)
        genre = self._get_genre(self.soup).strip()
        watch = self.base_url + self._get_watch(self.soup)
        try:
            watch2gether = self.base_url + self._get_watch2gether(self.soup)
        except:
            pass
        
        return json.dumps({'name':name,'image':image,'description':desc,'genre':genre,'watch':watch })
        
        
        
        
# z = ZoroViaUrl()
# print(z.Search('https://zoro.to/one-piece-movie-1-3096?ref=search'))