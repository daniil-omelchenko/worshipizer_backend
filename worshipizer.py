from functools import partial

from flask import Flask
from flask import request
from flask_cors import CORS

import logic


app = Flask(__name__)
CORS(app)

app.get = partial(app.route, methods=['GET'])
app.post = partial(app.route, methods=['POST'])
app.put = partial(app.route, methods=['PUT'])
app.delete = partial(app.route, methods=['DELETE'])


@app.post('/api/song')
def create_song():
    song_data = request.get_json()
    return logic.save_song(song_data)


@app.get('/api/song/<song_id>')
def get_song(song_id):
    return logic.get_song(song_id)


@app.delete('/api/song/<song_id>')
def delete_song(song_id):
    return logic.delete_song(song_id)


@app.put('/api/song/<song_id>')
def update_song(song_id):
    updated_song_data = request.get_json()
    return logic.update_song(song_id, updated_song_data)


@app.get('/api/song/search')
def search_song():
    query = request.args.to_dict().get('query')
    return logic.search_song(query)
