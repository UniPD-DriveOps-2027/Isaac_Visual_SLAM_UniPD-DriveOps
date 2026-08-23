# NVIDIA Isaac ROS base image must be installed once on the Jetson first.
# Override BASE_IMAGE/ROS_DISTRO when the local Isaac ROS installation uses a
# different distro or architecture-specific image.

ARG BASE_IMAGE=isaac_ros_dev-aarch64:latest
FROM ${BASE_IMAGE}

ARG ROS_DISTRO=jazzy
ENV ROS_DISTRO=${ROS_DISTRO} \
    DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-colcon-common-extensions \
    ros-${ROS_DISTRO}-isaac-ros-visual-slam \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/bfmc_isaac_ws
COPY container/package.xml container/setup.py container/setup.cfg ./
COPY container/resource ./resource
COPY container/launch ./launch
COPY src ./src

RUN source /opt/ros/${ROS_DISTRO}/setup.bash \
    && colcon build --merge-install --cmake-args -DBUILD_TESTING=OFF

COPY container/entrypoint.sh /usr/local/bin/bfmc-isaac-entrypoint
RUN chmod +x /usr/local/bin/bfmc-isaac-entrypoint

ENTRYPOINT ["/usr/local/bin/bfmc-isaac-entrypoint"]
CMD ["ros2", "launch", "bfmc_isaac_visual_slam", "bfmc_visual_slam.launch.py"]
