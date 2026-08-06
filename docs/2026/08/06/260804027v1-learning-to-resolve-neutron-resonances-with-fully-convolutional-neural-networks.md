# Learning to Resolve Neutron Resonances with Fully Convolutional Neural Networks

- 区域：精读区
- 排名：8
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Nataly R. Panczyk, Athanasios Stamatopoulos, Josef Svoboda, Majdi I. Radaideh
- 机构：Los Alamos National Laboratory, University of Michigan
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.04027v1) · [PDF](https://arxiv.org/pdf/2608.04027v1)

## TLDR
This paper investigates a fully convolutional neural network to automatically detect neutron resonances in transmission spectra, achieving ~93% accuracy but revealing limited generalization to unseen isotopes and underscoring the need for more diverse training data and physics-informed features.

## Abstract
This work investigates the feasibility of augmenting traditional R-Matrix codes with a robust machine learning framework for automatically detecting neutron resonances in transmission spectra. Neutron transmission data are often complex and noisy, making them difficult to analyze using traditional peak-identification methods. The state-of-the-art R-Matrix codes currently used by physicists to fit these data often depend on prior evaluations and require substantial manual effort. This preliminary study demonstrates a method for accelerating the post-experimental processing of neutron transmission data and reducing bias associated with dependence on prior evaluations. We employ a fully convolutional neural network to classify individual points as belonging to resonance or non-resonance regions in seven transmission spectra---two evaluated and five experimental. Although the model achieves classification accuracies in the range of 93\%, further analysis shows that this metric overstates its ability to generalize. Building on our prior analysis in PHYSOR 2026, we find that, despite the inclusion of additional training data, the method does not generalize reliably to previously unseen isotopes. To address these limitations, future work should evaluate whether a larger and more diverse training dataset can produce a generalizable model and should incorporate known physical characteristics of neutron resonances to improve model performance.


## 精读解读（中文）
### 一、研究动机
传统R-Matrix代码（如SAMMY/REFIT）拟合中子透射谱中的共振时，依赖先验评价且需要大量人工干预，且容易得到非物理解。本文旨在探索用全卷积神经网络自动检测中子透射谱中的共振区，以加速实验后处理并减少对先验评价的依赖，同时不替代现有白盒物理代码，而是作为辅助峰查找工具。

### 二、技术方案（Method）
使用一维全卷积神经网络（1D FCN）对透射谱逐点分类为共振/非共振。数据包括7个透射谱：Cs-133和Sm-149评价谱，以及Sm-149、Sm-147、Cu-63、Ir-191、Ir-193实验谱（来自DICER/LANSCE）。预处理：先用B样条拟合原始噪声谱（残差约1e-16），再在均匀能量网格上重采样为256000个点；通过交互式工具用SAMMY参数文件辅助标注峰区域，非峰标0、峰标1，污染物和模糊区标2/3但在训练中视为0；省略能量特征以增强材料无关性；将数据随机打乱并分割为长度1000的序列，不做重叠。模型架构：无全连接层，包含两组1D卷积+批归一化交替，后接Dropout，再接两个1D卷积层；逐像素输出概率，阈值0.5分类。训练：Adam优化器，二元交叉熵损失（logits），正类权重1.33以缓解类别不平衡，余弦退火学习率，训练50轮。针对三个泛化案例分别训练，每个案例用4个谱训练、2个谱测试；另训练了3个单谱对照模型。

### 三、结果（Result）
模型在分类准确率上达到约93%，但该指标高估了泛化能力。进一步分析表明，在三个跨同位素测试案例中，模型无法可靠泛化到未见过的同位素；即使增加了训练数据（相比PHYSOR 2026前作），泛化问题依旧存在。在部分测试谱上，模型对峰区域的识别精度与召回率不理想，尤其在峰密度较低的高能区表现较差；单谱模型在同谱测试上表现较好，但缺乏实际应用价值。

### 四、结论（Conclusion）
初步研究表明，1D FCN能学习透射谱中共振区域的模式，并在训练数据上达到较高分类准确率，但目前无法可靠泛化到未见过同位素。未来需要更大且更多样化的训练数据集，并将中子共振的已知物理特性（如Breit-Wigner形状、能量相关峰宽等）纳入模型，以提升泛化能力和物理一致性。该方法应与SAMMY等R-Matrix代码结合使用，而非替代。

### 五、方法论与关键技术细节
数据与标注：7个谱，2个评价谱（Cs-133, Sm-149 ENDF/B-VIII.0）和5个实验谱（Sm-149, Sm-147, Cu-63, Ir-191, Ir-193）；标注工具基于SAMMY参数文件定位峰，低能区峰更明显且标注更频繁，导致峰密度随能量变化；序列长度1000，无重叠，数据打乱打散能量连续性以增强训练多样性。训练配置：正权重1.33固定（基于最不偏斜的Sm-149实验谱），binary cross entropy with logits loss，cosine annealing，Adam，50轮。输入仅透射值（0-1），未缩放，刻意排除能量使模型不依赖特定同位素能量刻度。复杂度/约束：256000点均匀采样但不同谱能量范围不同导致点间距不一致，可能影响性能；逐像素预测要求比实际峰定位更精细，引入额外误差；模型仅为初步峰检测，不提供共振参数。局限性：训练数据量小、类别不平衡、标注主观性、跨同位素泛化失败；评价谱与实验谱存在域差异；评估指标需结合峰级度量而非仅像素级准确率。
