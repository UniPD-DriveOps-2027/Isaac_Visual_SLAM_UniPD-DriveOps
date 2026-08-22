# Container files

This folder builds and runs the Isaac ROS Visual SLAM image for the BFMC OAK
topics. Run the commands below from the `Isaac_Visual_SLAM_UniPD-DriveOps`
repository root:

```bash
./container/build.sh
./container/run.sh
```

The OAK-D camera remains owned by Brain. This container only uses NVIDIA GPU
acceleration and subscribes to the shared ROS 2 graph. The image also builds
the `bfmc_isaac_visual_odom` adapter in the repository's `src/` directory.
