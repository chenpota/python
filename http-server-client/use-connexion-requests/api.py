#!/usr/bin/env python3

from connexion import NoContent, abort, request

players = [
    {
        'pid': 0,
        'name': 'Michanel Jordan',
        'score': 100
    }
]
player_id = 1

PETS = {}


def get_players():
    return players, 200


def get_player(pid):
    global player_id, players

    for player in players:
        if player['pid'] == pid:
            return player, 200

    abort(404)


def create_player():
    global player_id, players

    player = {
        'pid': player_id,
        'name': request.json['name'],
        'score': request.json['score']
    }

    players.append(player)

    player_id += 1

    return player, 201


def delete_player(pid):
    index = 0

    global players

    for player in players:
        if player['pid'] == pid:
            del players[index]
            return NoContent, 204

        index += 1

    abort(404)


def replace_player(pid):
    global players

    for player in players:
        if player['pid'] == pid:
            player['name'] = request.json.get('name')
            player['score'] = request.json.get('score')
            return player, 200

    abort(404)


def update_player(pid):
    global players

    for player in players:
        if player['pid'] == pid:
            player['name'] = request.json.get('name', player['name'])
            player['score'] = request.json.get('score', player['score'])
            return player, 200

    abort(404)
