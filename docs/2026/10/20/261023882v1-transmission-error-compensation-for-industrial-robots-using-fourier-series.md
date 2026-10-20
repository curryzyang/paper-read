# Transmission Error Compensation for Industrial Robots Using Fourier Series

- 区域：速读区
- 排名：8
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Christian J. E. Bauer, Simon Nowinski, Valentin Kamm, Lukas Steinle, Armin Lechler, Alexander Verl
- 机构：University of Stuttgart
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.23882v1) · [PDF](https://arxiv.org/pdf/2610.23882v1)

## TLDR
This paper identifies velocity-dependent industrial-robot transmission errors from laser tracker measurements, models them with a Fourier series for virtual commissioning and CNC setpoint feedforward compensation, and improves Stäubli TX2-40 accuracy by 83.26% on axis 2 and 49.21% on axis 3 with a 0.114 mrad mean absolute model error.

## Abstract
Due to their low accuracy, industrial robots commonly require online teaching after the offline development of a robot program in simulation. The accuracy is limited by compliance and transmission errors in the robot joints. Transmission errors are defined as errors between the load-side angles of the gearboxes and the motor encoder angles. An approach to identify the transmission errors based on laser tracker measurements is presented. The developed velocity-dependent Fourier series model is integrated in a virtual commissioning software as a co-simulated functional mock-up unit. Additionally, it is used to compensate the transmission errors by correcting the setpoint from the computerized numerical control (CNC). The model identification and the compensation are experimentally evaluated with a Stäubli TX2-40 industrial robot. The model has a mean absolute error of 0.114 mrad, and the compensation improves the accuracy by 83.26 % for axis 2 and 49.21 % for axis 3.
