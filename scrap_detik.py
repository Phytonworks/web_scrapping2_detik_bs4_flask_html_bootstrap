import requests
import bs4

url = 'https://www.detik.com/terpopuler?tag_from=wp_cb_mostPopular_more'
contents = requests.get('https://www.detik.com/terpopuler', params={'tag_from': 'wp_cb_mostPopular_more'})
response = bs4.BeautifulSoup(contents.text, features='html.parser')
data = response.find(attrs={'class': 'grid-row list-content'})

judul = data.findAll(attrs={'class': 'media__title'})
gambar = data.findAll(attrs={'class': 'media__image'})


for judul in judul:
    print(judul.text)

for gambar in gambar:
    print(gambar.find('a').find('img')['title'])

