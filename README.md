#Kim Kardashian Robot arm(3 axis Cartesina Robot)

**URDF Architecture**: Design a basic kinematic chain from 'base_link' to 'finger'.

**Kinematic**:
    **X-axis**: Sliding module on a 2.0m rail(change and measure the real one later)
    **Z-Axis**: Vertical arm
    **Y-axis**: extenable gripper

##Requirements
```bash
sudo apt update && sudo apt install -y \ ros-jazzy-joint-state-publisher-gui \
ros-jazzy-xacro \
ros-jazzy-robot-state-publicher \
ros-jazzy-rvis2

