# Isaac_Visual_SLAM_UniPD-DriveOps

NVIDIA Isaac ROS Visual SLAM integration for UniPD DriveOps. This repository
contains the GPU container wrapper and the ROS odometry adapter used by the
Localization stack.

## Structure

```text
Isaac_Visual_SLAM_UniPD-DriveOps/
├── container/                    # Docker image and launch wrapper
│   ├── Dockerfile
│   ├── build.sh / run.sh
│   └── launch/bfmc_visual_slam.launch.py
└── src/bfmc_isaac_visual_odom/   # Isaac odometry → EKF topic adapter
```

## Architecture

The Brain container owns the OAK-D device and publishes the stereo topics.
This repository starts only NVIDIA Visual SLAM and the odometry adapter:

```text
Brain OAK stereo topics
        │
        ▼
NVIDIA Isaac ROS VisualSlamNode
        │ /visual_slam/tracking/odometry
        ▼
bfmc_isaac_visual_odom
        │ /visual_odom_planar
        ▼
Localization local EKF
```

The Isaac TF broadcasters are disabled because Localization owns the
`map → odom → base_link` TF chain.

## ROS topic contract

The wrapper remaps its stereo inputs to the OAK topics published by Brain:

```text
/oak/left/image_raw       → visual_slam/image_0
/oak/left/camera_info     → visual_slam/camera_info_0
/oak/right/image_raw      → visual_slam/image_1
/oak/right/camera_info    → visual_slam/camera_info_1
```

Isaac publishes `/visual_slam/tracking/odometry`. The adapter also publishes
`/visual_odom` and `/visual_odom_planar`, which Localization consumes.

No camera device is passed to this container and no camera launch is run here.

## Build once

The official NVIDIA Isaac ROS development image must already exist locally.
The default is `isaac_ros_dev-aarch64:latest`:

```bash
./container/build.sh
```

If the installed NVIDIA image has another name or ROS distribution:

```bash
ISAAC_ROS_BASE_IMAGE=<local-isaac-image> \
ISAAC_ROS_DISTRO=<jazzy-or-humble> \
./container/build.sh
```

The image installs `ros-${ROS_DISTRO}-isaac-ros-visual-slam` and builds the
launch-wrapper and odometry-republisher packages once. Normal runs do not
install packages.

## Run

```bash
./container/run.sh
```

Start Brain first so the stereo topics exist, then start this container, and
then start Localization.

The wrapper defaults to stereo tracking (`tracking_mode: 0`) because the
current Brain OAK node publishes left/right images but does not publish an
OAK IMU topic. To use visual-inertial tracking, edit
`container/launch/bfmc_visual_slam.launch.py`, set `tracking_mode` to `1`, and
enable the `/oak/imu/data` remap after that topic is provided.

## Repository history

The Isaac-specific odometry adapter was moved from
`Localization_UniPD-DriveOps/src/bfmc_isaac_visual_odom` into this repository.
See [MIGRATION.md](MIGRATION.md) for the ownership change.

## Documentation

- [ARCHITECTURE.md](ARCHITECTURE.md) — runtime and topic architecture
- [CONTAINER.md](CONTAINER.md) — build/run instructions
- [FILE_INDEX.md](FILE_INDEX.md) — repository file map
- [MIGRATION.md](MIGRATION.md) — move from the Localization repository
- [NVIDIA Isaac ROS Visual SLAM documentation](https://nvidia-isaac-ros.github.io/repositories_and_packages/isaac_ros_visual_slam/isaac_ros_visual_slam/index.html)
