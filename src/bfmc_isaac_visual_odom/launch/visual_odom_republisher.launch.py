from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    """Republish externally produced visual odometry; do not launch a camera."""
    return LaunchDescription([
        Node(
            package='bfmc_isaac_visual_odom',
            executable='visual_odom_republisher',
            name='visual_odom_republisher',
            output='screen',
            parameters=[{
                'input_topic': '/visual_slam/tracking/odometry',
                'output_topic': '/visual_odom',
                'planar_output_topic': '/visual_odom_planar',
                'publish_planar': True,
                'flatten_planar': True,
                'output_frame_id': 'odom',
                'output_child_frame_id': 'base_link',
                'position_variance_xy': 0.04,
                'position_variance_z': 999.0,
                'roll_pitch_variance': 999.0,
                'yaw_variance': 0.08,
                'linear_velocity_variance_xy': 0.10,
                'angular_velocity_variance_yaw': 0.10,
            }],
        ),
    ])
