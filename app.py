from flask import Flask,render template

app = Flask(__name__)

@app.route('/')
def index():
  name = 'kay khine'
  return render_template('index.html',name = name)
