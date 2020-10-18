# from module import member
#

from flask import Flask     


obj=Flask(__name__)

#Flaskobject.add_url_rule(<urlrule>,<endpoint>,<viewblock>)

def aboutUs():
	s="<h2><font color=green>about flask tutorial</font></h2>"
	return s

obj.add_url_rule("/about","about",aboutUs)



if __name__ == '__main__':  
	obj.run()           

