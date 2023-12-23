import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'week1_tutorials'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'models'), glob(os.path.join('models', 'cub_world.sdf'))),
        (os.path.join('share', package_name, 'config'), glob(os.path.join('config', 'custom.rviz'))),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', 'cub.launch.py'))),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', 'custom_rviz.launch.py'))),
    ],
    install_requires=['setuptools',
                      'launch',
        'ament_index_python',
        'ros2pkg',],
    zip_safe=True,
    maintainer='niranjan',
    maintainer_email='niranjan@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
