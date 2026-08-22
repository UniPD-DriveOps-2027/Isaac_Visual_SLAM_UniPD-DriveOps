from setuptools import setup


package_name = 'bfmc_isaac_visual_slam'

setup(
    name=package_name,
    version='0.1.0',
    packages=[],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', [
            'launch/bfmc_visual_slam.launch.py',
        ]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='UniPD DriveOps',
    maintainer_email='driveops@unipd.it',
    description='BFMC camera-topic wrapper for NVIDIA Isaac ROS Visual SLAM.',
    license='Apache-2.0',
)
