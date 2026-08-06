# Interpretable Fuzzy Inference for UAV Target Tracking Using Bounding-Box Geometry

- 区域：精读区
- 排名：3
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Reza Ahmari, Ahmad Mohammadi, Vahid Hemmati, Nicholas Edmond, Hossein Z. Saghazadeh, Olusola Odeyomi, Parham Kebria, Abdollah Homaifar
- 机构：North Carolina A&T State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.04121v1) · [PDF](https://arxiv.org/pdf/2608.04121v1)

## TLDR
The paper presents an interpretable fuzzy-inference framework that maps low-dimensional YOLO bounding-box features (centroid, area, aspect ratio) to continuous yaw commands for vision-based UAV tracking of ground vehicles, achieving high accuracy (e.g., ~0.14° mean absolute error) with a compact, data-efficient, and transparent 27-rule Takagi–Sugeno system.

## Abstract
Vision-based guidance of unmanned aerial vehicles (UAVs) toward unmanned ground vehicles (UGVs) supports cooperative aerial--ground robotics, but reliable continuous yaw estimation from onboard vision remains challenging because of sensing uncertainty, limited computation, and the need for interpretable control. Existing deep-learning and geometric-reconstruction approaches often require large datasets, external localization, or complex modeling assumptions, reducing transparency and deployment suitability on resource-constrained platforms. We present an interpretable fuzzy-inference framework that generates continuous yaw commands from low-dimensional features extracted from YOLO boxes: target centroid location, area, and aspect ratio. No explicit geometric modeling is required. A Mamdani fuzzy system serves as an interpretable baseline using a shoulder--triangle--shoulder input partition. It is followed by a first-order Takagi--Sugeno model with three antecedent membership terms per input, whose parameters are derived from training-set quantiles, yielding a compact 27-rule structure. Evaluation uses 6{,}169 labeled samples from a VICON motion-capture environment. Across five randomized train--test splits, the Takagi--Sugeno model achieves a test-set mean absolute error of $0.140^\circ \pm 0.003^\circ$, a root mean squared error of $0.200^\circ \pm 0.008^\circ$, and a maximum absolute error of $1.254^\circ \pm 0.121^\circ$. Within-threshold accuracies are $99.676% \pm 0.270%$ for $\pm1^\circ$ and $100.000% \pm 0.000%$ for both $\pm3^\circ$ and $\pm5^\circ$. Directional consistency between image-plane horizontal displacement and predicted yaw sign reaches $90.254% \pm 0.612%$. These results show that the framework is transparent, data-efficient, computationally lightweight, and suitable for real-time vision-based UAV guidance toward mobile ground targets.


## 精读解读（中文）
### 一、研究动机
视觉引导无人机追踪地面无人车是协同空地机器人的关键能力，但仅依靠机载视觉进行连续偏航角估计面临感知不确定性、计算资源有限和可解释性需求等挑战。现有深度学习和几何重建方法通常需要大规模数据集、外部定位或复杂建模假设，透明度低，难以在资源受限平台上实时部署。因此需要一种可解释、数据高效、计算轻量且适合实时视觉引导的连续偏航估计框架。

### 二、技术方案（Method）
提出一个可解释的模糊推理框架，输入为YOLO检测框提取的低维几何特征：目标质心水平位置、归一化面积和宽高比，输出连续偏航角。首先构建Mamdani模糊系统作为可解释基线，采用肩-三角-肩输入隶属函数划分；随后构建一阶Takagi-Sugeno模型，每个输入使用三个由训练集分位数导出的隶属函数，形成紧凑的27条规则结构。训练时，所有特征归一化和隶属函数参数仅从训练集获取，测试时保持不变；TS模型的后件线性参数通过最小二乘回归在训练集上辨识。评估使用VICON运动捕捉系统采集的6169个标注样本，并按五次随机训练测试划分进行验证。

### 三、结果（Result）
在五次随机划分的测试集上，Takagi-Sugeno模型取得平均绝对误差0.140°±0.003°，均方根误差0.200°±0.008°，最大绝对误差1.254°±0.121°。±1°阈值内准确率为99.676%±0.270%，±3°和±5°阈值内准确率均为100.000%±0.000%。图像平面水平位移与预测偏航角符号的方向一致性达到90.254%±0.612%。结果表明该框架透明、数据高效、计算轻量，适合实时视觉引导。

### 四、结论（Conclusion）
该模糊推理框架通过可解释的Mamdani基线和精确的一阶Takagi-Sugeno模型，在透明性与连续偏航回归精度之间取得了有效平衡，且无需显式几何建模。基于真实数据的多指标验证表明，该框架能够以极低计算成本可靠预测无人机对地面移动目标的偏航修正指令，适合部署在资源受限的机载平台上。

### 五、方法论与关键技术细节
关键细节包括：1) 防泄漏设计，所有归一化参数和隶属函数参数仅从训练集分位数计算，测试集不参与；2) 覆盖安全的肩-三角-肩输入划分减少边界激活模糊，保持27条规则的紧凑结构；3) Mamdani基线使用鲁棒百分位归一化并映射到[0,1]，TS模型直接使用原始特征尺度的训练分位数；4) TS模型后件为输入的一阶线性函数，通过训练集最小二乘辨识；5) 数据来自VICON运动捕捉系统，共6169个标注样本，五次随机70/30划分；6) 评估指标包括MAE、RMSE、最大绝对误差、阈值内准确率和方向一致性；7) 当前为离线评估，部署时预测偏航角可输入低层偏航率或姿态控制器，但未在真实控制回路中验证，且方法针对特定目标跟踪场景。
