import requests
import bs4
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('base.html')

@app.route('/detik-populer')
def detik_populer() :
    url = 'https://www.detik.com/terpopuler?tag_from=wp_cb_mostPopular_more'
    contents = requests.get('https://www.detik.com/terpopuler', params={'tag_from': 'wp_cb_mostPopular_more'})

    response = bs4.BeautifulSoup(contents.text, features='html.parser')
    data = response.find(attrs={'class': 'grid-row list-content'})

    judul = data.findAll(attrs={'class': 'media__title'})
    gambar = data.findAll(attrs={'class': 'media__image'})

    return render_template('detik-scraper.html', gambar=gambar)

@app.route('/idr-rates')
def idr_rates():
    source = requests.get(url='http://www.floatrates.com/daily/usd.json')
    json_data = source.json()
    return render_template('idr-rates.html', datas = json_data.values())





if __name__ == '__main__':
    app.run(debug=True)
