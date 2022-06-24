#!/usr/bin/env

#publisher_node.py
#publishes "Hello - <time in milliseconds>" to talking_topic topic at a rate of 1 hz.
#Run rostopic view talking_topic to view messages
#credit to Emil Vidmark on YouTube for code 

import rospy 
from std_msgs.msg import String
from vidmarktutorial.msg import Position   #import position message we created from msg folder

def talk_to_me():
    pub = rospy.Publisher('talking_topic', Position, queue_size=10)   #name of topic, message type, how many messages in queue until delete some)
    rospy.init_node('publisher_node', anonymous=True) #name of node, node gets a unique name if another node created
    rate = rospy.Rate(1) #rate in hz
    rospy.loginfo("Publisher Node Started, now publishing String messages")
    while not rospy.is_shutdown(): #while the node is running
        #populate data in message
        msg = Position()
        msg.message = "My Position is: "
        msg.x = 2.0
        msg.y = 1.5
        pub.publish(msg)
        rate.sleep()
    
if __name__ == '__main__':
    try:
        talk_to_me()
    except rospy.ROSInterruptException: #for if we cancel script with Ctrl-C
        pass
