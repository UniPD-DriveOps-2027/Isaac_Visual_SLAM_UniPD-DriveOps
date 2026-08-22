# Isaac Visual SLAM container

## First build

From inside this repository:

```bash
./container/build.sh
```

The NVIDIA Isaac ROS base image must already be available locally. Override it
with `ISAAC_ROS_BASE_IMAGE` and `ISAAC_ROS_DISTRO` when necessary.

## Daily run

```bash
./container/run.sh
```

Start Brain before this container. No OAK USB device is passed here; Brain
owns the camera and publishes the ROS topics over host networking.

## Validation

```bash
ros2 topic echo /visual_slam/tracking/odometry
ros2 topic echo /visual_odom_planar
```

Stop the attached container with `Ctrl-C`.
