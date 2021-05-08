#!/usr/bin/python
# coding: utf-8
 
import rospy #导入ROS Python客户端
from std_msgs.msg import String
 
# 定义Subscriber回调函数，处理收到的信息
def stringSubscriberCallback(data): #data的数据类型与Subscriber接收的Topic对应的消息类型一致
    rospy.loginfo('I heard: %s', data.data)
 
def stringSubscriber():
    rospy.init_node('sub_node', anonymous = False) #初始化ROS节点
    rospy.Subscriber('mytopic', String, stringSubscriberCallback) #定义Subscriber对象
 
    rospy.spin()
 
if __name__ == '__main__':
    stringSubscriber()

