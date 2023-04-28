import requests
from bs4 import BeautifulSoup
import json

class ZoroRecent:
    def __init__(self):
        self.base_url = 'https://zoro.to'
        self.trending_path = '/recently-updated'
        
    def _get_soup(self, url):
        response = requests.get(url)
        return BeautifulSoup(response.content, 'html.parser')

    def _get_poster_and_episodes(self, div):
        try:
            poster_k = 'film-poster'
            poster = div.find('div', class_=poster_k)
            img = 'data-src'
            episodes_div = poster.find('div', class_='tick ltr')
            episodes = episodes_div.find('div', class_='tick-item tick-sub').text
            return poster.find('img')[img], episodes
        except AttributeError as e:
            print(f"AttributeError: {e}")
        return None, None

    def _get_title_and_url(self, div):
        try:
            title_div = div.find('div', class_='film-detail')
            title_elem = title_div.find('a')
            title = title_elem.text.strip()
            url = self.base_url + title_elem['href']
            return title, url
        except AttributeError as e:
            print(f"AttributeError: {e}")
        return None, None  
    
    def latest_eps(self):
        self.soup = self._get_soup(self.base_url + self.trending_path)
        results = []

        for item in self.soup.find_all('div', class_='flw-item'):
            poster, episodes = self._get_poster_and_episodes(item)
            title, url = self._get_title_and_url(item)
            
            results.append({'title': title, 'url': url, 'poster': poster, 'episodes': episodes})
            
        return results
    
    
# z = ZoroRecent()
# print(z.latest_eps())