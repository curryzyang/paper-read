# Image-Based Path-Planning for Navigation of Soft-Growing Robots in the Spinal Sub-Arachnoid Space

- 区域：精读区
- 排名：7
- 匹配度：4.2/10
- 来源：arxiv
- 作者：George Dimas, Panagiotis G. Kalozoumis, Panagiotis Vartholomeos, Dimitris K. Iakovidis
- 机构：University of Thessaly
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.12631v1) · [PDF](https://arxiv.org/pdf/2610.12631v1)

## TLDR
This paper proposes an image-based 3D path-planning algorithm that extends A* to guide a soft-growing robot through the spinal sub-arachnoid space by generating safe, efficient paths while ensuring anchor points for reliable steering, evaluated on a detailed SSS model.

## Abstract
Recently, soft robotic procedures are being developed aiming at achieving targeted minimally invasive operations or drug administration in specific locations in the human body. Accordingly, specialized path-planning algorithms need to be investigated for the estimation of efficient paths that would protect the delicate tissue structures and simultaneously satisfy a set of requirements for the efficient navigation of the robot. In this context, we propose an image-based 3D pathplanning algorithm, which is an extension of the A* algorithm, for the navigation of a soft-growing robot inside the spinal subarachnoid space (SSS). The proposed algorithm is capable of estimating a safe pathway towards the goal location, while ensuring the establishment of anchor points that facilitate the efficient steering of the soft robot. The algorithm is evaluated using a highly detailed model of the SSS with respect to its capacity to satisfy the robot movement requirements and path efficiency.


## 精读解读（中文）
### 一、研究动机
针对软体生长机器人在脊髓蛛网膜下腔（SSS）内导航时需同时保护脆弱神经和血管结构并满足运动需求的问题，传统避障路径规划无法保证软体生长元件（GE）与周围结构形成锚定点以维持导管转向精度。因此需要一种基于影像的三维路径规划方法，在复杂SSS中估计安全且可锚定的路径，服务于微创靶向给药等任务。

### 二、技术方案（Method）
方法将MRI分割得到的SSS体数据表示为二值图像栈S∈{0,1}^{H×W×N}，其中0为自由空间、1为障碍或候选锚定结构；将机器人尖端建模为半径0.5 mm的导管圆盘和半径1 mm的GE圆环。在A*的f(n)=g(n)+h(n)基础上引入两个附加代价：c_a(n)奖励可形成锚定点的节点，c_b(n)惩罚远离障碍物的节点，c_a由自适应参数k(n)和陡峭度z=5控制。GE可通过性由交叉面积比不超过v=80%判定，锚定点定义为GE外圆在左右或上下相反弧段同时接触障碍；随后沿路径用相邻节点夹角估计作动节点（非零转角），并以锚定点百分比、平均距离和作动节点百分比评价路径。

### 三、结果（Result）
在由详细SSS数字模型生成的413层、223×128、0.547×0.547 mm²面内分辨率和1 mm层厚的分割图像栈上进行200次随机起止点实验。与原始A*、A*+c_a、A*+c_b相比，A*+c_a与A*+c_a+c_b获得最高锚定点百分比（APAP约19.41%和19.11%），但A*+c_a的平均作动节点百分比（APAN 32.87%）低于A*+c_a+c_b（38.83%），平均距离（ADT 1.10 mm）也更短；原始A*的ADT和APAN最低（1.09 mm、29.26%）但APAP仅14.37%。定性导入Siemens NX生成直径2 mm的GE管后，路径可避开神经根并沿SSS壁形成锚定，而传统A*在部分位置无法保证锚定。

### 四、结论（Conclusion）
研究表明，基于影像的三维扩展A*可在复杂SSS中规划出兼顾导管避障与GE锚定的路径，满足软体生长机器人“跟随领导者”导航对转向稳定性的关键要求。结果也显示锚定率、路径长度与作动复杂度之间存在权衡，单纯追求锚定或避障均不充分；路径中较突然的转向可通过后处理平滑而不破坏锚定点。总体而言，该方法为SSS内软体机器人导航提供了可行方案，但仍需真实MRI与更完整机器人动力学验证。

### 五、方法论与关键技术细节
关键实现细节包括：输入为SSS高精细数字模型经3D Slicer转换的分割图像栈，原始574层中保留413层；起止点随机取自首末层且属于导管与GE自由空间；导管半径0.5 mm、GE半径1 mm、GE安全通过率v=80%、k(n)陡峭度z=5；锚定由四个外圆弧的左右或上下接触同时判定，作动节点由相邻三点夹角a_act非零判定。方法假设仅机器人尖端部署于SSS且遵循“follow-the-leader”，未建模其余机器人本体、流体或压力动力学，也未在真实MRI上验证；此外锚定点增加可能提高路径复杂度和作动次数，需要多指标平衡。
