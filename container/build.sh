#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
IMAGE="${ISAAC_VISUAL_SLAM_IMAGE:-unipd-driveops/isaac-visual-slam:jazzy}"
BASE_IMAGE="${ISAAC_ROS_BASE_IMAGE:-isaac_ros_dev-aarch64:latest}"
ROS_DISTRO_VALUE="${ISAAC_ROS_DISTRO:-jazzy}"

if ! docker image inspect "${BASE_IMAGE}" >/dev/null 2>&1; then
  echo "ERROR: NVIDIA Isaac ROS base image is missing: ${BASE_IMAGE}" >&2
  echo "Install the official Isaac ROS development image first, or set" >&2
  echo "ISAAC_ROS_BASE_IMAGE to the local image name." >&2
  exit 1
fi

echo "Building Isaac Visual SLAM image: ${IMAGE}"
echo "Base image: ${BASE_IMAGE}"
docker build \
  --build-arg "BASE_IMAGE=${BASE_IMAGE}" \
  --build-arg "ROS_DISTRO=${ROS_DISTRO_VALUE}" \
  --file "${SCRIPT_DIR}/Dockerfile" \
  --tag "${IMAGE}" \
  "${REPO_DIR}"

echo "Isaac Visual SLAM image ready: ${IMAGE}"
