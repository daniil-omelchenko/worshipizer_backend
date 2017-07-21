import json
import uuid

import db


def error(msg, status_code):
    return response({'error': msg, 'status_code': status_code}, status_code)


def message(msg, status_code=200):
    return response({'message': msg, 'status_code': status_code}, status_code)


def response(data=None, status_code=200):
    data = data or {}
    return json.dumps(data), status_code, {'Content-Type': 'application/json'}


def get_song(song_id):
    song = db.song.find_one({'_id': song_id})
    if song:
        return response(song)
    else:
        return error('Song not found.', 404)


def save_song(song):
    song['_id'] = uuid.uuid4().hex
    song_id = db.song.insert_one(song).inserted_id
    return response({'message': 'Song created.', 'song_id': song_id})


def delete_song(song_id):
    count = db.song.delete_one({'_id': song_id}).deleted_count
    if count:
        return message('Song was deleted.')
    else:
        return error('Song not found.', 404)


def update_song(song_id, new_song):
    count = db.song.update_one({'_id': song_id}, {'$set': new_song})
    if count:
        return message('Song was updated.')
    else:
        return error('Song not found.', 404)


def search_song(query):
    if not query:
        return error('Empty search parameter.', 400)
    songs = []
    for song in db.song.find({'$text': {'$search': query}}):
        songs.append({
            '_id': song['_id'],
            'title': song['metaData']['title']
        })
    return response({'songs': songs})
