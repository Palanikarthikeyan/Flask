# from module import member
#

from flask import Flask     ### STEP 1

obj=Flask(__name__)  # creating the Flask class object ### STEP 2

@obj.route("/aboutus") # decorator # route() ## STEP 3
def fa():       # STEP 4
	s="""<html>
	<head>
	<title>Welcome</title>
	<body>
	<p>This is sample flask running page</p>
	<h1><font color=green>Test page1</h1></font>
	<h2><font color=red>Test Page2</h2></font>
	<h3><font color=blue>Test page3</h3></font>
	</body>
	</head>
	</html>"""
	return s


if __name__ == '__main__': ## STEP 5
	obj.run()          ## STEP 6

