#!/usr/bin/env bash
set -euo pipefail

source "/opt/ros/${ROS_DISTRO:-jazzy}/setup.bash"
source /opt/bfmc_isaac_ws/install/setup.bash

exec "$@"
