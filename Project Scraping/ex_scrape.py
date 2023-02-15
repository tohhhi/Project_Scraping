import requests
from bs4 import BeautifulSoup
import pprint

home = 'news'
page2 = '?p=2'
page3 = '?p=3'

res = requests.get(f'https://news.ycombinator.com/{page3}')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline')
subtext = soup.select('.subtext')

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.find('a')['href']
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
        
        if points > 99:
            
            hn.append({'title':title, 'links':href, 'votes': points})
            
    
    return sort_stories_by_votes(hn)

#create_custom_hn(links, votes)


pprint.pprint(create_custom_hn(links, subtext))