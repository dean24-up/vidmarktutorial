#service_client_node.py
#Receives service from service_server_node
#Message should be result of multiplying 7 and 2
#credit to Emil Vidmark on YouTube for code

import rospy
from vidmarktutorial.srv import multiplier, multiplierResponse #I'm not sure what multiplierResponse for

def multiplier_client(x, y):
    rospy.init_node("client_node")
    rospy.wait_for_service("multiplier") #waits for multiplier to exist
    rate = rospy.Rate(1) #1 second
    while not rospy.is_shutdown(): #while ros is running
        try:
            multiply_two_ints = rospy.ServiceProxy("multiplier", multiplier) #service name, what type of service message
            response = multiply_two_ints(x, y)
            rospy.loginfo(response.result)
            rate.sleep()
        except rospy.ServiceException as e:
            print("Service call failed %s", e)


if __name__ == '__main__':
    multiplier_client(7,2)


