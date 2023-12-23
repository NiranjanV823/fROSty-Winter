from launch import LaunchDescription
from launch_ros.actions import Node
import os
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
	
	pkg_project = get_package_share_directory('mrs_hudson')
	pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')
	sdf_file = os.path.join(pkg_project, 'models', 'mrs_hudson.urdf')
	with open(sdf_file, 'r') as infp:
 		robot_desc = infp.read()
 	
	robot_state_publisher = Node(
  	 package='robot_state_publisher',
   	 executable='robot_state_publisher',
   	 name='robot_state_publisher',
   	 output='both',
   	 parameters=[
   	     {'use_sim_time': True},
   	     {'robot_description': robot_desc},
   	 ]
	)
	
	gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_project, 'launch', 'mrs_hudson_empty_world.launch.py'))
    	)
	rviz = Node(
	package='rviz2',
	executable='rviz2',
	arguments=['-d', os.path.join(pkg_project, 'config', 'mrs_hudson.rviz')],
	)

	return LaunchDescription([
		robot_state_publisher,
		rviz,
		gz_sim
		])
