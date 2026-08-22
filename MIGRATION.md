# Migration Notes

## Moved from Localization

The Isaac-specific package moved from:

```text
Localization_UniPD-DriveOps/src/bfmc_isaac_visual_odom
```

to:

```text
Isaac_Visual_SLAM_UniPD-DriveOps/src/bfmc_isaac_visual_odom
```

Localization now treats `/visual_odom_planar` as an external ROS topic and no
longer builds or launches an Isaac-specific package.

## New runtime workflow

```bash
./Brain_UniPD-DriveOps/docker/run.sh --normal-start
./Isaac_Visual_SLAM_UniPD-DriveOps/container/run.sh
./Localization_UniPD-DriveOps/docker/run.sh --normal-start
```

The combined build entry point is:

```bash
./Containers_UniPD_DriveOps/build_all.sh
```

The local repository was initialized without a remote. Add the intended GitHub
remote before pushing.
