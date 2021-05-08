#!/usr/bin/python2
# coding: utf-8
     
import rospy #导入ROS Python客户端
from std_msgs.msg import String
from std_msgs.msg import Int16
def topicPublisher():
    rospy.init_node('pub_node', anonymous = False) #初始化ROS节点
    simple_publisher = rospy.Publisher('mytopic', String, queue_size = 10) #定义Publisher对象
    rate = rospy.Rate(10) #设置Topic发布的频率（Hz）
     
    mytopic_content = "Hello World!" #填充Topic内容
    while not rospy.is_shutdown():
        simple_publisher.publish(mytopic_content) #发布Topic
        rate.sleep() #确保Topic以我们设定的频率发布
     
if __name__ == '__main__':
    try:
        topicPublisher()
    except rospy.ROSInterruptException:
        pass
