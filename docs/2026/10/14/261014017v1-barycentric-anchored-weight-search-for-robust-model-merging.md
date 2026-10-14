# Barycentric Anchored Weight Search for Robust Model Merging

- 区域：精读区
- 排名：9
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Antoni Buades, Jose-Luis Lisani
- 机构：Universitat de les Illes Balears
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.14017v1) · [PDF](https://arxiv.org/pdf/2610.14017v1)

## TLDR
TLDR: Barycentric Anchored Search is a lightweight, post-hoc, derivative-free weight-space merging method that uses a pre-trained anchor and two fine-tuned checkpoints, guided by small out-of-distribution validation subsets, to improve robust vision model performance under distribution shift without extra training or inference cost.

## Abstract
We propose Barycentric Anchored Search, a post-hoc weight-space procedure for improving fine-tuned vision models under distribution shift without additional gradient training or increased inference cost. Given a pre-trained initialization and two checkpoints fine-tuned on a source dataset, the method constructs barycentric candidate weights and performs a small derivative-free search along directions connecting each candidate to the pre-trained model. Candidate weights are selected using a small validation subset of one or more out-of-distribution (OOD) datasets; the selected model is then evaluated on the held-out portions of those datasets, on additional OOD benchmarks, and on the ImageNet validation set to quantify the robustness-accuracy trade-off. The method is inspired by simplex-based derivative-free optimization, including Nelder-Mead and Torczon multidirectional search, but is specialized to the geometry of neural network weight merging. Unlike Model Soup, which typically benefits from many fine-tuned checkpoints, and unlike Model Stock, which applies a fixed geometric merge, our approach uses only two fine-tuned checkpoints and iteratively adapts the merge using validation feedback from OOD data. Experiments with CLIP ViT-B/32 show that the proposed search substantially improves performance on held-out OOD data, including ImageNet-A, ImageNet-R, and ImageNet-Sketch, while keeping ImageNet accuracy competitive. The resulting weights also improve transfer to OOD datasets not used during candidate selection, outperforming the original fine-tuned checkpoints, naive model soups, and Model Stock in our evaluations. These results suggest that lightweight optimization in anchored weight space provides a practical alternative to fixed weight-averaging rules, geometric merging, or single-model selection.


## 精读解读（中文）
### 一、研究动机
标准微调虽提升目标域精度，却常导致分布偏移下的鲁棒性下降；现有模型融合如 Model Soup 依赖大量检查点，Model Stock 采用固定几何插值，难以用少量检查点自适应利用 OOD 验证反馈。本文旨在不增加梯度训练与推理成本的前提下，利用预训练模型作为锚点，在权重空间中对两个微调检查点进行后处理搜索，以改善 OOD 鲁棒性并保持 ImageNet 精度。

### 二、技术方案（Method）
给定预训练权重 ω_P 和两个在同源数据上微调得到的检查点 ω_1、ω_2，先构造重心 ω_3=(ω_1+ω_2)/2；对候选 i=1,2,3 生成锚定扰动 ω_i^λ=ω_i+λ(ω_P−ω_i)，λ>0 向预训练锚点收缩、λ<0 远离锚点，并用 OOD 验证子集的准确率 F 判断是否替换原候选。第一阶段 λ 取 {-0.8,-0.6,-0.4,-0.2,0.2,0.4,0.6,0.8}，更新后计算二级重心 ω_4=(ω_1+ω_2+ω_3)/3，第二阶段以更小步长 {-0.04,-0.03,-0.02,-0.01,0.01,0.02,0.03,0.04} 对 i=1..4 重复扰动与验证更新，最终取 F 最高的单模型权重。实验在 CLIP ViT-B/32 上进行，使用来自 Model Stock 仓库的预训练权重和两个 ImageNet 微调检查点，按 ImageNet、ImageNet-A/R/Sketch 划分验证与测试子集，仅做权重组合与评估，不做梯度训练。

### 三、结果（Result）
在 CLIP ViT-B/32 上，BAS 在 ImageNet-A、ImageNet-R、ImageNet-Sketch 等留出 OOD 测试集上相较原始微调检查点、朴素 soup 和 Model Stock 取得更优或更具竞争力的鲁棒性，同时 ImageNet 精度保持接近。表中以 ImageNet-A 验证集引导的 BAS 将 ImageNet-A 从 Model Stock 的 0.3239 提升到 0.3571、ImageNet-R 从 0.6710 提升到 0.7150、ImageNet-Sketch 从 0.4706 提升到 0.4828，但 ImageNet 从 0.7967 降至 0.7635；以 ImageNet 验证集引导时 ImageNet 为 0.7946、OOD 平均为 0.4749。结果还显示，用于候选选择的 OOD 数据之外的额外 OOD 基准也能获得迁移提升。

### 四、结论（Conclusion）
BAS 表明，在预训练锚点约束下的轻量、无导数、验证驱动的权重空间搜索，可作为固定权重平均、几何融合或单模型选择的实用替代方案，尤其适合只有两个微调检查点且关注分布偏移鲁棒性的场景。其核心价值在于后处理、单模型推理、不增加推理成本，并能利用少量 OOD 验证反馈自适应权衡鲁棒性与精度。

### 五、方法论与关键技术细节
关键实现细节包括：仅用两个微调检查点加一个预训练锚点；两阶段由粗到细的 λ 搜索，分别采用 0.2 间隔和 0.01 间隔；候选更新规则为仅当验证准确率提升时接受；最终按验证准确率取 argmax；验证集来自一个或多个 OOD 数据的小子集，测试集与之不相交。方法受 Nelder-Mead 和 Torczon 多方向搜索启发，但不维护完整 d+1 单纯形，且不声称收敛到极小值。局限在于依赖 OOD 验证数据，选择结果与验证分布相关，实验仅覆盖 CLIP ViT-B/32 与两个 ImageNet 微调检查点，且可能以 ImageNet 精度下降换取 OOD 鲁棒性；无额外梯度训练或推理开销，但需要多次前向评估候选权重。
