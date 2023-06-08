import random
import string
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

url_database = {}

def generate_short_url():
    characters = string.ascii_letters + string.digits
    while True:
        short_url = ''.join(random.choice(characters) for _ in range(6))
        if short_url not in url_database:
            return short_url

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['url']
        short_url = generate_short_url()
        url_database[short_url] = original_url
        return render_template('index.html', short_url=short_url)
    return render_template('index.html')

@app.route('/<short_url>')
def redirect_url(short_url):
    if short_url in url_database:
        original_url = url_database[short_url]
        return redirect(original_url)
    else:
        return "Invalid URL"

if __name__ == '__main__':
    app.run(debug=True)
