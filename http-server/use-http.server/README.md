# Create server.pem

openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes

openssl x509 -outform pem -in server.pem -out mycert.crt

# curl
curl --cacert mycert.crt https://127.0.0.1:8000

# Reference

[1] https://docs.python.org/3.5/library/http.server.html
