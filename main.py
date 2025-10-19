import requests
from bs4 import BeautifulSoup
from datetime import datetime

'''
News12 The Bronx is one of the most reliable sites for local news
The first site for news web scrapping
'''

'''
Display Current Date and Local Time:
Today's Date: <Month Name> <Date>, <YYYY>
Local Time: XX:XX XM
'''
def time():
    current_time = datetime.now()
    display_date = current_time.strftime("%B %d, %Y")
    local_time = current_time.strftime("%I:%M %p")

    print(f"Today's Date: {display_date}")
    print(f"Local Time: {local_time}")

site_name_news12 = 'News12 The Bronx'
news12_bronx_url = 'https://bronx.news12.com/category/bronx-news'

response = requests.get(news12_bronx_url)

if response.status_code == 200:
    print(f'Successfully connected to the site: {site_name_news12}')
    print('=' * 40)
else:
    print(f'Couldnt connect to the site: {site_name_news12}. Check for issues.')
    exit()

content = response.content

# Organized the HTML content structure of News12 site
organized_news = BeautifulSoup(content, 'html.parser')

print(f'Local News: {site_name_news12}')
time()
print('=' * 40)

headlines = organized_news.find_all('div', {'data-testid': 'category-card'})


print(f'Top {len(headlines)} Headlines:')

for i, headline in enumerate(headlines, start=1):
    headline_tag = headline.find('p', {'class': 'card-title'})
    headline_text = headline_tag.get_text().strip()

    print(i, headline_text)