#!/usr/bin/env

#subscriber_node.py
#prints messages from talking topic (which publisher_node publishes to)
#credit to Emil Vidmark on YouTube for code

import rospy
from std_msgs.msg import String
from vidmarktutorial.msg import Position   #import position message we created from msg folder

def callback(data): #data is a string object with a string object inside it with the data
    rospy.loginfo("%s X: %f Y: %f", data.message, data.x, data.y)


def listener():
    rospy.init_node("Subscriber_Node", anonymous = True) #node name, anonymous tells ROS to have unique names on all nodes
    rospy.Subscriber("talking_topic", Position, callback)  #topic subscribe to, message type, callback is function called whenever you receive a message on the topic
    rospy.spin()                                         #runs node continuously until shut down


if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass

