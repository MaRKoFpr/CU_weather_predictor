from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = "uPjJem1EeTvZ6yMFa8yGUtewIUEQgfWV"
BASE_URL = "http://dataservice.accuweather.com"

@app.route('/')
def index():
    return 'hello  world'

if __name__ == "__main__":
    app.run(debug=True)
