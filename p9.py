# Flask URL Binding
# -------------------
# url_for() 

from flask import Flask 

obj=Flask(__name__) 

@obj.route("/aboutus")
def f1():
	return "<h1>About us message</h1>"

@obj.route("/home")
def f2():
	return "<h2>Home Page</h2>"

@obj.route("/contactus")
def f3():
	return "<h3>Contact Info</h3>"

@obj.route("/course/<var>")
def f4(var):
	if var == 'aboutus':
		return redirect(url_for('f1'))
	if var == 'home':
		return redirect(url_for('f2'))
	if var == 'contactus':
		return redirect(url_for('f3'))

if __name__ == '__main__':
	obj.run()

