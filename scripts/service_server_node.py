#service_server_node.py
#Returns multiplierResponse service that multiplies two input numbers
#no output will be shown unless you start the service_client_node
#OR unless you call the service directly using "rosservice call /multiplier" and
#double tab to fill in the fields
#credit to Emil Vidmark on YouTube for code

import rospy
from vidmarktutorial.srv import multiplier, multiplierResponse


def callback(request):    #holds a and b
    return multiplierResponse(request.a * request.b)

def multiply():
    rospy.init_node("multiplier_service")
    service = rospy.Service("multiplier", multiplier, callback)  #service name, type of service, callback function
    rospy.spin() #node keeps running until we stop it

if __name__ == '__main__':
    multiply()
