# Contact-Implicit Whole-Body Trajectory Optimization for Dynamic Humanoid Locomotion on Parameterizable Uneven Terrain

- 区域：速读区
- 排名：1
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Roberto Mauceri, Stefano Dafarra, Giulio Romualdi, Marco Gabiccini, Daniele Pucci
- 机构：University of Pisa, Istituto Italiano di Tecnologia, University of Manchester
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.05585v1) · [PDF](https://arxiv.org/pdf/2611.05585v1)

## TLDR
This paper presents a contact-implicit whole-body trajectory optimization planner that enables humanoid robots to generate dynamic, feasible locomotion over parameterizable uneven terrains by using a smooth terrain approximation and generalized contact constraints, validated in simulation and on the ErgoCub robot.

## Abstract
This letter presents a trajectory planner for humanoid robots to perform dynamic motions on complex, parameterizable terrains using a contact-implicit whole-body optimization framework. The planner generates feasible movements without predefined contact sequences, considering the robot's full dynamics and kinematics. To plan bipedal locomotion on steps, ramps, and other terrains, we propose a mathematical model to approximate ground geometry with a smooth surface. The rigid interaction between the robot and the ground is modeled via novel contact constraints, extending the domain of applicability from flat and horizontal surfaces to any arbitrary smooth surface. Effectiveness is demonstrated using nonlinear programming to plan motions on various terrain topologies. We also explore dynamic trajectory generation by embedding high-level requirements in the cost function and the initial guess. Preliminary feasibility tests were conducted over non-coplanar terrains, both in simulation and on the real robot ErgoCub.
