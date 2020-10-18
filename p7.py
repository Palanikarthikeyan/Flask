# from module import member
#

from flask import Flask     ### STEP 1

obj=Flask(__name__)  # creating the Flask class object ### STEP 2

@obj.route("/about/<int:var>") # decorator # route() ## STEP 3
def fa(var):       # STEP 4
	s="<h2><font color=green>port number is:%s"%(var)
	return s


if __name__ == '__main__': ## STEP 5
	obj.run()          ## STEP 6

