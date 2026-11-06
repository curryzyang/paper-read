# Distributed Geometric Optimization and Control of Rigid Differential-Drive Formations from Relative-Position Measurements

- 区域：精读区
- 排名：1
- 匹配度：5.6/10
- 来源：arxiv
- 作者：Thanacha Choopojcharoen, Erman Selim, Ramisha Anjum, Baris Fidan
- 机构：Ege University, University of Waterloo
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.07163v1) · [PDF](https://arxiv.org/pdf/2611.07163v1)

## TLDR
This paper develops a distributed optimization-based estimation–control scheme that reconstructs formation centroid, anchor vector, and centered coordinates from relative-position measurements and then regulates the shape, centroid, and orientation of differential-drive robot formations with only one absolute-position anchor, validated in ROS 2/Gazebo and with five physical robots.

## Abstract
Distance based formation control fixes the shape of a robot team but leaves its position and orientation unconstrained. We regulate all three for differential drive robots that have only one absolute position anchor, absolute headings, body frame relative position measurements, and communication with their neighbors. We derive a two layer estimation control scheme directly from optimization. The first half of the result is a set of graph-proximal estimators that reconstruct the centroid, the anchor vector, and the centered coordinates. Exact proximal updates reach consensus in finitely many steps, and a finite number of primal dual iterations leaves a bounded reconstruction error. The controller combines proximal centroid and orientation steps with distance gradient shape regulation, and a finite rotation removes the orientation drift caused by the shape step. A discrete Lyapunov analysis gives local exponential convergence once the estimators have converged. We validate the method in ROS 2 Gazebo and in experiments with five physical robots.


## 精读解读（中文）
### 一、研究动机
基于距离的编队控制只能固定机器人团队的形状，无法约束其平面位置与朝向；当多数机器人缺乏全局定位时，需要仅依赖单个绝对位置锚点、绝对航向、机体坐标系相对位置测量和邻居通信，同时调节差速驱动机器人编队的形状、质心与朝向这三个刚体自由度。

### 二、技术方案（Method）
论文针对N≥3台差速驱动机器人引入前视受控点z_i=p_i+ℓq_i，将非完整约束下的控制问题转化为采样受控点增量模型；每个采样周期运行两层算法。重建层用图近端估计器分别重构质心、锚点向量和中心化坐标，先按自身已施加运动预测，再通过邻居间近端/原始-对偶迭代在不改变平均值的约束下达成一致；控制层将近端质心与朝向更新同距离梯度形状调节结合，并用有限旋转消除形状步引入的朝向漂移。底层通过零阶保持下受控点增量的逐机器人逆映射实现差速驱动执行，估计收敛后由离散Lyapunov分析保证局部指数收敛。

### 三、结果（Result）
精确近端更新可在有限步内达到一致，有限轮原始-对偶迭代使重建误差有显式上界；在估计器收敛后，闭环对形状、质心跟踪和锚点向量定义的编队朝向具有局部指数收敛性。ROS 2/Gazebo仿真与五台实体机器人实验验证了方法，最终参考周期内质心误差低于1.1 cm、朝向误差低于0.019 rad。

### 四、结论（Conclusion）
该工作表明，可以从优化结构直接推导出分布式采样估计—控制架构，在仅有一个绝对位置锚点和局部相对位置测量的条件下同时锁定差速驱动刚体编队的形状、平移与旋转自由度。仿真和硬件实验支持该方案在稀疏通信与局部计算约束下的可实现性和精度。

### 五、方法论与关键技术细节
关键假设是通信图连通、距离约束图在期望平面构型附近无穷小刚性，且仅锚点N已知自身绝对受控点位置，锚点主要进入初始化；绝对航向用于把机体相对测量转到共同惯性方向。优化核心是带L-二次项与关联矩阵ℓ2,1精确惩罚的近端目标，需满足μ=β√λ2(L)−Δ>0以保证零分歧唯一最优，并用原始-对偶有限轮迭代近似求解。实现上估计仅需邻居消息，控制增量经零阶保持映射在(0,0)附近雅可比T_s diag(1,ℓ)非奇异而可局部精确实现；局限包括收敛性为估计器收敛后的局部结果、有限轮原始-对偶带来有界重建误差、精确执行依赖足够小增量，以及需要绝对航向、单锚点和刚性连通图等条件。
