# State-Space Unlearning for Non-Stationary Bias in Land Surface Forecasting

- 区域：精读区
- 排名：10
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Anidipta Pal
- 机构：Heritage Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.02248v1) · [PDF](https://arxiv.org/pdf/2610.02248v1)

## TLDR
SSU-LSF is a machine-unlearning framework for Mamba-based land surface forecasting that removes non-stationary confounding bias from state-transition matrices via EKFac influence functions, temporal footprint localization, and Hessian-free projected gradient ascent with spatial TV regularization, achieving high confounding reduction with minimal clean-domain degradation and far lower cost than retraining.

## Abstract
Operational land surface forecasting systems built on Mamba-family Structured State Space Models absorb non-stationary confounding events (unrecorded irrigation booms, dam-operation shifts, sensor recalibrations) into their state-transition matrices, silently biasing NDVI, LST, and crop phenology predictions long after the physical cause ends. This paper introduces SSU-LSF (State-Space Unlearning for Land Surface Forecasting), the first machine-unlearning framework purpose-built for geoscientific Mamba-based SSMs. We develop EKFac influence functions specialized to the Mamba state matrices via a closed-form matrix-exponential gradient, use spectral-radius-weighted elbow thresholding to localize a temporal confounding footprint $Φ$, and apply Hessian-free projected gradient ascent within a KL-divergence trust region augmented by spatial total-variation (TV) regularization. Proposition 1 establishes that residual confounding is bounded by $\mathcal{O}\big((1-ρ(\bar{A})^{T_c})/((1-ρ(\bar{A}))μ)\big)$, which grows with the window length $T_c$. Across three heterogeneous benchmarks and eleven baselines, SSU-LSF achieves confounding reduction rates of $0.773$ (CropHarvest), $0.821$ (NDVI-LST), and $0.859$ (ERA5), with worst-case clean-domain RMSE degradation of $4.2\%$ on ERA5, converging in 3--5 epochs at $8.4\times$ lower GPU-cost per unlearning request than full retraining. Code: https://github.com/Anidipta/SSU-LSF


## 精读解读（中文）
### 一、研究动机
业务化地表预报系统常采用Mamba族结构化状态空间模型，但会把未记录灌溉扩张、水坝调度变化、传感器重校准等非平稳混杂事件吸收进状态转移矩阵，并在物理原因结束后继续污染NDVI、LST和作物物候预测。全量重训练成本高达数十GPU小时，而梯度反转、SISA等已有遗忘方法会显著损伤干净域性能或依赖预分片，缺少面向地理科学Mamba SSM循环结构的机器遗忘框架。

### 二、技术方案（Method）
SSU-LSF以Mamba编码器-解码器为骨干，输入多变量地表观测，在给定混杂时间窗后求解带KL信任域约束的目标：提升对混杂窗口的损失、保留干净域损失并加入参数空间空间TV正则。方法先通过面向Mamba状态矩阵的EKFac影响函数与闭式矩阵指数梯度估计逐时刻影响，再用谱半径加权肘部阈值法定位时间混杂足迹Φ，最后在KL散度信任域内执行无Hessian投影梯度上升，并用空间TV约束相邻patch参数平滑，超出信任域时通过二分行搜索回缩。训练采用AdamW、余弦学习率、100轮和4张A100，遗忘阶段逐请求重新估计EKFac，复杂度约为O(|Wc|·d^2/B)，低于全量重训练的O(T·d^2)。

### 三、结果（Result）
在三个异构基准和十一个基线对比中，SSU-LSF取得混杂削减率CRR为0.773（CropHarvest）、0.821（NDVI-LST）和0.859（ERA5），并在ERA5上把最坏干净域RMSE退化控制在4.2%。方法通常3至5轮收敛，每个遗忘请求的GPU成本比全量重训练低8.4倍，且在真实EUMETSAT SEVIRI 2010—2012重校准事件上验证了Tc敏感性，经验R²为0.995。

### 四、结论（Conclusion）
SSU-LSF是首个面向地理科学Mamba状态空间模型的机器遗忘框架，能够定位并移除由非平稳混杂事件写入状态矩阵的偏差，在保持干净域精度的同时显著降低遗忘计算成本。其理论界表明残余混杂随混杂窗口长度Tc增长，这为缩短污染窗口和部署在线遗忘提供了可操作依据，但作者注入混杂、理论界偏松和部署场景限制仍需后续验证。

### 五、方法论与关键技术细节
关键实现包括47.3M参数Mamba骨干，6个块、d=256、E=2、N=16，4×4步长4 patch嵌入和3层高斯MLP预测头；数据为NDVI-LST 3847地点2002—2022、ERA5 1920 patch 1979—2022、CropHarvest 87343地点，混杂窗口Tc分别为24、24、6个月。遗忘超参为η=5e-5、β=0.6、δKL=0.05、γ=95百分位、λTV=0.01，单请求GPU成本约为NDVI-LST 1.8、ERA5 5.6、CropHarvest 3.0 GPU小时。理论部分给出编码器Lipschitz界、RKHS分离μ_ref和收敛保证，但μ_ref在独立参考模型上估计；主要局限是三个基准均使用作者注入混杂，真实事件仅附录验证，且Proposition 1的界与观测差距约200倍，说明其定量紧致性有限。
