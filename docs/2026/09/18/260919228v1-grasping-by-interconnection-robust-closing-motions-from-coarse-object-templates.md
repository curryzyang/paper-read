# Grasping by interconnection: robust closing motions from coarse object templates

- 区域：精读区
- 排名：9
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Julien Vanderheyden, Guillaume Drion, Fulvio Forni, Pierre Sacré
- 机构：University of Cambridge, University of Liège
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.19228v1) · [PDF](https://arxiv.org/pdf/2609.19228v1)

## TLDR
A motion planner that couples a dexterous hand to a coarse object template through compliant virtual springs and dampers generates robust closing grasps without feedback, tolerating about 1 cm size errors and several centimeters/tens of degrees pose errors, grasping 82.5% of everyday objects, and outperforming a state-of-the-art data-driven planner in 25 of 27 tested conditions.

## Abstract
Dexterous robot hands must often grasp objects whose shape, size, and pose are known only approximately. Grasp planners typically require accurate object models or correct errors with feedback, but how much inaccuracy a closing motion can tolerate on its own remains unclear. To address this question, we designed a motion planner based on four principles: a coarse template of the object, human grasp types, an object-centric interaction, and compliant, sliding contacts instead of prescribed contact points. This paper presents the planner, implemented through virtual model control, and its evaluation on a Shadow Dexterous Hand. Without feedback, the planned closing motions tolerated size errors of about 1cm and pose errors of several centimeters and tens of degrees, a wider range than a state-of-the-art data-driven planner in 25 of 27 tested conditions. They also grasped 82.5% of 80 everyday objects and succeeded within an autonomous pipeline. Robustness can thus be designed into the closing motion itself, rather than left only to feedback. This planner opens a path toward reliable manipulation in uncertain settings, which we will pursue by combining it with adaptive feedback control on the physical hand.


## 精读解读（中文）
### 一、研究动机
灵巧手抓取时物体的形状、尺寸和位姿往往只能近似已知（位姿估计误差可达数厘米与数十度，与手指间距相当），而传统解析法或数据驱动规划器依赖精确物体模型，或依靠触觉/力反馈在线纠错，导致无法判断成功究竟来自规划还是反馈。作者因此提出一个根本性问题：在不使用任何反馈的情况下，一条闭合运动本身能容忍多大的物体描述误差。

### 二、技术方案（Method）
规划器输入为粗模板（圆柱、球、扁盒）及其位姿与尺寸参数（至多8个参数，其中至多2个影响闭合运动），并将模板与人体抓取分类学中的medium wrap、power sphere、lateral pinch三种抓取型配对。方法用虚拟模型控制（VMC）实现：构建与真实Shadow手同构的虚拟手（连杆、关节、质量、惯量），用ReLU形弹簧与阻尼构造具有柔性表面的虚拟物体（阻尼系数含γ=1.05的5%膨胀，使阻尼先于弹簧力激活），再通过带滑动端点的虚拟界面（收缩/排斥弹簧-阻尼器，端点经棱柱与旋转关节在模板表面滑移，刚度分布由α、β设定）把虚拟手与虚拟物体耦合；由 u=ΣJ^T F 将虚拟力映射为关节力矩，积分耦合动力学 M(x)ẍ+C(x,ẋ)ẋ+g(x)=ΣJ^T F（x=(q,q_v)）仿真得到关节轨迹q(t)，物理手将其作为位置参考跟踪，仿真先于执行完成，闭合期间不使用任何真实物体测量。

### 三、结果（Result）
在Shadow灵巧手上无反馈执行规划闭合运动时，可容忍约1 cm的尺寸误差以及数厘米、数十度的位姿误差；在27个测试条件中的25个里，容差范围优于当前最先进的数据驱动规划器D(R,O) Grasp。该规划器还成功抓取了80件日常物体中的82.5%，并在一条自主流水线中完成任务，同时在不同刚度和阻尼参数下表现稳定。

### 四、结论（Conclusion）
鲁棒性可以被设计进闭合运动本身，而不必完全交给反馈控制；以粗模板为核心的object-centric顺应性互联为不确定环境下的可靠操作提供了一条路径。作者将其定位为闭环“interconnection抓取”的第一步，后续将结合物理手上的自适应反馈控制。

### 五、方法论与关键技术细节
关键点包括：接触点不预先指定，接触位置是仿真的产物；虚拟弹簧为ReLU形（仅压缩时产生排斥力）且力曲线连续，避免运动突变；模板尺寸只改变排斥弹簧静息长度与滑动端点布置，刚度与阻尼参数不随尺寸变化；VMC的被动性保证与被动物体交互稳定、无需精确接触模型，且无需逆运动学、计算负担低；虚拟界面模块化，可按模板与抓取型重构。局限性在于范围刻意狭窄：只规划从给定pre-grasp位姿开始的闭合运动，不涉及reaching、杂乱环境与模板选择；规划器不估计也不适应描述误差，读取一个模板只生成一条固定闭合运动。
