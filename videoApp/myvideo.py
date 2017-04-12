from flask import Flask, render_template, request

import os


from videoApp.api.omdbAPI import Omdb_Movie
from videoApp.api.vimeoAPI import vimeo_Movie

from videoApp.api.api_manager import API_Manager
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    keyword = request.form.get('keyword')

    #TODO make this modular

    api_clients = API_Manager()
    api_clients_responses = api_clients.search(keyword)


    return render_template('result.html', result=api_clients_responses, search = keyword)


if __name__ == "__main__":
    app.run()
