# Geometry-aware Latent Autoregressive Generative Model for PDEs in Complex Domains

- 区域：精读区
- 排名：2
- 匹配度：5.7/10
- 来源：arxiv
- 作者：Zi Wang, Minghui Xu, Tapan Mukerji
- 机构：Stanford University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.00297v1) · [PDF](https://arxiv.org/pdf/2609.00297v1)

## TLDR
GeoLAMP is a geometry-aware latent autoregressive generative model that uses dual graph encoders, a causal self-attention transformer with flow matching, and an arbitrary decoder to accurately and stably solve multiphysics PDEs in highly complex, tortuous μm-scale geometries.

## Abstract
Solving multiphysics partial differential equations (PDEs) remains a major challenge in scientific computing, especially for highly complex $μ$m-scale tortuous geometries critical to energy and chemical engineering. We address this challenge by proposing a Geometry-aware Latent Autoregressive generative Model for PDEs (GeoLAMP) for solving physics within highly irregular and tortuous structures. GeoLAMP introduces a dual-encoder architecture on graph representations to jointly capture global topology and fine-scale geometric features, enabling an effective transition from real-space fields to compact latent representations. In the latent space, we propose a causal self-attention transformer with flow matching to model temporal dynamics, allowing stable and scalable block-wise autoregressive prediction. A flexible decoder reconstructs high-resolution physical fields on arbitrary points. We establish three multiphysics benchmark datasets in complex geometries, covering reactive flow, heat convection, and elasticity. GeoLAMP consistently achieves the most stable autoregression performance on these datasets, maintaining low errors throughout the entire rollout horizon. Our results provide a systematic study of geometry-aware learning for PDEs in $μ$m-scale complex geometries and offer new insights into block-wise time marching of latent autoregressive PDE modeling via a flow matching framework.


## 精读解读（中文）
### 一、研究动机
求解复杂微米级迂曲几何结构中的多物理场偏微分方程是科学计算中的重大挑战，尤其在能源与化学工程中至关重要。现有方法或受限于真实空间几何复杂度随规模剧增，或缺乏能同时保留全局拓扑与局部精细几何特征的几何感知潜空间建模能力，因此需要一种能在高复杂不规则结构上稳定高效地学习时空动力学的方法。

### 二、技术方案（Method）
GeoLAMP 采用双编码器图表示架构：全局编码器用最远点采样覆盖全域拓扑，局部编码器用基于曲率协方差特征分解的采样捕捉孔隙与高曲率局部细节，二者作为变分自编码器将真实空间场压缩到规则潜空间；潜空间中用带因果掩码自注意力的 Transformer 以流匹配目标建模时间动态，支持 M-to-M 分块自回归预测；灵活解码器通过带掩码的图神经算子将潜变量解码到任意空间位置。训练时对目标块构造线性插值 xt=(1-t)epsilon+t z，回归目标速度 u=z-epsilon，损失为速度场 L2 误差；推理时用 50 步欧拉积分求解概率流 ODE，并将预测块拼接回条件窗口实现滚动预测。

### 三、结果（Result）
在反应流、热对流和弹性力学三个复杂几何多物理基准数据集上，GeoLAMP 在完整自回归 rollout 和最终步预测中均获得最低的最终步相对 L2 误差，长时程误差保持低水平，自回归稳定性优于 Transolver、Geo-FNO、NUNO 和匹配的确定性潜空间回归基线等对比方法；在弹性数据集上 Transolver 平均 rollout 误差略低，但 GeoLAMP 的平均误差与最终步误差接近，说明长时间自回归更稳定。

### 四、结论（Conclusion）
GeoLAMP 通过几何感知的双编码器将真实空间物理场压缩为潜表征，再利用流匹配增强的因果自注意力 Transformer 进行分块自回归，能够在高度不规则微米级复杂几何中稳定预测多物理场动态；结果提示分块 rollout 不只是对后续状态的简单回归，而是学习到了深层时间依赖，为复杂几何下潜空间自回归 PDE 建模提供了系统研究和新思路。

### 五、方法论与关键技术细节
数据集由 COMSOL 有限元生成，覆盖三种微米级结构：圆堆积多孔结构中的反应流、随机场结构中的对流换热、泡沫结构中的弹性问题，均含线性和非线性边界条件。编码器使用 GNO 层，GNO 以 Green 函数近似在查询球内聚合信息；全局采样用 FPS 的最大最小欧氏距离准则，局部采样用邻域协方差最小特征值占比作为曲率分数并选最大者。潜空间模型以 SiT 为骨干，GeoLAMP-S 用交叉注意力做单步预测，GeoLAMP-B 用因果自注意力做 M=8 的无重叠分块预测；每块条件 token 在前，目标 token 在后，噪声 token 可关注所有前置条件键。训练时噪声只在目标块上构造，条件块作为 c 传入，损失对目标潜变量位置平均。推理时从高斯噪声出发欧拉积分 50 步。解码器支持任意分辨率重建，并引入掩码策略处理变长网格节点。局限性可能包括对训练几何分布的依赖、潜空间中几何信息的压缩损失，以及 rollout 误差累积仍需进一步控制。
