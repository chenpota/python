# Dependency packages

pip3 install flask
pip3 install requests

# curl

## GET (read)

	curl -i http://127.0.0.1:8000/players
	curl -i http://127.0.0.1:8000/players/0

## POST (create)

	curl -X POST -H "Content-Type: application/json" -d '{"name":"Grant Hill", "score":90}' -i http://127.0.0.1:8000/players

## DELETE (remove)

	curl -X DELETE -i http://127.0.0.1:8000/players/0

## PUT (replace)

	curl -X PUT -H "Content-Type: application/json" -d '{"name":"Penny Hardaway", "score":80}' -i http://127.0.0.1:8000/players/1

## PATCH (update)

	curl -X PATCH -H "Content-Type: application/json" -d '{"score":70}' -i http://127.0.0.1:8000/players/1

# Reference

[1] http://flask.pocoo.org/docs/0.12/

[2] http://docs.python-requests.org/en/master/
