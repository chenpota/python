#!/usr/bin/env python3

import connexion


app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yaml')
app.run(host='127.0.0.1', port=8000)
