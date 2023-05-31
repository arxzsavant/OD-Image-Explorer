from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
import urllib.parse

app = Flask(__name__)

@app.route('/')
def home():
    url = 'https://www.dkpminus.com/wp-content/uploads/2019/08/?SD'  # Replace with your URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    img_urls = []

    for link in soup.find_all('a'):
        file_url = urllib.parse.urljoin(url, link.get('href'))
        if file_url.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
            img_urls.append(file_url)

    return render_template('index.html', img_urls=img_urls)


if __name__ == '__main__':
    app.run(debug=True)
