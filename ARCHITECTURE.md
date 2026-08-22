# Isaac_Visual_SLAM_UniPD-DriveOps Architecture

## Ownership

| Component | Owner | Role |
|---|---|---|
| OAK-D hardware and camera launch | `Brain_UniPD-DriveOps` | Publishes stereo images and camera calibration |
| NVIDIA `VisualSlamNode` | `Isaac_Visual_SLAM_UniPD-DriveOps` container | GPU stereo visual odometry/SLAM |
| Isaac odometry adapter | `bfmc_isaac_visual_odom` | Normalizes Isaac odometry for the BFMC EKF |
| EKF and global localization | `Localization_UniPD-DriveOps` | Fuses wheel, car IMU, visual odometry, GPS, map matching, and signs |

## Data flow

```text
/oak/left/image_raw + /oak/left/camera_info
/oak/right/image_raw + /oak/right/camera_info
                         │
                         ▼
              VisualSlamNode (GPU)
                         │
              /visual_slam/tracking/odometry
                         │
                         ▼
            visual_odom_republisher
              │                  │
       /visual_odom       /visual_odom_planar
                                  │
                                  ▼
                       Localization local EKF
```

## TF policy

Isaac publishes odometry messages only. `publish_map_to_odom_tf` and
`publish_odom_to_base_tf` are disabled in the wrapper. The Localization EKFs
are the sole owners of `map → odom → base_link`.

## Tracking modes

The default is stereo tracking (`tracking_mode: 0`). Visual-inertial mode is
available by editing `container/launch/bfmc_visual_slam.launch.py` after a
valid `/oak/imu/data` topic is available.
