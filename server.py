from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('hello.tpl')

@app.route("/person/<string:name>" methods=["GET"])
def person(name):
	return render_template('hello.tpl', name=name)
@app.route("/person/<string:name>", methods=["POST"])
def post_person(name):
	return render_template('hello.tpl', name=name)
if __name__ == "__main__":
    app.run()