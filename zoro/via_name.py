import requests
from bs4 import BeautifulSoup


class ZoroViaName:
    def __init__(self):
        self.base_url = 'https://zoro.to'
        self.search_path = '/search?keyword='

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

    def _get_duration_and_type(self, div):
        try:
            detail_div = div.find('div', class_='film-detail')
            duration_elem = detail_div.find('span', class_='fdi-item fdi-duration')
            duration = duration_elem.text.strip()
            type_elem = detail_div.find('span', class_='fdi-item').find_next('span', class_='fdi-item')
            typee = type_elem.text.strip()
            return duration, typee
        except AttributeError as e:
            print(f"AttributeError: {e}")
        return None, None
    
    def _get_description(self, url):
        try:
            c  = self._get_soup(url)
            desc = c.find('div', {"class" : "anis-content"}).find('div', {'class': 'film-description m-hide'}).div.string
            s = desc.replace('\n', '').replace('\r', '').replace('\t', '').replace('  ', '')
            
            return s
        except:
            return ' '
            
        
    def search_(self, keyword):
        try:
            search_url = self.base_url + self.search_path + keyword.replace(' ', '+')
            soup = self._get_soup(search_url)
            results = []

            for item in soup.find_all('div', class_='flw-item'):
                poster, episodes = self._get_poster_and_episodes(item)
                title, url = self._get_title_and_url(item)
                duration, typee = self._get_duration_and_type(item)
                results.append({'title': title, 'url': url, 'poster': poster, 'episodes': episodes, 'duration': duration, 'type': typee})
                
            return results
        except Exception as e:
            print(f"An error occurred: {e}")
        return None
    
    def search_desc(self,keyword):
        try:
            search_url = self.base_url + self.search_path + keyword.replace(' ', '+')
            soup = self._get_soup(search_url)
            results = []
            
            for item in soup.find_all('div', class_='flw-item'):
                poster, episodes = self._get_poster_and_episodes(item)
                title, url = self._get_title_and_url(item)
                duration, typee = self._get_duration_and_type(item)
                try:
                    description = self._get_description(url)
                except:
                    description = ' '
                results.append({'title': title, 'url': url, 'poster': poster, 'episodes': episodes, 'duration': duration, 'type': typee , 'description': description})
                
            return results
        except Exception as e:
            print(f"An error occurred: {e}")
        return None
        
    
    
    
# z = ZoroViaName()
# print(z.search('Overflow'))