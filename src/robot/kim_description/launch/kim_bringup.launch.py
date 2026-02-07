import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import Command, LaunchConfiguration
from launch.conditions import IfCondition

def generate_launch_description():
    pkg_description = get_package_share_directory('kim_description')
    pkg_ired = get_package_share_directory('ired_bringup')
    
    urdf_file = os.path.join(pkg_description, 'urdf', 'kim_kardashian.urdf.xacro')

    hardware_arg = DeclareLaunchArgument(
        'hardware',
        default_value='false',
        description='Set to "true" to enable Lidar and real robot hardware'
    )

    return LaunchDescription([
        hardware_arg,

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{
                'robot_description': Command(['xacro ', urdf_file])
            }]
        ),
        
        
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_ired, 'launch', 'ired_bringup.launch.py')
            ),
            condition=IfCondition(LaunchConfiguration('hardware'))
        ),

        Node(
            package='rviz2', 
            executable='rviz2', 
            name='rviz2'
        )
    ])