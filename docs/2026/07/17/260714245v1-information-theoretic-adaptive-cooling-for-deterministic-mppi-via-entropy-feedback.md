# Information-Theoretic Adaptive Cooling for Deterministic MPPI via Entropy Feedback

- 区域：精读区
- 排名：6
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Shuqi Wang, Wenrong Sun, Tao Han, Yue Gao, Xiang Yin
- 机构：Shanghai Jiao Tong University, The Hong Kong University of Science and Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.14245v1) · [PDF](https://arxiv.org/pdf/2607.14245v1)

## TLDR
This paper introduces Information-Theoretic Adaptive Cooling (ITAC), a framework that uses Shannon entropy of importance weights as online feedback to adaptively regulate temperature in deterministic MPPI, achieving faster convergence and improved sampling efficiency without sacrificing the derivative-free nature of the algorithm.

## Abstract
This paper investigates deterministic optimal control using Model Predictive Path Integral (MPPI) control, a sampling-based and derivative-free framework well suited for systems with complex dynamics and nonsmooth objectives. In deterministic MPPI, the temperature must be driven to zero to recover the true optimum, yet the design of an effective cooling schedule remains a fundamental challenge. Existing methods typically rely on predefined open-loop schedules, which limit the efficiency and robustness of the algorithm. To overcome this limitation, we propose an Information-Theoretic Adaptive Cooling (ITAC) framework that uses the Shannon entropy of the importance weights as an online feedback signal to regulate the temperature. The proposed mechanism adapts the cooling rate to the current sampling state, enabling fast progress when the weights are diffuse and cautious cooling when they become concentrated. We prove asymptotic convergence of the resulting scheme to the deterministic optimum, and further derive a critical entropy threshold that leads to a smooth barrier against premature weight collapse. Experiments on nonsmooth signal temporal logic motion-planning tasks show that ITAC improves sampling efficiency and achieves substantially faster convergence than state-of-the-art baselines without sacrificing the derivative-free nature of MPPI.


## 精读解读（中文）
### 一、研究动机
在确定性MPPI控制中，温度必须降至零以恢复真正最优，但现有冷却调度为预定义开环方式，限制了效率和鲁棒性。因此需要一种自适应冷却机制来平衡收敛速度与防止权重过早崩溃。

### 二、技术方案（Method）
提出信息论自适应冷却（ITAC）框架，以重要性权重的香农熵作为在线反馈信号调节温度。具体地，定义归一化采样熵Ĥ，并采用自适应冷却调度λ_{j+1}=Γ(Ĥ_j)λ_j，其中Γ为Ĥ的递减函数。框架证明渐近收敛到确定性最优，并推导出关键熵阈值作为防止权重崩溃的光滑屏障。在非光滑信号时序逻辑运动规划任务中验证。

### 三、结果（Result）
实验表明ITAC显著提高采样效率，收敛速度相比现有基线提升高达73%。在非光滑信号时序逻辑任务上验证了稳定性和加速效果。

### 四、结论（Conclusion）
ITAC框架通过熵反馈自适应调节冷却速率，有效平衡了探索与利用，保证了渐近最优性，同时维持了MPPI无导数优化的优势，适用于复杂动力学和非光滑代价问题。

### 五、方法论与关键技术细节
关键点：采用香农熵作为冷却速率的反馈信号；推导临界熵阈值防止玻璃化；理论证明渐近收敛至最优；冷却函数Γ需满足递减且值域(0,1)；保持R=λΣ^{-1}恒定以维持自由能结构；方法保持无导数特性，适用于非光滑代价。
