# KiRA: Kronecker Input-Gated Rank Adaptation for Parameter-Efficient Fine-Tuning of Pretrained Models

- 区域：精读区
- 排名：7
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Akil Ahmad Taki, Shaikh Anowarul Fattah
- 机构：Bangladesh University of Engineering and Technology (BUET)
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.33236v1) · [PDF](https://arxiv.org/pdf/2611.33236v1)

## TLDR
KiRA is a parameter-efficient fine-tuning method that uses a frozen random Kronecker factor to multiply the rank of a trainable input-gated low-rank update without adding trainable parameters, and it includes a pre-training criterion to predict when input conditioning will help, outperforming baselines with 8.7–9.7× fewer trainable parameters.

## Abstract
Full fine-tuning of large pretrained models is expensive, and parameter-efficient fine-tuning (PEFT) is the standard alternative. Most PEFT methods use low-rank updates, whose rank lies far below that of full fine-tuning and is the same for every input. Input-adaptive variants vary the capacity per input but remain within the low-rank bottleneck, and whether a task benefits from input conditioning is not known before training. This paper introduces Kronecker input-gated rank adaptation (KiRA). Instead of the conventional low-rank product, the update $ΔW$ is the Kronecker product of a frozen random $p\times p$ matrix $A$ and a trainable factor $M(x)$, which overcomes the rank ceiling: because rank is multiplicative under this product, $A$ multiplies the rank of $M(x)$ by $p$ without adding trainable parameters. The factor $M(x)$ is further decomposed as $B_1\,\mathrm{diag}(g(x))\,B_2$, where the input gate $g(x)$, computed once per sample by a network shared across all adapted layers, adjusts the rank of the update to each input in steps of $p$. Where input conditioning is unnecessary, the gate is folded into $B_1$ at deployment. Because the gate changes the rank only in discrete steps, the benefit of input conditioning can be predicted before training from a few hundred labeled inputs. Across six medical imaging and language benchmarks, KiRA attains the highest mean score against five published baselines with 8.7--9.7 times fewer trainable parameters than low-rank adaptation, and the pre-training criterion agrees with the measured benefit of input conditioning on all six tasks.


## 精读解读（中文）
### 一、研究动机
全量微调大模型成本高，PEFT 常用低秩更新，但低秩瓶颈导致更新秩远低于全量微调且对所有输入相同；现有输入自适应方法虽按样本调整容量，仍受低秩限制，而且任务是否能从输入条件化中获益在训练前未知。该文因此希望在显著减少可训练参数的同时突破低秩秩上限，并提供训练前判断是否值得引入输入门控的准则。

### 二、技术方案（Method）
KiRA 将适配更新设为 ΔW(x)=A⊗M(x)，其中 A 为冻结的 p×p 随机高斯满秩矩阵，M(x)=B1 diag(g(x)) B2 为可训练低秩因子，q=d/p，B1∈R^{q×r}、B2∈R^{r×q}。门控 g(x)=σ(Wg2 φ(Wg1 x̄)) 由所有适配层共享的瓶颈网络对样本均值池化表示 x̄ 计算一次，h=64，输出 r 维[0,1]门值；训练时冻结预训练权重 W0 与 A，仅学习 B1、B2 和门控网络，推理时若无需输入条件化可把门折叠进 B1。作者还采用低秩/克罗内克与静态/输入门控的因子实验，并设置参数匹配的常数门控对照，以分离门控网络参数与输入访问的贡献，同时在训练前用几百个标注输入计算自适应性比率决定是否启用输入门控。

### 三、结果（Result）
在六个医学影像与语言基准上，KiRA 相对五个已发表基线取得最高平均分，且可训练参数比低秩适配少 8.7–9.7 倍；参数匹配的常数门控对照表明精度优势主要来自克罗内克基底，输入条件化仅在准则选中的三个任务上带来增益。训练前准则在全部六个任务上与实测的输入条件化收益一致，说明门控是否有效可提前预测。

### 四、结论（Conclusion）
KiRA 通过冻结随机克罗内克因子为可训练低秩因子放大秩而不增加可训练参数，从而在更小参数预算下超过 LoRA 类基线，并用精确秩恒等式刻画硬门控的 rank(ΔW)=p k(x) 与软门控的有效秩/稳定秩乘法关系。其离散秩步长机制还导出了训练前可测的输入条件化判据，使是否采用更复杂输入自适应设计有据可依，并有利于在共享硬件上维护大量任务适配器。方法的主要约束是 p 必须整除维度、随机因子需满秩且谱分布良好，门控收益依赖任务且秩调节粒度较粗。

### 五、方法论与关键技术细节
关键实现细节包括：A 仅保存随机种子，取独立标准高斯且近似满秩，p 整除 d；每层可训练参数约 2dr/p，门控网络共享且仅增加 h(d+r) 个参数，h=64；硬门控下 rank(ΔW(x))=p k(x)，软门控给出有效秩与稳定秩的乘法式，放大秩会缩小可达子空间维度，形成秩放大与子空间维度间的权衡。输入为图像或句对，门值按样本计算一次；门控以 p 为步长改变秩，因此只有每样本秩需求变化超过一个步长的任务才可能受益。训练前判据只需几百个标注输入，并在预训练模型上测量；实验用参数匹配常数门控控制变量，覆盖六个医学影像和语言任务，但结论仍受限于这些基准、维度整除约束和随机因子谱条件。
