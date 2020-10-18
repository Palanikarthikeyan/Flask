from flask import *

obj=Flask(__name__)

@obj.route("/login",methods=["POST"])
def login():
	n=request.form['n1']
	p=request.form['p1']
	if n == 'root' and p == 'welcome':
		return "<h2>Welcome to flask page</h2>"
	else:
		return "<h2>Login crediential is failed</h2>"


if __name__ == '__main__':
	obj.run()