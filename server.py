from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
	return render_template('hello.tpl')


@app.route("/", methods=["POST"])
def make_appointment():
	
	print request.form['name'], request.form['email'], request.form['nailtype']
# @app.route("/person/<string:name>" methods=["GET"])
# def person(name):
# 	return render_template('hello.tpl', name=name)
# @app.route("/person/<string:name>", methods=["POST"])
# def post_person(name):
# 	return render_template('hello.tpl', name=name)
if __name__ == "__main__":
    app.run()