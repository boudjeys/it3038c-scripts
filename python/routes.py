from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def hello():
	#myName = 'AJ'
	return render_template("index.html")
	#, name=myName)

@app.route('/welcome', methods=['POST'])
def welcome():
	return render_template("welcome.html", myName=request.form["myName"])
