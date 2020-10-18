# from module import member
#

from flask import Flask     ### STEP 1

obj=Flask(__name__)  # creating the Flask class object ### STEP 2

@obj.route("/contactus") # decorator # route() ## STEP 3
def fa():       # STEP 4
	s="""<html>
	<head>
	<title>Welcome</title>
	<body>
	<h1><b>OurContact details</h1></b>
	<h1><font color=green>Krosum Labs</h1></font>
	<h2><font color=green>1st main</h2></font>
	<h2><font color=green>Bangalore</h2></font>
	<h2><font color=red>PIN:560028</h2></font>
	</body>
	</head>
	</html>"""
	return s


if __name__ == '__main__': ## STEP 5
	obj.run()          ## STEP 6

