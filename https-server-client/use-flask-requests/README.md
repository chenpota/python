# Dependency packages

pip3 install flask
pip3 install requests

# Create certificate files

openssl req -new -x509 -keyout server.key -out server.pem -days 365 -nodes -subj '/C=TW/ST=Taiwan/L=Taipei/CN=127.0.0.1/emailAddress=test@test.com'

# curl
curl -i --cacert server.pem https://127.0.0.1:8000

# Reference

[1] http://flask.pocoo.org/docs/0.12/

[2] http://docs.python-requests.org/en/master/
