# Create server.pem

openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes

# Reference

[1] https://docs.python.org/3.5/library/http.server.html
