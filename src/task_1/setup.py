from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'task_1'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
                (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', 'mrs_hudson_world.launch.py'))),
                        (os.path.join('share', package_name, 'config'), glob(os.path.join('config', 'mrs_hudson.rviz'))),
                                (os.path.join('share', package_name, 'worlds'), glob(os.path.join('worlds', 'mrs_hudson_arena.sdf'))),



    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='niranjan',
    maintainer_email='niranjan@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'node_96 ='+package_name+'.96:main',
        ],
    },
)
