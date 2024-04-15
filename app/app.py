from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def home():
	return json.dumps({'result': 'IPV6-KM'})

if __name__== "__main__":
	app.run(host='::',port=80)
