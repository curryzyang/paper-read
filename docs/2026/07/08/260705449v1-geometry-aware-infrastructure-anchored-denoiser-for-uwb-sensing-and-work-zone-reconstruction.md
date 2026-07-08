# Geometry-Aware Infrastructure-Anchored Denoiser for UWB Sensing and Work-Zone Reconstruction

- 区域：精读区
- 排名：5
- 匹配度：2.6/10
- 来源：arxiv
- 作者：Weizhe Tang, Jiaxi Liu, Junwei you, Steven T. Parker, Pei Li, Sikai Chen, Meng Ran, Bin Ran
- 机构：University of Wyoming, University of Wisconsin-Madison, Chongqing University of Posts and Telecommunications
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.05449v1) · [PDF](https://arxiv.org/pdf/2607.05449v1)

## TLDR
GAIA introduces a geometry-aware, infrastructure-anchored denoising framework that jointly models temporal UWB ranges and latent anchor layouts to produce boundary-consistent work-zone reconstructions, achieving state-of-the-art range MSE and polygon IoU on real-world outdoor datasets.

## Abstract
Accurate work-zone geometry perception is critical for intelligent transportation systems, and ultra-wideband sensing offers a low-cost approach for infrastructure-aided reconstruction. However, outdoor UWB ranging is often degraded by non-line-of-sight propagation, burst noise, and long-tail errors, which can distort downstream spatial reconstruction. We present GAIA, a geometry-aware, infrastructure-anchored learning framework that couples temporal range modeling with latent anchor-layout estimation and deterministic distance projection. GAIA preserves range denoising as the supervised task while orienting the learned distances toward boundary-consistent reconstruction. We evaluate GAIA on a real-world outdoor UWB dataset with synchronized UWB, GNSS, and IMU measurements, and further test robustness using a real-data-calibrated stress-test simulator. GAIA achieves the lowest overall range MSE and highest polygon IoU among evaluated filtering-based and learning-based baselines, reducing MSE by 18.4% and improving polygon IoU by 15.5% over PoseMLP. These results show that geometry-aware range denoising provides an effective path toward spatially coherent work-zone reconstruction.


## 精读解读（中文）
### 一、研究动机
现有UWB测距在室外施工区常受非视距传播、突发噪声和长尾误差影响，导致下游空间重建失真。现有方法主要进行信号级测距去噪，未显式建模几何结构；且仅优化平均测距误差不足以实现可靠的边界重建，因为关键锚点误差对重建质量影响远大于非关键锚点。

### 二、技术方案（Method）
输入为车辆轨迹序列（RTK-GNSS）、多锚点UWB原始测距及有效性掩码。GAIA由六个模块组成：PoseMLP Base（预训练冻结，提供初始锚点级测距估计）、Temporal Refinement（双向GRU+LayerNorm，捕捉时序依赖与跨锚相关）、Layout Head（对时序特征取均值后经MLP预测潜在锚点布局）、GeoDist（根据潜在布局和车辆轨迹确定性计算几何一致距离）、Prediction Head（基于时序特征输出残差校正和门控信号）、Gated Fusion（通过门控自适应融合几何距离与学习残差，输出最终去噪距离）。训练目标结合测距监督与几何一致性正则化，使去噪距离朝向边界一致的重建。

### 三、结果（Result）
在真实室外UWB数据集上，GAIA在所有评估的滤波与学习基线中取得最低整体测距MSE和最高多边形IoU：相比PoseMLP，MSE降低18.4%，IoU提高15.5%。在真实数据标定的仿真应力测试中，GAIA在强NLOS和长尾误差下仍保持鲁棒，验证了其几何感知设计的有效性。

### 四、结论（Conclusion）
GAIA通过将几何感知引入基础设施锚定的UWB测距去噪，显著提升了施工区边界重建的精度与空间一致性。实验表明，几何感知测距去噪是通往空间连贯重建的有效路径，在真实数据上优于仅优化测距误差的方法。

### 五、方法论与关键技术细节
关键点：1）使用RTK-GNSS作为轨迹输入，隔离测距去噪影响，对应上限设定；2）双向GRU利用过去和未来上下文，适用于事后重建或有限延迟的近实时映射；3）潜在布局推断提供显式空间先验，并通过GeoDist确定性投影得到物理合理距离；4）门控融合允许模型自适应平衡学习校正与几何一致性；5）局限性包括：依赖高精度轨迹（未来可探索噪声轨迹鲁棒性）和非因果时序（未来可扩展因果版本）。
