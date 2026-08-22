#!/usr/bin/env bash
set -euo pipefail

IMAGE="${ISAAC_VISUAL_SLAM_IMAGE:-unipd-driveops/isaac-visual-slam:jazzy}"
CONTAINER="${ISAAC_VISUAL_SLAM_CONTAINER:-unipd-isaac-visual-slam}"

if ! docker image inspect "${IMAGE}" >/dev/null 2>&1; then
  echo "ERROR: Isaac Visual SLAM image is missing: ${IMAGE}" >&2
  echo "Build it once with: ./Isaac_Visual_SLAM_UniPD-DriveOps/container/build.sh" >&2
  exit 1
fi

# No USB camera is passed to this container. Brain owns the OAK device and
# publishes the stereo topics over the host ROS 2 network.
exec docker run --rm -it \
  --name "${CONTAINER}" \
  --network host \
  --ipc host \
  --runtime nvidia \
  --env NVIDIA_VISIBLE_DEVICES=all \
  --env NVIDIA_DRIVER_CAPABILITIES=all \
  --env "ROS_DOMAIN_ID=${ROS_DOMAIN_ID:-0}" \
  --env "RMW_IMPLEMENTATION=${RMW_IMPLEMENTATION:-rmw_fastrtps_cpp}" \
  --volume /etc/localtime:/etc/localtime:ro \
  "${IMAGE}"
