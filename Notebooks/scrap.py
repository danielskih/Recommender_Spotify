from bs4 import BeautifulSoup
import requests
import pandas as pd
def extract_abc(string):
    k = ''
    for i in string:
        if i.isalpha() or i in [' ',',','&']:
            k += i
    return k
url = 'https://www.billboard.com/charts/hot-100/'
response = requests.get(url)
#response.content
response.status_code
soup = BeautifulSoup(response.content, 'html.parser')
songs = [extract_abc(i.get_text()) for i in soup.select(".c-title.a-no-trucate")]
artists = [extract_abc(i.get_text()) for i in soup.select(".c-label.a-no-trucate")]
d = {'artist':artists, 'song':songs}
df = pd.DataFrame(data=d)
df.to_csv('../Data/bllbrd_top_100')