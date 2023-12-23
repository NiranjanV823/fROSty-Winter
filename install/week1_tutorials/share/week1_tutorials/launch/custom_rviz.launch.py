from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
import os.path

def generate_launch_description():
    pkg_project = get_package_share_directory('week1_tutorials')  # Replace 'your_package_name' with the actual name of your package
    return LaunchDescription([
        Node(
            package='rviz2',
            namespace='',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', os.path.join(pkg_project, 'config', 'custom.rviz')]
        )
    ])