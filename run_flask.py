import requests
import bs4
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detik-populer')
def detik_populer() :
    url = 'https://www.detik.com/terpopuler?tag_from=wp_cb_mostPopular_more'

    contents = requests.get('https://www.detik.com/terpopuler', params={'tag_from': 'wp_cb_mostPopular_more'})

    response = bs4.BeautifulSoup(contents.text, features='html.parser')

    data = response.find(attrs={'class': 'grid-row list-content'})

    judul = data.findAll(attrs={'class': 'media__title'})
    gambar = data.findAll(attrs={'class': 'media__image'})

    return render_template('index.html', gambar=gambar)






if __name__ == '__main__':
    app.run(debug=True)
