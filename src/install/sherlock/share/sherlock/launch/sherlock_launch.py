from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='sherlock',
            executable='sherlock_node_1.py',
            name='sherlock_node_1'
        ),
        Node(
            package='sherlock',
            executable='sherlock_node_2.py',
            name='sherlock_node_2'
        ),
        Node(
            package='sherlock',
            executable='sherlock_node_3.py',
            name='sherlock_node_3'
        ),
    ])
