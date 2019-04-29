#!/usr/bin/python3
"""main app file for Flask instance in REST API
"""
from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext():
    """called on teardown of app contexts of flask
    """
    storage.close()

if __name__ == "__main__":
    """run the app if the script is not being imported
    """
    fetched_host = os.environ.get('HBNB_API_HOST')
    fetched_port = os.environ.get('HBNB_API_PORT')
    if fetched_host is None:
        fetched_host = '0.0.0.0'
    if fetched_port is None:
        fetched_port = 5000
    app.run(host=fetched_host, port=fetched_port, threaded=True)
