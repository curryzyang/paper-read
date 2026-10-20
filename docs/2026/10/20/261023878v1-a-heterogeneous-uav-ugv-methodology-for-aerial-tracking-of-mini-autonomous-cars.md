# A Heterogeneous UAV UGV Methodology for Aerial Tracking of Mini Autonomous Cars

- 区域：精读区
- 排名：3
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Santiago Fernandez, Angel da Silva, Hiago Sodre, Pablo Moraes, Bruna Gutterres, Ricardo B. Grando
- 机构：Technological University of Uruguay
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.23878v1) · [PDF](https://arxiv.org/pdf/2610.23878v1)

## TLDR
This paper presents a ROS 2/Gazebo Sim heterogeneous UAV–UGV framework that fuses YOLO-based aerial detections with UGV state information to maintain continuous tracking of mini autonomous cars during visual gaps, achieving near-continuous coverage and substantially lower localization error than visual-only YOLO tracking.

## Abstract
Aerial tracking of autonomous ground vehicles can provide useful situational awareness in environments where fixed external perception infrastructure is unavailable. However, visual-only tracking from an unmanned aerial vehicle (UAV) is limited by camera field of view, viewpoint changes, occlusions, and temporary loss of target visibility. This paper presents a heterogeneous UAV--UGV methodology for aerial tracking of small-scale autonomous ground vehicles in simulation. The system is implemented in ROS~2 and Gazebo Sim using a Tello-like UAV equipped with a front-facing RGB camera and multiple LIMO-like unmanned ground vehicles (UGVs). Three approaches are evaluated: a training-free color-marker baseline, a YOLO-based visual baseline, and a proposed UAV--UGV fusion method. The proposed method uses the same visual detector as the YOLO baseline, but combines visual detections with UGV state information to maintain the target estimate during visual gaps. The methods are evaluated across four scenarios: single-car tracking, crossing trajectories, occlusion, and UAV-assisted awareness. Results over 600 simulation runs show that the proposed fusion method achieves nearly continuous track coverage across all scenarios while reducing localization error relative to the YOLO baseline. Compared with the visual-only YOLO approach, the fusion method reduces RMSE by 37.3\%, 64.2\%, 62.6\%, and 61.8\% in the four evaluated scenarios, respectively. The method also enables conflict-awareness lead times of 10.20~s in the crossing scenario and 9.07~s in the UAV-assisted awareness scenario. These results indicate that heterogeneous UAV--UGV fusion can improve aerial tracking continuity and robustness when visual observations are intermittent.


## 精读解读（中文）
### 一、研究动机
无人机对地面自主车辆的空中跟踪可在缺乏固定外部感知基础设施时提供态势感知，但纯视觉跟踪受相机视场、视角变化、遮挡和目标暂时不可见限制。异质UAV-UGV系统具有互补能力：UAV提供高位广域视角，UGV提供稳定地面状态信息，因此需要评估共享UGV状态信息能否在视觉中断时保持空中跟踪连续性。

### 二、技术方案（Method）
在ROS 2 Jazzy与Gazebo Sim中构建Tello类UAV（前视RGB相机）和LIMO类UGV的仿真系统，场景控制器生成四类运动轨迹，视觉检测器处理UAV图像，跟踪模块将检测转换为目标状态，评估器记录覆盖率和定位误差。对比三种方法：无训练颜色标记基线采用RGB阈值与连通域滤波；YOLOv8视觉基线用仿真图像训练，标签由RGB图像中可见标记生成，并以检测框和前视相机测距模型估计目标位置；提出的UAV-UGV融合法使用同一YOLOv8检测器，有检测时用视觉量测更新目标状态，无检测时用UGV共享的位置、姿态和速度信息进行状态预测以维持目标估计。每个场景采用5个随机种子、每种子10次试验，每种方法共200次运行、每场景50次。

### 三、结果（Result）
600次仿真中三种方法各完成200次有效运行，未出现假阳性、ID切换或YOLO检测器回退。融合法在所有场景取得最低RMSE和最高跟踪覆盖率，相较YOLO视觉基线在S1至S4的RMSE分别降低37.3%、64.2%、62.6%和61.8%，跟踪覆盖率分别提升36.7、64.5、61.7和65.1个百分点；冲突预警提前量在交叉场景为10.20 s、UAV辅助感知场景为9.07 s。颜色基线定位误差较高，YOLO基线在目标可见时定位准确但视觉缺失时跟踪中断。

### 四、结论（Conclusion）
结果表明，异质UAV-UGV融合能在视觉观测间歇时维持目标估计，显著提高空中跟踪连续性和鲁棒性，并支持交叉与共享区域场景的冲突预警。由于融合法与YOLO基线共用同一检测器，其性能增益可归因于UGV状态信息的引入而非更强视觉检测器。该方法适用于无固定感知基础设施下的车队监控与地面感知辅助，但当前证据限于仿真小尺度场景。

### 五、方法论与关键技术细节
关键实现点包括：颜色基线无需训练但易受视角、光照、标记可见性和几何投影误差影响；YOLO标签从RGB可见标记生成以避免前视相机几何投影造成错误标签，检测结果通过边界框测距模型转换为位置；融合法不引入额外学习损失或复杂超参，核心是根据视觉检测可用性在视觉更新与UGV状态预测之间切换；评价指标含检测覆盖率、跟踪覆盖率、RMSE、MAE、位置标准差、假阳性、ID切换和冲突提前量；局限为仅仿真验证、小尺度车辆、预定义轨迹，并假设UGV状态可共享且未充分建模通信延迟与状态不确定性。
