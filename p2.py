# from module import member
#

from flask import Flask     ### STEP 1

obj=Flask(__name__)  # creating the Flask class object ### STEP 2

@obj.route("/") # decorator # route() ## STEP 3
def fa():       # STEP 4
	return "<h1>Welcome</h1>"


if __name__ == '__main__': ## STEP 5
	obj.run()          ## STEP 6

