import imp
from portfolio import app

@app.route('/')
def index():
    return 'Homepage'

