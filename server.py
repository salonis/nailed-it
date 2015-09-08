from flask import Flask, render_template, request, redirect
app = Flask(__name__)


appointments = []

@app.route("/", methods=["GET"])
def hello():
	return render_template('hello.tpl')


@app.route("/", methods=["POST"])
def make_appointment():
	appointments.append((request.form['name'], request.form['email'], request.form['nailtype']))
	print request.form['name'], request.form['email'], request.form['nailtype']
	return redirect("confirmation/%d/" % (len(appointments) - 1), code=302)

@app.route("/confirmation/<int:id>/", methods=["GET"])
def confirmation(id):
	appt = appointments[id]
	return render_template('confirmation.tpl', 
		name=appt[0], email=appt[1], nailtype=appt[2])

# @app.route("/person/<string:name>" methods=["GET"])
# def person(name):
# 	return render_template('hello.tpl', name=name)
# @app.route("/person/<string:name>", methods=["POST"])
# def post_person(name):
# 	return render_template('hello.tpl', name=name)
if __name__ == "__main__":
    app.run(debug=True)