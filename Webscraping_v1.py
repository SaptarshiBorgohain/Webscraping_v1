#import the libaries 1st.

from urllib.request import urlopen
from bs4 import BeautifulSoup

#change the url with the page you want to scrape information.

url = "https://www.bbc.com/news/technology-52815552"

#Try run open the url. Most website block this. Will be updating the code to overcome this.
 
try:
    page = urlopen(url)
except:
    print("Error opening url")

soup = BeautifulSoup(page, 'html.parser')
content = soup.find('div', {"class": "story-body"}) #Ok now open the inspect page in chrome and find the "div" and then the class of the needed information. Then paste the class name here inside the "..".

article = ''
for i in content.findAll('p'):
    article = article + '' + i.text
print(article)

#Happy scraping!!
