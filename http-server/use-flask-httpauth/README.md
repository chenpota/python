# Dependency packages

pip3 install flask flask-httpauth Werkzeug

# curl basic-auth

	$ curl -u username:password http://localhost:5000

# curl digest-auth

	$ curl --digest -u username:password http://localhost:5000

Fail

# Reference

[1] http://flask.pocoo.org/docs/0.12/

[2] https://flask-httpauth.readthedocs.io/en/latest/

# Note
* Logout only when closing browser or requesting http://error-username:error-password@localhost:5000
