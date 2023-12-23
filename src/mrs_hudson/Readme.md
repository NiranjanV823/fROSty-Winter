# mrs_hudson

## Overview
This is a package for the mrs_hudson bot. This repository hosts the essential URDF and launch files for mrs_hudson bot, designed specifically for this fROSty winter.

## Installation
### Dependencies
Follow the instructions on the fROSty winter 2023 repository for the intital setup of with ros and gazebo.

Then for cloning the repo you need to have git installed on your system

```bash
apt-get install git
```

Then go to the ```erc_ws/src``` directory and open the terminal and run

```bash 
git clone https://github.com/erciitb/mrs_hudson.git
```

### Building
Now before building the package with ```colcon build``` first we need to change the path of meshes in the urdf and sdf files.

In the ```models``` and ```world``` folder open the urdf and sdf files and in mesh filename update the path of the meshes.

(PS: Use a simple find and replace, eg 

find = ```home/saurabh42/erc_ws/src/mrs_hudson/meshes```

replace = ```home/shiwani418/erc_ws/src/mrs_hudson/meshes```

Do a replace all in both the URDF and SDF file.
)


Then run ```colcon build``` in the workspace and follow the frosty content.