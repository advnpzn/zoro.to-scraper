import requests
from bs4 import BeautifulSoup
import json

class ZoroGenre:
    def __init__(self,genre):
        self.base_url = 'https://zoro.to'
        self.genre_list =  ['Action', 'Adventure', 'Cars', 'Comedy', 'Dementia', 'Demons', 'Drama', 'Ecchi', 'Fantasy', 'Game', 'Harem', 'Historical', 'Horror', 'Isekai', 'Josei', 'Kids', 'Magic', 'Martial Arts', 'Mecha', 'Military', 'Music', 'Mystery', 'Parody', 'Police', 'Psychological', 'Romance', 'Samurai', 'School', 'Sci-Fi', 'Seinen', 'Shoujo', 'Shoujo Ai', 'Shounen', 'Shounen Ai', 'Slice of Life', 'Space', 'Sports', 'Super Power', 'Supernatural', 'Thriller', 'Vampire']
        if genre.capitalize() not in self.genre_list:
            raise ValueError(f'{genre} is not a valid genre. Please choose from {self.genre_list}')
        self.genre = genre
        self.genres = {
            'Action': 'https://zoro.to/genre/action',
            'Adventure': 'https://zoro.to/genre/adventure',
            'Cars': 'https://zoro.to/genre/cars',
            'Comedy': 'https://zoro.to/genre/comedy',
            'Dementia': 'https://zoro.to/genre/dementia',
            'Demons': 'https://zoro.to/genre/demons',
            'Drama': 'https://zoro.to/genre/drama',
            'Ecchi': 'https://zoro.to/genre/ecchi',
            'Fantasy': 'https://zoro.to/genre/fantasy',
            'Game': 'https://zoro.to/genre/game',
            'Harem': 'https://zoro.to/genre/harem',
            'Historical': 'https://zoro.to/genre/historical',
            'Horror': 'https://zoro.to/genre/horror',
            'Isekai': 'https://zoro.to/genre/isekai',
            'Josei': 'https://zoro.to/genre/josei',
            'Kids': 'https://zoro.to/genre/kids',
            'Magic': 'https://zoro.to/genre/magic',
            'Martial Arts': 'https://zoro.to/genre/martial-arts',
            'Mecha': 'https://zoro.to/genre/mecha',
            'Military': 'https://zoro.to/genre/military',
            'Music': 'https://zoro.to/genre/music',
            'Mystery': 'https://zoro.to/genre/mystery',
            'Parody': 'https://zoro.to/genre/parody',
            'Police': 'https://zoro.to/genre/police',
            'Psychological': 'https://zoro.to/genre/psychological',
            'Romance': 'https://zoro.to/genre/romance',
            'Samurai': 'https://zoro.to/genre/samurai',
            'School': 'https://zoro.to/genre/school',
            'Sci-Fi': 'https://zoro.to/genre/sci-fi',
            'Seinen': 'https://zoro.to/genre/seinen',
            'Shoujo': 'https://zoro.to/genre/shoujo',
            'Shoujo Ai': 'https://zoro.to/genre/shoujo-ai',
            'Shounen': 'https://zoro.to/genre/shounen',
            'Shounen Ai': 'https://zoro.to/genre/shounen-ai',
            'Slice of Life': 'https://zoro.to/genre/slice-of-life',
            'Space': 'https://zoro.to/genre/space',
            'Sports': 'https://zoro.to/genre/sports',
            'Super Power': 'https://zoro.to/genre/super-power',
            'Supernatural': 'https://zoro.to/genre/supernatural',
            'Thriller': 'https://zoro.to/genre/thriller',
            'Vampire': 'https://zoro.to/genre/vampire'
            }
        self.genre_url = self.genres[self.genre]
        
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
    
    def Search(self):
        self.soup = self._get_soup(self.genre_url)
        results = []

        for item in self.soup.find_all('div', class_='flw-item'):
            poster, episodes = self._get_poster_and_episodes(item)
            title, url = self._get_title_and_url(item)
            
            results.append({'title': title, 'url': url, 'poster': poster, 'episodes': episodes})
            
        return results
    
    
# z = ZoroGenre('Action')
# print(z.Search())