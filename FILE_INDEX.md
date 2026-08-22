# Isaac_Visual_SLAM_UniPD-DriveOps File Index

| Path | Purpose |
|---|---|
| `README.md` | Repository overview and daily workflow |
| `ARCHITECTURE.md` | Ownership, data flow, TF, and tracking modes |
| `CONTAINER.md` | Container build/run instructions |
| `MIGRATION.md` | Migration from the Localization repository |
| `container/Dockerfile` | Isaac ROS image definition |
| `container/build.sh` | One-time image build |
| `container/run.sh` | Runtime GPU container launcher |
| `container/entrypoint.sh` | ROS workspace setup |
| `container/launch/bfmc_visual_slam.launch.py` | NVIDIA Visual SLAM wrapper and topic remaps |
| `container/package.xml` | Wrapper package manifest |
| `src/bfmc_isaac_visual_odom/` | Isaac odometry republisher ROS package |
| `.dockerignore` | Docker build-context exclusions |
| `.gitignore` | Git build-artifact exclusions |
