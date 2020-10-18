# from module import member
#

from flask import Flask     ### STEP 1
#### ----- ###### ------
#kw  module kw    classname 

# kw - keyword 

obj=Flask(__name__)  # creating the Flask class object ### STEP 2
#    #####  current module  
#
# user defined object

@obj.route("/") # decorator # route() ## STEP 3
def display():
	s="<h2><font color=green>Welcome to flask programming</font></h2>" # STEP 4
	return s

if __name__ == '__main__': ## STEP 5
	obj.run()          ## STEP 6

