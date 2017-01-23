#!/usr/bin/env python3

from flask import Flask, abort, jsonify, request


app = Flask(__name__)

players = [
    {
        'pid': 0,
        'name': 'Michanel Jordan',
        'score': 100
    }
]
player_id = 1


@app.route('/players', methods=['GET'])
def get_players():
    global players
    return jsonify({'players': players}), 200


@app.route('/players/<int:pid>', methods=['GET'])
def get_player(pid):
    global player_id, players

    for player in players:
        if player['pid'] == pid:
            return jsonify({'player': player}), 200

    abort(404)


@app.route('/players', methods=['POST'])
def create_player():
    if (not request.json) or \
       (not 'name' in request.json) or \
       (not 'score' in request.json):
        abort(400)

    global player_id, players

    player = {
        'pid': player_id,
        'name': request.json['name'],
        'score': request.json['score']
    }

    players.append(player)

    player_id += 1

    return jsonify({'player': player}), 201


@app.route('/players/<int:pid>', methods=['DELETE'])
def delete_player(pid):
    index = 0

    global players

    for player in players:
        if player['pid'] == pid:
            del players[index]
            return jsonify({'result': True}), 200

        index += 1

    abort(404)


@app.route('/players/<int:pid>', methods=['PUT'])
def replace_player(pid):
    if (not request.json) or \
       (not 'name' in request.json) or \
       (not 'score' in request.json):
        abort(400)

    global players

    for player in players:
        if player['pid'] == pid:
            player['name'] = request.json.get('name')
            player['score'] = request.json.get('score')
            return jsonify({'player': player}), 200

    abort(404)


@app.route('/players/<int:pid>', methods=['PATCH'])
def update_player(pid):
    if (not request.json) or \
       ((not 'name' in request.json) and (not 'score' in request.json)):
        abort(400)

    global players

    for player in players:
        if player['pid'] == pid:
            player['name'] = request.json.get('name', player['name'])
            player['score'] = request.json.get('score', player['score'])
            return jsonify({'player': player}), 200

    abort(404)


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=8000,
        debug=True
    )
