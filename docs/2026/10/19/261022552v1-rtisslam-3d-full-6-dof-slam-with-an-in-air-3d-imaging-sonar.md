# RTISSLAM-3D: Full 6-DoF SLAM With an In-Air 3D Imaging Sonar

- 区域：速读区
- 排名：12
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Jan Steckel, Vincent Katter, Wouter Jansen
- 机构：University of Antwerp, Flanders Make Strategic Research Centre
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.22552v1) · [PDF](https://arxiv.org/pdf/2610.22552v1)

## TLDR
RTISSLAM-3D is a full 6-DoF sonar SLAM system that uses an in-air 3D imaging sonar with IMU and wheel encoders to perform acoustic odometry, place recognition, loop closure, and 3D occupancy mapping, achieving sub-meter trajectory and map accuracy on a 545 m forest drive.

## Abstract
Echolocating bats navigate dense forests using sonar alone, and in-air 3D imaging sonars now capture the entire frontal hemisphere with every pulse. Sonar SLAM, however, has so far been planar: current systems estimate a 2D trajectory and discard the elevation information in the sonar images, an assumption that does not hold on rough and sloped terrain such as a forest floor. In this paper, we introduce RTISSLAM-3D, a novel 6-DoF SLAM system for a wheeled robot that carries an in-air 3D imaging sonar, an IMU and wheel encoders. A CFAR detector on the sphere reduces every sonar image to a sparse set of 3D detections, which we use for a 3D acoustic odometry that models the shape of the sonar beam, for place recognition with polar submap descriptors, and for the verification of loop closures by 3D registration, all combined in a 6-DoF pose graph with attitude factors. We evaluated RTISSLAM-3D on a 545m drive through a forest, with a 3D lidar SLAM as reference. The loop closures reduced the horizontal error of the acoustic odometry from 1.74m to 0.28m, with a height error of 0.12m, and 94.6% of the resulting 3D sonar map lies within 0.3 m of the lidar map.
