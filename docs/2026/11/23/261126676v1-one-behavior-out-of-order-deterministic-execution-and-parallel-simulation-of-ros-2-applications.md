# One Behavior, Out of Order: Deterministic Execution and Parallel Simulation of ROS 2 Applications

- 区域：速读区
- 排名：5
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Chengzi Huang, Behnam Khodabandeloo, Duc Anh Nguyen, Chuanchao Gao, Wang Yi
- 机构：Uppsala University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.26676v1) · [PDF](https://arxiv.org/pdf/2611.26676v1)

## TLDR
The paper proposes a lightweight coordination scheme that makes ROS 2 applications deterministic by fixing when components read and write, and leverages these known dependencies for an out-of-order parallel simulator that preserves this single behavior while speeding up testing.

## Abstract
System-level simulation is widely used to validate robotic applications before hardware deployment. However, Robot Operating System 2 (ROS 2), a popular middleware for such applications, uses asynchronous publish-subscribe communication, which can make application behavior depend on scheduling and the platform. The behavior can then vary across runs and machines even with the same inputs. This nondeterminism makes faults hard to reproduce and tests unreliable. In this paper, we first give ROS 2 applications a lightweight coordination scheme in which every component, including event-driven ones, reads its inputs and writes its outputs at predefined time instants. By decoupling computation and communication, the scheme makes an application deterministic, that is, it always has one behavior for given inputs. Tests are thus repeatable, but for large applications they still take a long time. To speed up these tests, we then present an out-of-order parallel simulation algorithm. From the predefined read and write instants, it knows before the run which activations of components depend on which. It starts each activation as soon as those it depends on have finished. Finally, we implement the algorithm in a simulator that runs existing ROS 2 applications without any change to them or to ROS 2. We evaluate the simulator on industrial use cases and synthetic graphs. On the industrial use cases, it is up to 2.6 times faster than synchronous parallel simulation and needs an order of magnitude less memory for messages than asynchronous parallel simulation.
