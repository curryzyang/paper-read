# Uncertainty-Aware Parameter Estimation for Condition Monitoring of Power Converters

- 区域：精读区
- 排名：8
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Tomas Monopoli, Jiahong Liu, Shuai Zhao
- 机构：Aalborg University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.00218v1) · [PDF](https://arxiv.org/pdf/2609.00218v1)

## TLDR
The paper proposes an uncertainty-aware Bayesian parameter estimation framework for power converter condition monitoring that provides local Gaussian posteriors via Laplace approximation, enabling uncertainty quantification, consistency testing, and precision-weighted pooling, and demonstrates that while well-identified parameters are accurately estimated, parameters like MOSFET on-resistance have weak practical identifiability under typical sensing configurations.

## Abstract
Parameter estimation is widely used for condition monitoring of power converters, but most existing methods provide only point estimates and therefore cannot quantify whether an observed parameter change is statistically significant. This paper proposes an uncertainty-aware parameter estimation framework based on Bayesian maximum a posteriori optimization and a differentiable converter model. A Laplace approximation is used to obtain a local Gaussian posterior, enabling uncertainty quantification, consistency testing, estimator-resolution analysis, and precision-weighted pooling across data windows. The method is validated on synthetic and hardware Buck converter. It demonstrates accurate estimation of well-identified parameters and reveal the weak practical identifiability of parameters such as MOSFET on-resistance under the available sensing configuration.


## 精读解读（中文）
### 一、研究动机
现有电力电子变换器参数估计方法大多只给出点估计，无法量化观测到的参数变化在统计上是否显著，也难以区分估计噪声与真实退化，因此难以支撑基于统计显著性的状态监测与变化检测。论文提出一种不确定性感知的参数估计框架，通过贝叶斯后验分布而非单一数值来表征参数估计质量。

### 二、技术方案（Method）
该方法基于贝叶斯最大后验（MAP）优化，结合可微分的Buck变换器物理前向模型。具体流程为：以硬件或仿真采集的输入输出数据为观测，建立负对数后验损失（数据似然项加先验项）；使用Adam与L-BFGS的序列组合优化该损失以求得MAP点估计；在最优解处对负对数后验进行二阶泰勒展开，用其Hessian矩阵构造Laplace近似的局部高斯后验。为获得校准的不确定性，引入基于有限冲激响应（FIR）的白化算子处理积分器残差的相关性及有色噪声和周期性扰动；再通过谱正则化对后验协方差进行条件化处理，使不同工作点下的后验可相互比较。基于所得后验，还可进行一致性检验、分辨率分析以及跨数据窗的精度加权融合。

### 三、结果（Result）
在仿真数据上，该方法与已知PINN基准相比实现了约20倍的速度提升，同时提供了校准后的不确定性；在硬件Buck变换器测试台上，该方法恢复了物理上正确的参数值，验证了不同工作点后验的可比性，并能以量化分辨率检测出电流相关电感偏移和模拟电容老化等元件级变化。此外，实验揭示了在现有传感配置下，某些参数（如MOSFET导通电阻）的实际可辨识性较弱，而对良好可辨识的参数则能实现准确估计。

### 四、结论（Conclusion）
该不确定性感知贝叶斯参数估计框架为电力电子变换器状态监测提供了一种统计上严谨的工具，不仅能够给出参数的点估计，还能量化其不确定性、支持估计分辨率分析、跨工作点比较和基于精度加权的多窗口融合，从而可靠地检测参数漂移或退化。研究同时指出，参数能否被准确估计取决于当前传感配置下的实际可辨识性，这为未来传感设计和监测策略提供了重要启示。

### 五、方法论与关键技术细节
数据与输入：使用合成仿真数据和硬件Buck变换器测量数据，无创采集正常运行数据，无需额外信号注入。先验：通过先验分布融合数据手册公差或历史测量等知识。损失：负对数后验包含数据项和先验项，噪声模型采用基于FIR白化算子的广义最小二乘结构以处理残差相关性与有色噪声。优化：Adam+L-BFGS序列优化，Hessian来自优化器曲率信息，Laplace后验近似额外成本可忽略。协方差正则：基于损失景观对工作点结构依赖的谱正则化，保证跨工作点后验可比性。复杂度/限制：方法在非线性模型下为局部后验近似，弱可辨识参数（如MOSFET导通电阻）在现有传感配置下估计不确定性大；Laplace近似与局部优化不保证全局最优，且模型失配时需靠白化与正则化缓解；与MCMC相比计算高效，但仍有模型-现实差异敏感性。
