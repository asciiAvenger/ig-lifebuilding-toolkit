from flask import Flask
from quotes_model import QuotesModel
import json

model = QuotesModel()
model.load_model('model.json')

app = Flask(__name__)

@app.route('/')
def index():
    return 'temp index page'

@app.route('/quote')
def quote():
    quote = model.generate()
    return json.dumps({'quote': quote})

app.run(debug=True)