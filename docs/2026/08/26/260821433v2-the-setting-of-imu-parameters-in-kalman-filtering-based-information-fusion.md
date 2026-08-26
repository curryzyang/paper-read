# The Setting of IMU Parameters in Kalman Filtering-based Information Fusion

- 区域：速读区
- 排名：11
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Qiang Hu, Yanhua Zou, Shuaiyi Huo, Haibo Ge, Wei Ouyang
- 机构：Tongji University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.21433v2) · [PDF](https://arxiv.org/pdf/2608.21433v2)

## TLDR
The paper proposes a systematic method for setting IMU noise and bias-instability parameters in Kalman filtering-based sensor fusion by leveraging the relationship between power spectral density and Allan variance calibration, and demonstrates its feasibility across INS/GNSS integration, LiDAR-inertial odometry, and visual-inertial odometry.

## Abstract
The setting or tuning of specifications for the inertial measurement unit (IMU) is tricky in sensor fusion. The underneath conundrum is caused by the fact that the working condition of IMU is more complex than the stationary calibration scenario. Since the noises and biases instabilities calibrated under static condition cannot accommodate other cases, the effective tuning of IMU parameters largely hinges on the experience or profound understanding of the system. In the current work, the setting method of IMU parameters based on Allan variance calibration is delved into within the Kalman filtering framework. Specifically, the relationship between the power sepctral density and Allan variance is leveraged in formulating the process uncertainty in continuous-time filtering. Three typical IMU-based sensor fusion systems, including INS/GNSS integration, LiDAR-inertial odometry, and visual-inertial odometry are considered to show the feasibility and effectiveness of this parameter setting process.
