#!/usr/bin/env python3

import requests
import json


def get_players():
    print("----Get all players---------")
    rsp = requests.get(url='http://127.0.0.1:8000/players')
    print(rsp.text)


def create_player(name, score):
    print("----insert new player-------")
    rsp = requests.post(url='http://127.0.0.1:8000/players',
                        json={'name': name, 'score': score})
    print(rsp.text)


def get_player(id):
    print("----Get player--------------")
    rsp = requests.get(url='http://127.0.0.1:8000/players/' + str(id))
    print(rsp.text)


def delete_player(id):
    print("----Delete player-----------")
    rsp = requests.delete(url='http://127.0.0.1:8000/players/' + str(id))
    print(rsp.text)


def update_player(id, data):
    print("----Update player-----------")
    rsp = requests.patch(url='http://127.0.0.1:8000/players/' + str(id),
                         json=data)
    print(rsp.text)


def replace_player(id, name, score):
    print("----Replace player----------")
    rsp = requests.put(url='http://127.0.0.1:8000/players/' + str(id),
                       json={'name': name, 'score': score})
    print(rsp.text)


def main():
    get_players()
    get_player(0)
    get_player(1)
    create_player('Scottie Pippen', 95)
    get_players()
    get_player(1)
    update_player(1, {'score': 99})
    get_players()
    replace_player(0, 'Steve Kerr', 80)
    get_players()
    delete_player(0)
    get_players()


if __name__ == '__main__':
    main()
