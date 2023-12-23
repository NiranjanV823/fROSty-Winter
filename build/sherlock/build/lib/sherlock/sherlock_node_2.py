#!/usr/bin/env python3

import rclpy
from std_msgs.msg import String

def main():
    rclpy.init()
    node = rclpy.create_node('sherlock_node_2')
    pub = node.create_publisher(String, 'listen_2', 10)
    msg = String()
    msg.data = 'I am a high-functioning sociopath.'

    while rclpy.ok():
        pub.publish(msg)
        rclpy.spin_once(node)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
