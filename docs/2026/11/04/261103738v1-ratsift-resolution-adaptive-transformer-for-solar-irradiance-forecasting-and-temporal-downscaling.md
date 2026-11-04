# RATSIFT: Resolution-Adaptive Transformer for Solar Irradiance Forecasting and Temporal Downscaling

- 区域：精读区
- 排名：7
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Jesto Peter, Timothy M. Hansen, Hossein Moradi Rekabdarkolaee
- 机构：Bowling Green State University, Colorado State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.03738v1) · [PDF](https://arxiv.org/pdf/2611.03738v1)

## TLDR
RATSIFT is a resolution-adaptive Transformer that simultaneously forecasts and temporally downscales solar irradiance from arbitrary input resolutions to finer outputs, using genetic-algorithm hyperparameter optimization to improve efficiency and providing uncertainty estimates for grid-management applications.

## Abstract
Accurate forecasting and temporal downscaling of solar irradiance is critical for reliable renewable energy integration and grid management. Traditional methods often struggle to capture rapid irradiance variability. In this work, we develop a Transformer-based architecture for simultaneous forecasting and temporal downscaling. The model takes input data at arbitrary resolutions and generates outputs at any resolutions represented within the training data, leveraging both global and local contextual information. To improve training efficiency, a genetic algorithm-based optimization framework is implemented to identify suitable model hyperparameters, while reducing the computational cost of exhaustive grid search. The effectiveness of the proposed model is shown by analyzing real data in Dallas, Texas. The proposed model achieved root mean square error (RMSE) values of 28.785, 29.544, 30.157, 32.132~W/m\(^2\) for 15-, 30-, 60-minute, and irregularly spaced global input and producing forecast at 5-minutes resolution, respectively. Furthermore, this model produced reliable uncertainty estimates, exhibiting wider prediction intervals for high-resolution inputs during volatile solar conditions, whereas coarser-resolution inputs result in narrower intervals and significantly lower training time and computational cost. Our approach provides a scalable and efficient framework for multi-resolution solar irradiance forecasting and temporal downscaling, suitable for practical energy forecasting and grid management applications.


## 精读解读（中文）
### 一、研究动机
光伏渗透率提升使太阳辐照度的准确预测与时序降尺度对并网稳定、分布式资源聚合和电力市场运行至关重要。传统方法难以捕获快速辐照度波动，而现有Transformer预测器通常假设输入输出分辨率固定且对超参数选择敏感，难以适应异质时间分辨率数据和高分辨率预测需求。

### 二、技术方案（Method）
基于得克萨斯州达拉斯2024年NSRDB 15分钟GHI与本地5分钟地面观测，构建分辨率自适应Transformer：输入任意粗分辨率或不等间隔GHI，经Conv1D令牌嵌入、月日星期小时分钟五分量学习式时间嵌入和正弦位置编码后送入多层自注意力编码器，解码器以标签段加末值重复填充并通过交叉注意力一次性输出未来24小时5分钟预测。数据预处理包括重复时间戳保留首条、缺失值PCHIP插补、原始幅值不标准化，并用遗传算法以RMSE为评价指标搜索超参数，与Informer、Autoformer、FEDformer和非平稳Transformer对比。

### 三、结果（Result）
在达拉斯真实数据上，15、30、60分钟及不规则间隔全局输入对应5分钟分辨率预测的RMSE分别为28.785、29.544、30.157和32.132 W/m^2。模型能给出可靠不确定性估计，波动条件下高分辨率输入预测区间更宽，粗分辨率输入区间更窄且训练时间和计算成本显著降低。

### 四、结论（Conclusion）
结果表明RATSIFT可在统一框架内完成多分辨率太阳辐照度预测和时序降尺度，在精度、不确定性和计算效率之间取得可扩展平衡，适合实际能源预测与电网管理应用。该工作为异质分辨率时序数据的单次多步预测提供了可行范式，并提示可通过更丰富特征和实际部署约束进一步扩展。

### 五、方法论与关键技术细节
数据包含NSRDB 35,136条15分钟GHI无缺失和本地103,744条5分钟观测，后者有12个重复时间戳与1,910个缺失值并用保形PCHIP插补；模型输入特征数为1，目标为5分钟分辨率，解码器由T_label观测段和重复末值填充段构成，GA通过随机种群、按RMSE保留前n个候选、交叉变异迭代至收敛来降低网格搜索成本。实现上使用原始数据不做标准化，卫星GHI相对地面观测更平滑导致幅值与高频变异性不匹配，位置编码按批内行偏移生成而非真实时间位置，且注意力复杂度和超参数搜索成本仍是主要约束。
