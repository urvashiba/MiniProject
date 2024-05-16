# ROS 2 MiniProject

</br>

## About

This Repository contains information about how to run the differential drive robot.
For controlling the robot I'm using the ROS2(foxy) framework in particular ros2_control and Gazebo Fortress (former Ignition) simulation.

</br>

### Steps

#### Make workspace

```bash
mkdir -p ign_ws/src
cd ign_ws/src
sudo apt-get update
sudo apt-get install lsb-release wget gnupg
```
Then install Ignition Fortress:

```bash
sudo wget https://packages.osrfoundation.org/gazebo.gpg -O /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null
sudo apt-get update
sudo apt-get install ignition-fortress
```
Now build the package and source it.
Install ros2 ignition bridge using below command.

```bash
sudo apt-get install ros-foxy-ign-bridge
```
Go to src folder and clone this repository and do not forget to do colcon build.

* Now, To run `differential drive robot` 

```bash
ros2 launch publish drive.launch.py
```
### Run with teleoperation

* To run the robot using `teleop_twist_keyboard` go to the model folder and run below comand in terminal,

```bash
ign gazebo diff_drive.sdf
ros2 run ros_ign_bridge parameter_bridge /model/vehicle_blue/cmd_vel@geometry_msgs/msg/Twist]ignition.msgs.Twist
ros2 run teleop_twist_keyboard teleop_twist_keyboard cmd_vel:=/model/vehicle_blue/cmd_vel
```

