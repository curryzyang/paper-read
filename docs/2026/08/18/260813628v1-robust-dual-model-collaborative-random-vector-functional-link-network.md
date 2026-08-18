# Robust Dual-Model Collaborative Random Vector Functional Link Network

- 区域：精读区
- 排名：8
- 匹配度：4.2/10
- 来源：arxiv
- 作者：A. Quadir, A. Rahaman, Mushir Akhtar, M. Tanveer
- 机构：Indian Institute of Technology Indore
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.13628v1) · [PDF](https://arxiv.org/pdf/2608.13628v1)

## TLDR
This paper proposes KRPRVFL, a robust random vector functional link network that integrates the kernel risk-sensitive mean p-power criterion with collaborative learning to effectively handle label noise, outliers, and imbalanced data, consistently outperforming baseline models on benchmark classification tasks.

## Abstract
Random vector functional link (RVFL) networks are lightweight and fast neural models that offer efficient training and strong generalization through randomized hidden-layer weights and direct input-output connections. However, conventional RVFL models are sensitive to noisy labels, outliers, and imbalanced data, which limits their performance in real-world applications. To address these challenges, we propose the kernel risk-sensitive mean p-power based RVFL (KRPRVFL) model, which integrates the computational efficiency of RVFL with the robustness of the kernel risk-sensitive mean p-power (KRP) criterion. By replacing the standard least-squares objective with a KRP-based loss, KRPRVFL adaptively reduces the influence of corrupted or unreliable samples during training, resulting in improved stability and generalization. Additionally, a collaborative learning mechanism is introduced to enable adaptive interaction among model components, further enhancing robustness in complex and noisy environments. The proposed framework also leverages kernel-induced feature mapping to capture nonlinear relationships without requiring explicit hidden-layer selection, maintaining both efficiency and scalability. Extensive experiments on UCI and KEEL benchmark datasets demonstrate that KRPRVFL consistently outperforms baseline models in terms of accuracy, robustness, and statistical significance, highlighting its effectiveness as a fast, scalable, and reliable solution for challenging classification tasks.


## 精读解读（中文）
### 一、研究动机
传统随机向量函数链接（RVFL）网络虽然训练快、泛化能力强，但采用最小二乘目标且对所有样本平等对待，对噪声标签、异常值和不平衡数据高度敏感，限制了其在真实复杂环境下的分类性能。

### 二、技术方案（Method）
提出基于核风险敏感均值p次幂准则的RVFL模型（KRPRVFL）。输入为带标签样本，使用RVFL的随机隐藏层映射与输入输出直连，并用高斯核诱导特征空间；将原始最小二乘损失替换为KRP经验损失，即最小化正则项与各样本指数型核偏差之和；通过梯度置零推导出输出权重的闭式迭代更新公式，利用对角权重矩阵Ω自适应降低异常样本影响；同时引入协作学习机制，使模型组件间动态交互以增强鲁棒性；根据样本数与特征维度选择等价逆矩阵形式求解。

### 三、结果（Result）
在UCI和KEEL多个基准数据集上的大量实验表明，KRPRVFL在准确率、鲁棒性和统计显著性方面一致优于多种基线RVFL变体，验证了其在含噪、不平衡任务中的有效性与可靠性。

### 四、结论（Conclusion）
KRPRVFL成功将RVFL的计算效率与KRP准则的鲁棒性结合，有效抑制了噪声标签和异常值干扰，同时通过核映射避免隐层节点数选择问题，为复杂分类任务提供了一种快速、可扩展且稳健的解决方案。

### 五、方法论与关键技术细节
关键细节包括：KRP损失参数μ控制风险敏感程度，p控制偏差惩罚阶数，高斯核带宽σ决定相似度度量；正则化系数D用于控制模型复杂度；输出权重通过不动点迭代更新，并依据n与特征维数选择(H^TΩH+μ'I)^{-1}或等价形式；Ω对角线项结合核值、偏差幂次和指数因子动态加权样本；该模型避免了显式隐层节点数选择，但需调节μ、p、σ、D等超参数，且迭代求解在极大样本下仍有计算开销。代码见https://github.com/mtanveer1/KRPRVFL。
