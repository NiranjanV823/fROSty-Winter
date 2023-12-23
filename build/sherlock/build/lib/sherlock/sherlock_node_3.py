#!/usr/bin/env python3

import rclpy
from std_msgs.msg import String

def callback(msg):
    print(msg.data)

def main():
    rclpy.init()
    node = rclpy.create_node('sherlock_node_3')
    sub_1 = node.create_subscription(String, 'listen_1', callback, 10)
    sub_2 = node.create_subscription(String, 'listen_2', callback, 10)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
