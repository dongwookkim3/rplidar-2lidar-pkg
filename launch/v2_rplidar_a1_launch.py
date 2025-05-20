#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([

        # 첫 번째 RPLIDAR 노드 (/scan1)
        Node(
            package='rplidar_ros',
            executable='rplidar_node',
            name='rplidar_node_1',
            namespace='rplidar1',
            parameters=[{
                'channel_type': 'serial',
                'serial_port': '/dev/ttyUSB0',
                'serial_baudrate': 115200,
                'frame_id': 'laser1',
                'inverted': False,
                'angle_compensate': True,
                'scan_mode': 'Sensitivity',
            }],
            remappings=[('/scan', '/scan1')],
            output='screen',
        ),

        # 두 번째 RPLIDAR 노드 (/scan2)
        Node(
            package='rplidar_ros',
            executable='rplidar_node',
            name='rplidar_node_2',
            namespace='rplidar2',
            parameters=[{
                'channel_type': 'serial',
                'serial_port': '/dev/ttyUSB1',
                'serial_baudrate': 115200,
                'frame_id': 'laser2',
                'inverted': False,
                'angle_compensate': True,
                'scan_mode': 'Sensitivity',
            }],
            remappings=[('/scan', '/scan2')],
            output='screen',
        ),
    ])
