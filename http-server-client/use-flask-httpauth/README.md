# Dependency packages

	$ apt-get install httpie curl wget

	$ pip3 install flask flask-httpauth Werkzeug requests

# curl basic-auth

	$ curl -u username:password http://localhost:5000

	$ http --auth-type basic -a username:password http://localhost:5000

# curl digest-auth

	$ wget http://localhost:5000 --http-user=username --http-password=password

	$ http --auth-type digest -a username:password http://localhost:5000

	$ curl --digest -u username:password http://localhost:5000

curl is failed.

	$ 

# Reference

[1] http://flask.pocoo.org/docs/0.12/

[2] https://flask-httpauth.readthedocs.io/en/latest/

# Note
* Logout only when closing browser or requesting http://error-username:error-password@localhost:5000
