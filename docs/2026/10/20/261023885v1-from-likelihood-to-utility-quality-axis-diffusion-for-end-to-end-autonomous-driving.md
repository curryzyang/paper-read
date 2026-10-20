# From Likelihood to Utility: Quality-Axis Diffusion for End-to-End Autonomous Driving

- 区域：精读区
- 排名：5
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Junjie Yang, Ziyi Shi, Shuqi Shen, Xinhu Zheng, Hongliang Lu, Hai Yang
- 机构：The Hong Kong University of Science and Technology (Guangzhou), The Chinese University of Hong Kong, Shenzhen, The Hong Kong University of Science and Technology, Southern University of Science and Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.23885v1) · [PDF](https://arxiv.org/pdf/2610.23885v1)

## TLDR
QualiDrive reframes diffusion for end-to-end autonomous driving along a driving-quality axis—using scene-specific quality ladders and quality-conditioned low-to-high refinement—rather than Gaussian noise, yielding state-of-the-art NAVSIM performance by directly generating higher-utility trajectories.

## Abstract
Diffusion models have become a dominant paradigm for end-to-end autonomous driving, yet existing planners organize trajectory generation along the Gaussian-noise axis, treating driving utility only as an auxiliary guidance or selection signal. We instead formulate diffusion along a driving-quality axis. We propose QualiDrive, which constructs scene-specific quality ladders by ranking observed trajectories according to measured driving utility and learns to reverse this ordered degradation through ordered low-to-high-quality refinement. Each reverse step is conditioned on the scene, ego state, current trajectory, and target quality level, progressively refining trajectories toward higher driving quality. On NAVSIM, QualiDrive achieves 94.5 PDMS on v1 and a state-of-the-art 92.74 EPDMS on v2. QualiDrive improves Oracle EPDMS only modestly over endpoint-only quality supervision (98.52 to 98.57), but substantially increases the fractions of candidates above 0.95 and 0.98 EPDMS from 12.94%/9.71% to 21.53%/15.93%, raising selected EPDMS from 92.63 to 92.74. These results suggest that diffusion is not merely a process of denoising, but one of progressive quality-ordered refinement.


## 精读解读（中文）
### 一、研究动机
现有端到端扩散规划器沿高斯噪声轴组织轨迹生成，把驾驶效用仅作为辅助引导或候选选择信号，导致生成过程追求人类示范分布下的高似然，而非安全、进度、舒适等多目标下的高驾驶效用。论文提出将扩散坐标从噪声水平改为驾驶质量，以直接对齐规划目标。

### 二、技术方案（Method）
QualiDrive先用大规模场景-轨迹评分库对同一意图下的观测轨迹按驾驶效用排序，构建场景特定的六级质量阶梯，并学习从低质量到高质量的有序反向细化。每个反向步骤以场景图像、自车状态、当前轨迹以及当前和目标质量等级为条件，通过DINOv2场景编码器与轨迹编码器交叉注意力融合，残差式预测下一级更高质轨迹；前向过程为高质量到低质量的有序退化并叠加小幅高斯扰动，反向过程执行五次确定性质量跃迁。训练损失包含逐级轨迹回归与平滑、质量分数回归、单调改进排序损失和终点回归；推理时生成512个候选，再由预测九项场景条件子分数的多目标评分器排序选最优轨迹。

### 三、结果（Result）
在NAVSIM上，QualiDrive在v1取得94.5 PDMS，在v2取得92.74 EPDMS，较此前最佳提升2.34分。相较仅端点质量监督，Oracle EPDMS仅从98.52小幅升至98.57，但EPDMS高于0.95和0.98的候选比例从12.94%/9.71%提升至21.53%/15.93%，使选中EPDMS从92.63升至92.74。

### 四、结论（Conclusion）
结果表明扩散规划不必只是去噪或恢复示范轨迹，而可以沿可测驾驶质量轴进行渐进式质量有序细化，从提升似然转向提升效用。该质量轴扩散框架在提升候选池高质量密度与最终选择性能上均有效，并在NAVSIM v1/v2达到领先结果。

### 五、方法论与关键技术细节
关键实现包括262144条有效轨迹在103288个训练场景上的评分库，约270亿场景-轨迹标签；质量阶梯按意图和路径原型分组，六级节点均为真实观测轨迹而非插值，目标质量按线性间隔选取并允许非回退，共享质量调度为q=(0,0.28,0.50,0.67,0.88,1)，相对进度计算使用epsilon=1e-4。生成器采用逐级轨迹回归、平滑、质量回归、相邻级单调排序铰链损失和终点回归，评分器用掩码二元交叉熵训练九个子分数并按NC、DAC、DDC、TL及TTC、EP、LK、HC、EC加权组合。推理时仅在初始低质量状态注入随机性，级间不再加噪，评分器独立于生成器且不访问评测器输出；评分库与阶梯仅用于训练，方法仍受有限轨迹库和评测质量函数依赖约束。
