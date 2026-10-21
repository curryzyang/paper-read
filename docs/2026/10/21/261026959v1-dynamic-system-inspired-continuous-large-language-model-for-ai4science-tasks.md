# Dynamic System Inspired Continuous Large Language Model for AI4Science Tasks

- 区域：精读区
- 排名：3
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Zhaoxin Fan, Zheng Zhu, Yuqing Ma, Faguo Wu, Jian Yang, Wenjun Wu
- 机构：Beihang University, GigaAI
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.26959v1) · [PDF](https://arxiv.org/pdf/2610.26959v1)

## TLDR
Continuum-LM reuses pretrained residual transformations as continuous-depth ODE operators in a language model, enabling extra latent computation without expanding the backbone and improving mean exact-match accuracy on eight AI4Science tasks by 7.77 and 10.96 points over discrete counterparts at 0.6B and 1.7B scales.

## Abstract
Scientific foundation models increasingly operate on continuous phenomena, yet still use discrete residual computation. We ask whether pretrained residual transformations can support additional latent computation without expanding the backbone. To test this possibility, we introduce Continuum-LM, which reuses these transformations as dynamical operators in a continuous-depth language model. Its hidden states evolve through an ordinary differential equation evaluated by higher-order numerical integration, with solver order and step size controlling computation. Across eight scientific tasks, Continuum-LM trains stably and improves mean exact-match accuracy by 7.77 and 10.96 percentage points over discrete counterparts at the 0.6B and 1.7B scales, respectively. At 0.6B, it also outperforms an Ouro-style recurrent control under matched parameter and residual-function evaluation budgets. Together, these results support extensible computational depth through parameter reuse, identifying continuous hidden-state evolution as a practical design dimension for scientific language models beyond parameter scaling.


## 精读解读（中文）
### 一、研究动机
科学基础模型 increasingly 处理连续现象，却仍采用离散残差计算和固定深度架构，扩展主要依赖数据、领域知识与参数规模。作者追问：预训练残差变换能否在不扩大骨干参数的情况下，通过连续深度和额外潜在计算提升 AI4Science 任务，并使求解器阶数与步长成为可控的计算维度。

### 二、技术方案（Method）
将预训练 Qwen3 的每个注意力与 FFN 残差分支分别视为局部 ODE dh/dt=F_j(h)、h(0)=h_j、t∈[0,1]，原残差更新对应单位步 Euler 离散，转换时复用原参数并用 RK2/RK4 高阶积分在中间隐状态重算归一化与变换，tokenizer、embedding、归一化结构、位置编码和输出头保持不变。默认采用两步中点 RK2，先进行连续深度 base training（主模型 10 万步，求解器消融 2 万步），再冻结连续深度骨干，在注意力 q/k/v/o 与 FFN up/gate/down 上插入 LoRA，在八个 AI4Science 任务上微调，并与参数匹配 Qwen3 及 Ouro 式循环控制比较。

### 三、结果（Result）
Continuum-LM 在两个参数尺度、八个任务上均优于同参数 Qwen3，平均 exact-match 在 0.6B 和 1.7B 分别提升 7.77 和 10.96 个百分点，达到 17.83% 和 24.33%；0.6B 超过 Qwen3-1.7B@SFT，1.7B 超过 Qwen3-4B@SFT 并接近 Qwen3-8B@SFT。0.6B 在匹配参数和残差函数评估预算下优于 Ouro 式循环控制；转换的边际计算回报为 1.05 个百分点/TFLOP，高于 0.6B→1.7B 缩放的 0.73，1.7B 路径为 0.52 对 0.49。

### 四、结论（Conclusion）
连续隐状态演化与预训练参数复用可作为科学语言模型除参数扩展外的实际架构设计维度，能够稳定训练并提供可扩展的计算深度。其收益具有任务与指标依赖性且需要额外推理计算，应被视为可调的计算组织方式，而非唯一真实推理轨迹的物理类比。

### 五、方法论与关键技术细节
参数尺度扫描在 1000 个训练样本上以 teacher-forced next-token 交叉熵评估，多数层—分支的最小损失系数接近 c=1，支持直接沿用预训练尺度初始化；求解器消融显示 RK2/RK4 在 2 万步内损失下降，默认两步中点 RK2 每个残差分支需 4 次函数评估，推理 FLOP 按 C≈2νP(Tin+Tout) 估计，采用 1024 输入/输出 token、batch size 1、KV cache，离散模型 ν=1、默认连续模型 ν=4，主实验 LoRA rank=16 并做三次独立运行。局限包括 NFE 与 FLOP 为 leading-order 近似、四倍分支评估带来推理成本、任务级及 rank 从 16 继续增大时收益不一致，且连续路径不假定存在唯一真实轨迹。
