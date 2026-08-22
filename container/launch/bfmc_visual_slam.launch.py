"""Run NVIDIA Isaac ROS Visual SLAM against the OAK topics from Brain.

Brain owns the OAK device and publishes the two mono streams. This launch file
only creates the Isaac ROS component and remaps its inputs; it never starts a
camera driver.
"""

import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode


def generate_launch_description():
    visual_slam_node = ComposableNode(
        name='visual_slam_node',
        package='isaac_ros_visual_slam',
        plugin='nvidia::isaac_ros::visual_slam::VisualSlamNode',
        parameters=[{
            'num_cameras': 2,
            # Brain publishes raw mono8 frames, not rectified images.
            'rectified_images': False,
            # Stereo tracking works with the currently published Brain topics.
            # Change this to 1 and add the IMU remap below when /oak/imu/data
            # is available from the camera stack.
            'tracking_mode': 0,
            'enable_localization_n_mapping': True,
            'enable_ground_constraint_in_odometry': True,
            'enable_ground_constraint_in_slam': True,
            'base_frame': 'base_link',
            'map_frame': 'map',
            'odom_frame': 'odom',
            'camera_optical_frames': ['oak_left', 'oak_right'],
            # Localization owns map→odom→base_link TF. Isaac publishes the
            # odometry message but must not publish a competing TF tree.
            'publish_map_to_odom_tf': False,
            'publish_odom_to_base_tf': False,
            'enable_slam_visualization': False,
        }],
        remappings=[
            ('visual_slam/image_0', '/oak/left/image_raw'),
            ('visual_slam/camera_info_0', '/oak/left/camera_info'),
            ('visual_slam/image_1', '/oak/right/image_raw'),
            ('visual_slam/camera_info_1', '/oak/right/camera_info'),
            # Visual-inertial mode, when deliberately enabled in this file:
            # ('visual_slam/imu', '/oak/imu/data'),
        ],
    )

    container = ComposableNodeContainer(
        name='bfmc_visual_slam_container',
        namespace='',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[visual_slam_node],
        output='screen',
    )

    return launch.LaunchDescription([container])
