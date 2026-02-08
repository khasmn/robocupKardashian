#Kim Kardashian Robot arm(3 axis Cartesina Robot)

**URDF Architecture**: Design a basic kinematic chain from 'base_link' to 'finger'.

**Kinematic**:
    **X-axis**: Sliding module on a 2.0m rail(change and measure the real one later)
    **Z-Axis**: Vertical arm
    **Y-axis**: extenable gripper

**run and see the modle**:
```bash
ros2 launch kim_description kim_bringup.launch.py
ros2 run joint_state_publisher_gui joint_state_publisher_gui

##Requirements
sudo apt update && sudo apt install -y \ ros-jazzy-joint-state-publisher-gui \
ros-jazzy-xacro \
ros-jazzy-robot-state-publicher \
ros-jazzy-rvis2

**run and see the modle**:
