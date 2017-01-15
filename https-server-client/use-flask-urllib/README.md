# Dependency packages

pip3 install flask

# Create certificate files

    openssl req -new -x509 -keyout server.key -out server.pem -days 365 -nodes -subj '/C=TW/ST=Taiwan/L=Taipei/CN=127.0.0.1/emailAddress=test@test.com'

# curl
curl -i --cacert server.pem https://127.0.0.1:8000

# Reference

[1] http://flask.pocoo.org/docs/0.12/

[2] https://docs.python.org/3.5/library/urllib.html

[3] https://docs.python.org/3.5/library/email.message.html#email.message.Message

[4] https://docs.python.org/3.5/library/json.html
